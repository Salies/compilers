# Generated from ./tools/LangGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LangGrammar import LangGrammar
else:
    from LangGrammar import LangGrammar

# This class defines a complete generic visitor for a parse tree produced by LangGrammar.

class LangGrammarVisitor(ParseTreeVisitor):

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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#bloco.
    def visitBloco(self, ctx:LangGrammar.BlocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#parteDeclaracaoSubRotina.
    def visitParteDeclaracaoSubRotina(self, ctx:LangGrammar.ParteDeclaracaoSubRotinaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangGrammar#parteDeclaracaoSubRotina1.
    def visitParteDeclaracaoSubRotina1(self, ctx:LangGrammar.ParteDeclaracaoSubRotina1Context):
        return self.visitChildren(ctx)


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



del LangGrammar