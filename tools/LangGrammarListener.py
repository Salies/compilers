# Generated from LangGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LangGrammarParser import LangGrammarParser
else:
    from LangGrammarParser import LangGrammarParser

# This class defines a complete listener for a parse tree produced by LangGrammarParser.
class LangGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by LangGrammarParser#numero.
    def enterNumero(self, ctx:LangGrammarParser.NumeroContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#numero.
    def exitNumero(self, ctx:LangGrammarParser.NumeroContext):
        pass


    # Enter a parse tree produced by LangGrammarParser#relacao.
    def enterRelacao(self, ctx:LangGrammarParser.RelacaoContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#relacao.
    def exitRelacao(self, ctx:LangGrammarParser.RelacaoContext):
        pass


    # Enter a parse tree produced by LangGrammarParser#termo.
    def enterTermo(self, ctx:LangGrammarParser.TermoContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#termo.
    def exitTermo(self, ctx:LangGrammarParser.TermoContext):
        pass


    # Enter a parse tree produced by LangGrammarParser#expressaoSimples.
    def enterExpressaoSimples(self, ctx:LangGrammarParser.ExpressaoSimplesContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#expressaoSimples.
    def exitExpressaoSimples(self, ctx:LangGrammarParser.ExpressaoSimplesContext):
        pass


    # Enter a parse tree produced by LangGrammarParser#expressao.
    def enterExpressao(self, ctx:LangGrammarParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#expressao.
    def exitExpressao(self, ctx:LangGrammarParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by LangGrammarParser#fator.
    def enterFator(self, ctx:LangGrammarParser.FatorContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#fator.
    def exitFator(self, ctx:LangGrammarParser.FatorContext):
        pass


    # Enter a parse tree produced by LangGrammarParser#variavel.
    def enterVariavel(self, ctx:LangGrammarParser.VariavelContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#variavel.
    def exitVariavel(self, ctx:LangGrammarParser.VariavelContext):
        pass


    # Enter a parse tree produced by LangGrammarParser#declaracaoVariavel.
    def enterDeclaracaoVariavel(self, ctx:LangGrammarParser.DeclaracaoVariavelContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#declaracaoVariavel.
    def exitDeclaracaoVariavel(self, ctx:LangGrammarParser.DeclaracaoVariavelContext):
        pass


    # Enter a parse tree produced by LangGrammarParser#listaIdentificadores.
    def enterListaIdentificadores(self, ctx:LangGrammarParser.ListaIdentificadoresContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#listaIdentificadores.
    def exitListaIdentificadores(self, ctx:LangGrammarParser.ListaIdentificadoresContext):
        pass


    # Enter a parse tree produced by LangGrammarParser#parteDeclaracaoVariavel.
    def enterParteDeclaracaoVariavel(self, ctx:LangGrammarParser.ParteDeclaracaoVariavelContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#parteDeclaracaoVariavel.
    def exitParteDeclaracaoVariavel(self, ctx:LangGrammarParser.ParteDeclaracaoVariavelContext):
        pass


    # Enter a parse tree produced by LangGrammarParser#tipo.
    def enterTipo(self, ctx:LangGrammarParser.TipoContext):
        pass

    # Exit a parse tree produced by LangGrammarParser#tipo.
    def exitTipo(self, ctx:LangGrammarParser.TipoContext):
        pass



del LangGrammarParser