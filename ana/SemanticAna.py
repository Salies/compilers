from __future__ import annotations
from typing import Optional
from tools.LangGrammar import LangGrammar
from tools.LangGrammarVisitor import LangGrammarVisitor

class Symbol:
    def __init__(self: Symbol, name: str, type: str):
        self.name = name
        self.type = type

class Scope:
    def __init__(self, scope_name: str, enclosing_scope: Optional[Scope] = None):
        self.scope_name = scope_name
        self.enclosing_scope: Optional[Scope] = enclosing_scope
        self.symbols = {}
        self.symbol_used = {}
        self.var_decl_pos = {}
        self.procedure_signatures = {}

    def define(self, symbol: Symbol):
        self.symbols[symbol.name] = symbol
        self.symbol_used[symbol.name] = (False)

    def resolve(self, name: str) -> Optional[Symbol]:
        return self.symbols.get(name)
    
    def set_pos(self, name: str, pos: int):
        self.var_decl_pos[name] = pos
    
# Objetivos da análise semântica:
# * Variável ou procedimento não declarado OK
# * Variável ou procedimento declarado mais de uma vez OK
# * Incompatibilidade de parâmetros formais e reais: número, ordem e tipo
# * Uso de variáveis variáveis de escopo inadequado - SEMI-OK (eu não fiz isso, mas sempre informo o escopo)
# * Atribuição de um inteiro a um booleano OK
# * Divisão que não é entre números inteiros OK
# ^ impossível de acontecer, pois só há inteiros, mas eu entendi o que ele quis dizer
# ^ na vdd é verificar operação entre inteiros e booleanos
# * Variável declarada e nunca utilizada OK
# * Read e write com variáveis de tipo diferentes ??? Não entendi
# * Tratamento de escopo
#   - Erro: variável local a um procedimento utilizada no programa principal
# * Extra: uso errado de procedimentos (chamada sem argumentos, chamada com argumentos a mais, etc)
# ^ sobre isso, acho que está incluso em "ordem", em "ordem e tipo"

# LEMBRETE: DO JEITO QUE ESTÁ, VARIÁVEIS E PROCEDIMENTOS PODEM TER O MESMO NOME

