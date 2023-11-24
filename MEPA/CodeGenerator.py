from __future__ import annotations
from typing import Optional
from tools.LangGrammar import LangGrammar
from tools.LangGrammarVisitor import LangGrammarVisitor

class Symbol:
    def __init__(self: Symbol, name: str, pos: int):
        self.name = name
        self.pos_stack = pos

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
# * Variável ou procedimento não declarado
# * Variável ou procedimento declarado mais de uma vez
# * Incompatibilidade de parâmetros formais e reais: número, ordeme tipo
# * Uso de variáveis variáveis de escopo inadequado
# * Atribuição de um inteiro a um booleano
# * Divisão que não é entre números inteiros
# * Variável declarada e nunca utilizada
# * Read e write com variáveis de tipo diferentes
# * Tratamento de escopo
#   - Erro: variável local a um procedimento utilizada no programa principa

# Esta classe herda e sobrescreve o visitor do ANTLR para fazer a análise semântica
class CodeGenerator(LangGrammarVisitor):
    
    def __init__(self, errorListener):
        self.current_scope: Scope = Scope("global")
        self.errorListener = errorListener
        self.generated_code = []

    def enterScope(self, scope_name: str):
        scope = Scope(scope_name, self.current_scope)
        self.current_scope = scope

    def exitScope(self):
        if self.current_scope.enclosing_scope is not None:
            self.current_scope = self.current_scope.enclosing_scope

    def visitPrograma(self, ctx: LangGrammar.ProgramaContext):
        self.generated_code.append("INPP\n")
        self.visitChildren(ctx)
        self.generated_code("PARA\n")
        self.salvarPrograma()

    # Variável não declarada
    # Variáveis só aparecem em dois contextos, além de sua declaração:
    # Atribuição (atribuicao) e fator

    # Visit a parse tree produced by LangGrammar#atribuicao.
    def visitAtribuicao(self, ctx:LangGrammar.AtribuicaoContext):
        variavel = ctx.variavel()
        assert variavel is not None
        nome_variavel = variavel.IDENTIFICADOR().getText()
        symbol = self.current_scope.resolve(nome_variavel)
        return self.visitChildren(ctx)

    def visitListaIdentificadores(self, ctx: LangGrammar.ListaIdentificadoresContext):
        self.generated_code.append("AMEM 1\n")
        variavel = ctx.variavel()
        nome_variavel = variavel.IDENTIFICADOR().getText()
        self.current_scope.define(Symbol(self.current_scope.resolve(nome_variavel), len(self.current_scope.symbols)))
        return self.visitChildren(ctx)

    def visitListaIdentificadores1(self, ctx: LangGrammar.ListaIdentificadoresContext):
        self.generated_code.append("AMEM 1\n")
        variavel = ctx.variavel()
        nome_variavel = variavel.IDENTIFICADOR().getText()
        self.current_scope.define(Symbol(self.current_scope.resolve(nome_variavel), len(self.current_scope.symbols)))
        return self.visitChildren(ctx)


    def visitExpressaoSimples(self, ctx:LangGrammar.ExpressaoSimplesContext ):
        self.visitChildren(ctx.getChild(0))
        if(ctx.SUB() != None):
            self.generated_code.append("INVR\n")
        self.visitChildren(ctx.getChild(1))
        return

    def visitExpressaoSimples1(self, ctx:LangGrammar.ExpressaoSimples1Context ):
        self.visitChildren(ctx)
        if(ctx.SUB() != None):
            self.generated_code.append("SUB\n")
        elif(ctx.SUM() != None):
            self.generated_code.append("SUM\n")
        elif(ctx.OR() != None):
            self.generated_code.append("DISJ\n")
        return

    def visitFator(self, ctx: LangGrammar.FatorContext):
        if(ctx.variavel() != None):
            #verificar como pegar a posicao da variavel no stack de dados
            #num = variavel.pos_in_stack()
            #self.generated_code.append(f"CRVR {num}")
            pass
        elif(ctx.numero() != None):
            num = ctx.numero()
            self.generated_code.append(f"CRVL {num}")
        #TODO verificar como representar booleanos na MEPA
        elif(ctx.CONST_FALSE() != None):
            self.generated_code.append(f"CRVL 0")
        elif(ctx.CONST_TRUE() != None):
            self.generated_code.append("CRVL 1")
        self.visitChildren(ctx)
        if(ctx.NOT() != None):
            self.generated_code.append("NEGA")
        
    #TODO
    def visitFator1(self, ctx: LangGrammar.FatorContext):
        if(ctx.variavel() != None):
            #verificar como pegar a posicao da variavel no stack de dados
            #num = variavel.pos_in_stack()
            #self.generated_code.append(f"CRVR {num}")
            pass
        elif(ctx.numero() != None):
            num = ctx.numero()
            self.generated_code.append(f"CRVL {num}")
        #TODO verificar como representar booleanos na MEPA
        elif(ctx.CONST_FALSE() != None):
            self.generated_code.append(f"CRVL 0")
        elif(ctx.CONST_TRUE() != None):
            self.generated_code.append("CRVL 1")
        self.visitChildren(ctx)
        if(ctx.NOT() != None):
            self.generated_code.append("NEGA")

    def visitComandoRepetitivo1(self, ctx:LangGrammar.ComandoRepetitivo1Context):
        inicio_laco = len(self.generated_code()) - 1
        self.generated_code.append("NADA")
        #visita a expressao e adiciona um placeholder para indicar o final do bloco de repeticao
        self.visitChildren(ctx.getChild(0))
        instruction_reminder = len(self.generated_code())
        self.generated_code.append("PLACEHOLDER")
        self.visitChildren(ctx.getChild(1))
        self.generated_code.append(f"DSVS {inicio_laco}")
        self.generated_code[instruction_reminder] = f"DSVF {instruction_reminder}"

    def visitAtribuicao(self, ctx: LangGrammar.AtribuicaoContext):
        variavel = ctx.variavel()
        nome_variavel = variavel.IDENTIFICADOR().getText()
        symbol = self.current_scope.symbols.get(nome_variavel)
        num = symbol.pos_stack
        self.visitChildren(ctx)
        self.generated_code.append(f"ARMZ {num}")

    def visitComandoCondicional(self, ctx: LangGrammar.ComandoCondicionalContext):
        self.visitChildren(ctx.getChild(0))
        instruction_reminder = len(self.generated_code())
        self.generated_code.append("PLACEHOLDER")
        self.visitChildren(ctx.getChild(1))
        self.generated_code[instruction_reminder] = f"DSVF {len(self.generated_code)}"
        self.generated_code.append("NADA")

    def salvarPrograma(self):
        #TODO
        codigo_final = "".join(self.generated_code)
        print(codigo_final)
        f = open("mepa_code.exe", "w")
        f.write(codigo_final)
        f.close()