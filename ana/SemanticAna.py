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
class SemanticAna(LangGrammarVisitor):
    
    def __init__(self):
        self.current_scope: Optional[Scope] = None


    def enterScope(self, scope_name: str):
        scope = Scope(scope_name, self.current_scope)
        self.current_scope = scope


    def exitScope(self):
        self.current_scope = self.current_scope.enclosing_scope


    # Visit a parse tree produced by LangGrammar#numero.
    def visitNumero(self, ctx:LangGrammar.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#relacao.
    def visitRelacao(self, ctx:LangGrammar.RelacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#termo.
    def visitTermo(self, ctx:LangGrammar.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#termo1.
    def visitTermo1(self, ctx:LangGrammar.Termo1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#expressaoSimples.
    def visitExpressaoSimples(self, ctx:LangGrammar.ExpressaoSimplesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#expressaoSimples1.
    def visitExpressaoSimples1(self, ctx:LangGrammar.ExpressaoSimples1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#expressao.
    def visitExpressao(self, ctx:LangGrammar.ExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#expressao1.
    def visitExpressao1(self, ctx:LangGrammar.Expressao1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#fator.
    def visitFator(self, ctx:LangGrammar.FatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#variavel.
    def visitVariavel(self, ctx:LangGrammar.VariavelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#variavel1.
    def visitVariavel1(self, ctx:LangGrammar.Variavel1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#declaracaoVariavel.
    def visitDeclaracaoVariavel(self, ctx:LangGrammar.DeclaracaoVariavelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#listaIdentificadores.
    def visitListaIdentificadores(self, ctx:LangGrammar.ListaIdentificadoresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#listaIdentificadores1.
    def visitListaIdentificadores1(self, ctx:LangGrammar.ListaIdentificadores1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#parteDeclaracaoVariavel.
    def visitParteDeclaracaoVariavel(self, ctx:LangGrammar.ParteDeclaracaoVariavelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#parteDeclaracaoVariavel1.
    def visitParteDeclaracaoVariavel1(self, ctx:LangGrammar.ParteDeclaracaoVariavel1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#tipo.
    def visitTipo(self, ctx:LangGrammar.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#programa.
    def visitPrograma(self, ctx:LangGrammar.ProgramaContext):
        self.enterScope("main")
        self.visitChildren(ctx)
        return self.exitScope()


    # Visit a parse tree produced by LangGrammar#bloco.
    def visitBloco(self, ctx:LangGrammar.BlocoContext):
        
        return self.exitScope(ctx)


    # Visit a parse tree produced by LangGrammar#parteDeclaracaoSubRotina.
    def visitParteDeclaracaoSubRotina(self, ctx:LangGrammar.ParteDeclaracaoSubRotinaContext):
        nome_subrotina = ctx.IDENTIFIER().getText()
        if self.current_scope.resolve(nome_subrotina):
            self.errorListener.semanticError(
                ctx.IDENTIFIER().symbol.line,
                ctx.IDENTIFIER().symbol.column,
                f"Subrotina {nome_subrotina} já declarada!",
            )
        else:
            self.current_scope.define(Symbol(nome_subrotina, "subrotina"))
            self.enterScope(nome_subrotina)
            self.visitChildren(ctx)
            return self.exitScope()


    # Visit a parse tree produced by LangGrammar#parteDeclaracaoSubRotina1.
    def visitParteDeclaracaoSubRotina1(self, ctx:LangGrammar.ParteDeclaracaoSubRotina1Context):
        nome_subrotina = ctx.IDENTIFIER().getText()
        if self.current_scope.resolve(nome_subrotina):
            self.errorListener.semanticError(
                ctx.IDENTIFIER().symbol.line,
                ctx.IDENTIFIER().symbol.column,
                f"Subrotina {nome_subrotina} já declarada!",
            )
        else:
            self.current_scope.define(Symbol(nome_subrotina, "subrotina"))
            self.enterScope(nome_subrotina)
            self.visitChildren(ctx)
        return self.exitScope()


    # Visit a parse tree produced by LangGrammar#declaracaoProcedimento.
    def visitDeclaracaoProcedimento(self, ctx:LangGrammar.DeclaracaoProcedimentoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#declaracaoProcedimento1.
    def visitDeclaracaoProcedimento1(self, ctx:LangGrammar.DeclaracaoProcedimento1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#parametrosFormais.
    def visitParametrosFormais(self, ctx:LangGrammar.ParametrosFormaisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#parametrosFormais1.
    def visitParametrosFormais1(self, ctx:LangGrammar.ParametrosFormais1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#secaoParametrosFormais.
    def visitSecaoParametrosFormais(self, ctx:LangGrammar.SecaoParametrosFormaisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#secaoParametrosFormais1.
    def visitSecaoParametrosFormais1(self, ctx:LangGrammar.SecaoParametrosFormais1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#comandoComposto.
    def visitComandoComposto(self, ctx:LangGrammar.ComandoCompostoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#comandoComposto1.
    def visitComandoComposto1(self, ctx:LangGrammar.ComandoComposto1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#comando.
    def visitComando(self, ctx:LangGrammar.ComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#atribuicao.
    def visitAtribuicao(self, ctx:LangGrammar.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#chamadaProcedimento.
    def visitChamadaProcedimento(self, ctx:LangGrammar.ChamadaProcedimentoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#chamadaProcedimento1.
    def visitChamadaProcedimento1(self, ctx:LangGrammar.ChamadaProcedimento1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#comandoCondicional.
    def visitComandoCondicional(self, ctx:LangGrammar.ComandoCondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#comandoCondicional1.
    def visitComandoCondicional1(self, ctx:LangGrammar.ComandoCondicional1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#comandoRepetitivo1.
    def visitComandoRepetitivo1(self, ctx:LangGrammar.ComandoRepetitivo1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#listaExpressao.
    def visitListaExpressao(self, ctx:LangGrammar.ListaExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#listaExpressao1.
    def visitListaExpressao1(self, ctx:LangGrammar.ListaExpressao1Context):
        return self.visitChildren(ctx)