# Esta classe herda e sobrescreve o visitor do ANTLR para fazer a análise semântica
class SemanticAna(LangGrammarVisitor):
    
    def __init__(self, errorListener):
        self.current_scope: Scope = Scope("global")
        self.errorListener = errorListener

    def enterScope(self, scope_name: str):
        #print('entrei no escopo', scope_name)
        scope = Scope(scope_name, self.current_scope)
        self.current_scope = scope

    def exitScope(self):
        print('sai do escopo')
        # verifica se há variáveis não utilizadas
        for symbol in self.current_scope.symbols.values():
            print('symbol', symbol.name, symbol.type)
            if not self.current_scope.symbol_used[symbol.name]:
                err = f"Variável '{symbol.name}' declarada, mas não utilizada."
                x, y = self.current_scope.var_decl_pos[symbol.name]
                self.errorListener.addError(err, x, y)

        if self.current_scope.enclosing_scope is not None:
            self.current_scope = self.current_scope.enclosing_scope

    def check_type(self, type):
        if type == 'int' or type == 'boolean':
            return 'variável'
        return 'procedimento'
    
    # A mudança de escopo ocorre quando se entra em um procedimento
    def visitDeclaracaoProcedimento(self, ctx: LangGrammar.DeclaracaoProcedimentoContext):
        nome_procedimento = ctx.IDENTIFICADOR().getText()
        # verifica se procedimento já foi declarado no escopo atual
        if self.current_scope.resolve(nome_procedimento) is not None:
            err = f"Símbolo '{nome_procedimento}' já declarado (escopo {self.current_scope.scope_name}), como {self.check_type(self.current_scope.resolve(nome_procedimento).type)}."
            self.errorListener.addError(err, ctx.start.line, ctx.start.column)
            # não vou dar return aqui... espero que não bugue por causa dos nomes
        self.current_scope.define(Symbol(nome_procedimento, "procedimento"))
        self.enterScope(nome_procedimento)
        self.visitChildren(ctx)
        self.exitScope()

    # Declaração de variável
    def visitDeclaracaoVariavel(self, ctx: LangGrammar.DeclaracaoVariavelContext):
        tipo = ctx.tipo().getText()
        lista_id_ctx = ctx.listaIdentificadores()
        while lista_id_ctx.IDENTIFICADOR() is not None:
            nome_variavel = lista_id_ctx.IDENTIFICADOR().getText()
            symbol = Symbol(nome_variavel, tipo)
            # verifica se variável já foi declarada no escopo atual
            if self.current_scope.resolve(nome_variavel) is not None:
                err = f"Símbolo '{nome_variavel}' já declarado (escopo {self.current_scope.scope_name}), como {self.check_type(self.current_scope.resolve(nome_variavel).type)}."
                self.errorListener.addError(err, lista_id_ctx.start.line, lista_id_ctx.start.column)
            # verifica se a variável já foi declarada em um escopo superior
            elif self.current_scope.enclosing_scope is not None and self.current_scope.enclosing_scope.resolve(nome_variavel) is not None:
                err = f"Símbolo '{nome_variavel}' já declarado (escopo {self.current_scope.enclosing_scope.scope_name}), como {self.check_type(self.current_scope.enclosing_scope.resolve(nome_variavel).type)}."
                self.errorListener.addError(err, lista_id_ctx.start.line, lista_id_ctx.start.column)
                # mesmo assim, define para evitar erro de não declaração (afinal, este não é o problema tratado aqui)
                self.current_scope.define(symbol)
                self.current_scope.set_pos(nome_variavel, (lista_id_ctx.start.line, lista_id_ctx.start.column))
            else:
                self.current_scope.define(symbol)
                self.current_scope.set_pos(nome_variavel, (lista_id_ctx.start.line, lista_id_ctx.start.column))
            lista_id_ctx = lista_id_ctx.listaIdentificadores1()

    # Variável não declarada
    # Variáveis só aparecem em dois contextos, além de sua declaração:
    # Atribuição (atribuicao) e fator
    def visitAtribuicao(self, ctx:LangGrammar.AtribuicaoContext):
        variavel = ctx.variavel()
        assert variavel is not None
        nome_variavel = variavel.IDENTIFICADOR().getText()
        nome_escopo = self.current_scope.scope_name
        symbol = self.current_scope.resolve(nome_variavel)
        if symbol is None:
           err = f"Variável '{nome_variavel}' não declarada (escopo {nome_escopo})."
           return self.errorListener.addError(err, variavel.start.line, variavel.start.column)
        
        # Verificação de incompatibilidade de tipos
        # primeiramente, pega o tipo da variável
        tipo_variavel = symbol.type
        #print('att - tipo da variável:', tipo_variavel)
        # agora verifica o tipo atribuído na expressão...
        # lembrando que aqui já passou por análise léxica e sintática, então a expressão é válida

        # como só há int e boolean, aqui usaremos uma lógica bem simples:
        # se qualquer um dos membros da expressão for um número, então o tipo da expressão é int
        # caso contrário, é boolean
        tipo_expressao = self.encontrarTipoExpressao(ctx.expressao())
        #_, tipo_expressao = self.visitExpressao(ctx.expressao())
        # não era pra precisar, mas reporta tipo incompatível aqui também
        if tipo_expressao == 'mixed':
            err = f"Expressão possui tipos incompatíveis."
            self.errorListener.addError(err, ctx.start.line, ctx.start.column)

        if tipo_variavel != tipo_expressao:
            if tipo_variavel == 'procedimento':
                err = f"Tentativa de atribuição de valor a procedimento '{nome_variavel}'."
                return self.errorListener.addError(err, variavel.start.line, variavel.start.column)
            err = f"Variável '{nome_variavel}' é do tipo '{tipo_variavel}', mas a expressão é do tipo '{tipo_expressao}'."
            return self.errorListener.addError(err, variavel.start.line, variavel.start.column)
        
        # se tudo estiver ok, define o símbolo como usado
        self.current_scope.symbol_used[nome_variavel] = True

        return self.visitChildren(ctx)

    def visitFator(self, ctx: LangGrammar.FatorContext):
        variavel = ctx.variavel()
        if variavel is not None:
            nome_variavel = variavel.IDENTIFICADOR().getText()
            nome_escopo = self.current_scope.scope_name
            symbol = self.current_scope.resolve(nome_variavel)
            if symbol is None:
                err = f"Variável '{nome_variavel}' não declarada (escopo {nome_escopo})."
                return self.errorListener.addError(err, variavel.start.line, variavel.start.column)
            
            # se tudo estiver ok, define o símbolo como usado
            self.current_scope.symbol_used[nome_variavel] = True
        return self.visitChildren(ctx)
    
    # Procedimento não declarado
    def visitChamadaProcedimento(self, ctx: LangGrammar.ChamadaProcedimentoContext):
        if ctx.IDENTIFICADOR() is not None:
            nome_procedimento = ctx.IDENTIFICADOR().getText()
            print(nome_procedimento)
            symbol = self.current_scope.resolve(nome_procedimento)
            if symbol is None:
                err = f"Procedimento '{nome_procedimento}' não declarado."
                return self.errorListener.addError(err, ctx.start.line, ctx.start.column)
            # verificar assinatura do procedimento
        return self.visitChildren(ctx)
    
    def visitExpressao(self, ctx: LangGrammar.ExpressaoContext):
        print('visitando expressao')
        # verifica tipo da expressão
        tipo = self.encontrarTipoExpressao(ctx)
        if tipo == 'mixed':
            err = f"Expressão possui tipos incompatíveis."
            self.errorListener.addError(err, ctx.start.line, ctx.start.column)

        return self.visitChildren(ctx), tipo

    '''
    fator:
        ( variavel | numero | ( LP expressao RP ) | ( NOT fator ) | CONST_TRUE | CONST_FALSE ) ;
    '''

    def encontrarTipoExpressao(self, expressao):
        tipos = []
        expressao_simples = expressao.expressaoSimples()
        while expressao_simples is not None:
            # vê se a expressão simples tem sub ou sum (se tiver já coloca o tipo como int)
            sub = expressao_simples.SUB()
            sum = expressao_simples.SUM()
            if sub is not None or sum is not None:
                tipos.append('int')
            termo = expressao_simples.termo()
            # se termo1 tiver MUL ou INT_DIV, já adiciona o tipo como int
            if termo is not None:
                if termo.termo1() is not None:
                    mul = termo.termo1().MUL()
                    int_div = termo.termo1().INT_DIV()
                    if mul is not None or int_div is not None:
                        tipos.append('int')
            while termo is not None:
                fator = termo.fator()
                # fator pode ser: variável, número, booleano ou expressão entre parênteses
                if fator is not None:
                    if fator.numero() is not None:
                        tipos.append('int')
                    if fator.variavel() is not None:
                        # tenta achar a variável: em pascal a declaração sempre vem antes da atribuição
                        # então se ela não está aqui, é porque não foi declarada, e isso já foi tratado
                        nome_variavel = fator.variavel().IDENTIFICADOR().getText()
                        symbol = self.current_scope.resolve(nome_variavel)
                        if symbol is not None:
                            tipo_variavel = symbol.type
                            if tipo_variavel == 'int':
                                tipos.append('int')
                    if fator.CONST_TRUE() is not None or fator.CONST_FALSE() is not None:
                        tipos.append('boolean')
                    if fator.expressao() is not None:
                        tipos.append(self.encontrarTipoExpressao(fator.expressao()))
                termo = termo.termo1()
            expressao_simples = expressao_simples.expressaoSimples1()
        tipo = 'int'
        if ('boolean' in tipos and 'int' in tipos) or 'mixed' in tipos:
            tipo = 'mixed'
        elif 'boolean' in tipos:
            tipo = 'boolean'
        print('tipo final:', tipo)
        return tipo
    
    def encontrarVarGlobaisNaoUtilizadas(self):
        # pega o escopo global
        scope = self.current_scope
        while scope.enclosing_scope is not None:
            scope = scope.enclosing_scope
        # verifica se há variáveis não utilizadas
        for symbol in scope.symbols.values():
            if symbol.type == 'procedimento':
                continue
            if not scope.symbol_used[symbol.name]:
                err = f"Variável '{symbol.name}' declarada, mas não utilizada."
                x, y = scope.var_decl_pos[symbol.name]
                self.errorListener.addError(err, x, y)
