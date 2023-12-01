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

    def define(self, symbol: Symbol):
        self.symbols[symbol.name] = symbol

    def resolve(self, name: str) -> Optional[Symbol]:
        return self.symbols.get(name)
    
# Objetivos da análise semântica:
# * Variável ou procedimento não declarado OK
# * Variável ou procedimento declarado mais de uma vez OK
# * Incompatibilidade de parâmetros formais e reais: número, ordem e tipo
# * Uso de variáveis variáveis de escopo inadequado - SEMI-OK (eu não fiz isso, mas sempre informo o escopo)
# * Atribuição de um inteiro a um booleano
# * Divisão que não é entre números inteiros
# * Variável declarada e nunca utilizada
# * Read e write com variáveis de tipo diferentes
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
        #print('sai do escopo')
        if self.current_scope.enclosing_scope is not None:
            self.current_scope = self.current_scope.enclosing_scope

    # A mudança de escopo ocorre quando se entra em um procedimento
    def visitDeclaracaoProcedimento(self, ctx: LangGrammar.DeclaracaoProcedimentoContext):
        nome_procedimento = ctx.IDENTIFICADOR().getText()
        # verifica se procedimento já foi declarado no escopo atual
        if self.current_scope.resolve(nome_procedimento) is not None:
            err = f"Procedimento '{nome_procedimento}' já declarado."
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
                err = f"Variável '{nome_variavel}' já declarada (escopo {self.current_scope.scope_name})."
                self.errorListener.addError(err, lista_id_ctx.start.line, lista_id_ctx.start.column)
            # verifica se a variável já foi declarada em um escopo superior
            elif self.current_scope.enclosing_scope is not None and self.current_scope.enclosing_scope.resolve(nome_variavel) is not None:
                err = f"Variável '{nome_variavel}' já declarada (escopo {self.current_scope.enclosing_scope.scope_name})."
                self.errorListener.addError(err, lista_id_ctx.start.line, lista_id_ctx.start.column)
                # mesmo assim, define para evitar erro de não declaração (afinal, este não é o problema tratado aqui)
                self.current_scope.define(symbol)
            else:
                self.current_scope.define(symbol)
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
        print('att - tipo da variável:', tipo_variavel)
        # agora verifica o tipo atribuído na expressão...
        # lembrando que aqui já passou por análise léxica e sintática, então a expressão é válida

        # como só há int e boolean, aqui usaremos uma lógica bem simples:
        # se qualquer um dos membros da expressão for um número, então o tipo da expressão é int
        # caso contrário, é boolean
        tipo_expressao = 'boolean'

        # outra coisa importante: uma expressão pode conter sub-expressões
        # enfim, tá aí o "detector de tipo"
        # não é a melhor coisa do mundo, mas tá funcionando, pelo visto
        expressao_simples = ctx.expressao().expressaoSimples()
        while expressao_simples is not None:
            termo = expressao_simples.termo()
            while termo is not None:
                fator = termo.fator()
                if fator is not None:
                    if fator.numero() is not None:
                        tipo_expressao = 'int'
                    elif fator.variavel() is not None:
                        # tenta achar a variável: em pascal a declaração sempre vem antes da atribuição
                        # então se ela não está aqui, é porque não foi declarada, e isso já foi tratado
                        nome_variavel = fator.variavel().IDENTIFICADOR().getText()
                        symbol = self.current_scope.resolve(nome_variavel)
                        assert symbol is not None
                        tipo_variavel = symbol.type
                        if tipo_variavel == 'int':
                            tipo_expressao = 'int'
                termo = termo.termo1()
            expressao_simples = expressao_simples.expressaoSimples1()

        print('tipos:', tipo_variavel, tipo_expressao)

        if tipo_variavel != tipo_expressao:
            err = f"Variável '{nome_variavel}' é do tipo '{tipo_variavel}', mas a expressão é do tipo '{tipo_expressao}'."
            return self.errorListener.addError(err, variavel.start.line, variavel.start.column)

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
        return self.visitChildren(ctx)