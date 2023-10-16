# Generated from ./tools/LangGrammar.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LangGrammar import LangGrammar
else:
    from LangGrammar import LangGrammar

# This class defines a complete listener for a parse tree produced by LangGrammar.
class LangGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by LangGrammar#numero.
    def enterNumero(self, ctx:LangGrammar.NumeroContext):
        pass

    # Exit a parse tree produced by LangGrammar#numero.
    def exitNumero(self, ctx:LangGrammar.NumeroContext):
        pass


    # Enter a parse tree produced by LangGrammar#relacao.
    def enterRelacao(self, ctx:LangGrammar.RelacaoContext):
        pass

    # Exit a parse tree produced by LangGrammar#relacao.
    def exitRelacao(self, ctx:LangGrammar.RelacaoContext):
        pass


    # Enter a parse tree produced by LangGrammar#termo.
    def enterTermo(self, ctx:LangGrammar.TermoContext):
        pass

    # Exit a parse tree produced by LangGrammar#termo.
    def exitTermo(self, ctx:LangGrammar.TermoContext):
        pass


    # Enter a parse tree produced by LangGrammar#expressaoSimples.
    def enterExpressaoSimples(self, ctx:LangGrammar.ExpressaoSimplesContext):
        pass

    # Exit a parse tree produced by LangGrammar#expressaoSimples.
    def exitExpressaoSimples(self, ctx:LangGrammar.ExpressaoSimplesContext):
        pass


    # Enter a parse tree produced by LangGrammar#expressaoSimples1.
    def enterExpressaoSimples1(self, ctx:LangGrammar.ExpressaoSimples1Context):
        pass

    # Exit a parse tree produced by LangGrammar#expressaoSimples1.
    def exitExpressaoSimples1(self, ctx:LangGrammar.ExpressaoSimples1Context):
        pass


    # Enter a parse tree produced by LangGrammar#expressao.
    def enterExpressao(self, ctx:LangGrammar.ExpressaoContext):
        pass

    # Exit a parse tree produced by LangGrammar#expressao.
    def exitExpressao(self, ctx:LangGrammar.ExpressaoContext):
        pass


    # Enter a parse tree produced by LangGrammar#expressao1.
    def enterExpressao1(self, ctx:LangGrammar.Expressao1Context):
        pass

    # Exit a parse tree produced by LangGrammar#expressao1.
    def exitExpressao1(self, ctx:LangGrammar.Expressao1Context):
        pass


    # Enter a parse tree produced by LangGrammar#fator.
    def enterFator(self, ctx:LangGrammar.FatorContext):
        pass

    # Exit a parse tree produced by LangGrammar#fator.
    def exitFator(self, ctx:LangGrammar.FatorContext):
        pass


    # Enter a parse tree produced by LangGrammar#variavel.
    def enterVariavel(self, ctx:LangGrammar.VariavelContext):
        pass

    # Exit a parse tree produced by LangGrammar#variavel.
    def exitVariavel(self, ctx:LangGrammar.VariavelContext):
        pass


    # Enter a parse tree produced by LangGrammar#variavel1.
    def enterVariavel1(self, ctx:LangGrammar.Variavel1Context):
        pass

    # Exit a parse tree produced by LangGrammar#variavel1.
    def exitVariavel1(self, ctx:LangGrammar.Variavel1Context):
        pass


    # Enter a parse tree produced by LangGrammar#declaracaoVariavel.
    def enterDeclaracaoVariavel(self, ctx:LangGrammar.DeclaracaoVariavelContext):
        pass

    # Exit a parse tree produced by LangGrammar#declaracaoVariavel.
    def exitDeclaracaoVariavel(self, ctx:LangGrammar.DeclaracaoVariavelContext):
        pass


    # Enter a parse tree produced by LangGrammar#listaIdentificadores.
    def enterListaIdentificadores(self, ctx:LangGrammar.ListaIdentificadoresContext):
        pass

    # Exit a parse tree produced by LangGrammar#listaIdentificadores.
    def exitListaIdentificadores(self, ctx:LangGrammar.ListaIdentificadoresContext):
        pass


    # Enter a parse tree produced by LangGrammar#listaIdentificadores1.
    def enterListaIdentificadores1(self, ctx:LangGrammar.ListaIdentificadores1Context):
        pass

    # Exit a parse tree produced by LangGrammar#listaIdentificadores1.
    def exitListaIdentificadores1(self, ctx:LangGrammar.ListaIdentificadores1Context):
        pass


    # Enter a parse tree produced by LangGrammar#parteDeclaracaoVariavel.
    def enterParteDeclaracaoVariavel(self, ctx:LangGrammar.ParteDeclaracaoVariavelContext):
        pass

    # Exit a parse tree produced by LangGrammar#parteDeclaracaoVariavel.
    def exitParteDeclaracaoVariavel(self, ctx:LangGrammar.ParteDeclaracaoVariavelContext):
        pass


    # Enter a parse tree produced by LangGrammar#parteDeclaracaoVariavel1.
    def enterParteDeclaracaoVariavel1(self, ctx:LangGrammar.ParteDeclaracaoVariavel1Context):
        pass

    # Exit a parse tree produced by LangGrammar#parteDeclaracaoVariavel1.
    def exitParteDeclaracaoVariavel1(self, ctx:LangGrammar.ParteDeclaracaoVariavel1Context):
        pass


    # Enter a parse tree produced by LangGrammar#tipo.
    def enterTipo(self, ctx:LangGrammar.TipoContext):
        pass

    # Exit a parse tree produced by LangGrammar#tipo.
    def exitTipo(self, ctx:LangGrammar.TipoContext):
        pass


    # Enter a parse tree produced by LangGrammar#programa.
    def enterPrograma(self, ctx:LangGrammar.ProgramaContext):
        pass

    # Exit a parse tree produced by LangGrammar#programa.
    def exitPrograma(self, ctx:LangGrammar.ProgramaContext):
        pass


    # Enter a parse tree produced by LangGrammar#bloco.
    def enterBloco(self, ctx:LangGrammar.BlocoContext):
        pass

    # Exit a parse tree produced by LangGrammar#bloco.
    def exitBloco(self, ctx:LangGrammar.BlocoContext):
        pass


    # Enter a parse tree produced by LangGrammar#parteDeclaracaoSubRotina.
    def enterParteDeclaracaoSubRotina(self, ctx:LangGrammar.ParteDeclaracaoSubRotinaContext):
        pass

    # Exit a parse tree produced by LangGrammar#parteDeclaracaoSubRotina.
    def exitParteDeclaracaoSubRotina(self, ctx:LangGrammar.ParteDeclaracaoSubRotinaContext):
        pass


    # Enter a parse tree produced by LangGrammar#parteDeclaracaoSubRotina1.
    def enterParteDeclaracaoSubRotina1(self, ctx:LangGrammar.ParteDeclaracaoSubRotina1Context):
        pass

    # Exit a parse tree produced by LangGrammar#parteDeclaracaoSubRotina1.
    def exitParteDeclaracaoSubRotina1(self, ctx:LangGrammar.ParteDeclaracaoSubRotina1Context):
        pass


    # Enter a parse tree produced by LangGrammar#declaracaoProcedimento.
    def enterDeclaracaoProcedimento(self, ctx:LangGrammar.DeclaracaoProcedimentoContext):
        pass

    # Exit a parse tree produced by LangGrammar#declaracaoProcedimento.
    def exitDeclaracaoProcedimento(self, ctx:LangGrammar.DeclaracaoProcedimentoContext):
        pass


    # Enter a parse tree produced by LangGrammar#declaracaoProcedimento1.
    def enterDeclaracaoProcedimento1(self, ctx:LangGrammar.DeclaracaoProcedimento1Context):
        pass

    # Exit a parse tree produced by LangGrammar#declaracaoProcedimento1.
    def exitDeclaracaoProcedimento1(self, ctx:LangGrammar.DeclaracaoProcedimento1Context):
        pass


    # Enter a parse tree produced by LangGrammar#parametrosFormais.
    def enterParametrosFormais(self, ctx:LangGrammar.ParametrosFormaisContext):
        pass

    # Exit a parse tree produced by LangGrammar#parametrosFormais.
    def exitParametrosFormais(self, ctx:LangGrammar.ParametrosFormaisContext):
        pass


    # Enter a parse tree produced by LangGrammar#parametrosFormais1.
    def enterParametrosFormais1(self, ctx:LangGrammar.ParametrosFormais1Context):
        pass

    # Exit a parse tree produced by LangGrammar#parametrosFormais1.
    def exitParametrosFormais1(self, ctx:LangGrammar.ParametrosFormais1Context):
        pass


    # Enter a parse tree produced by LangGrammar#secaoParametrosFormais.
    def enterSecaoParametrosFormais(self, ctx:LangGrammar.SecaoParametrosFormaisContext):
        pass

    # Exit a parse tree produced by LangGrammar#secaoParametrosFormais.
    def exitSecaoParametrosFormais(self, ctx:LangGrammar.SecaoParametrosFormaisContext):
        pass


    # Enter a parse tree produced by LangGrammar#secaoParametrosFormais1.
    def enterSecaoParametrosFormais1(self, ctx:LangGrammar.SecaoParametrosFormais1Context):
        pass

    # Exit a parse tree produced by LangGrammar#secaoParametrosFormais1.
    def exitSecaoParametrosFormais1(self, ctx:LangGrammar.SecaoParametrosFormais1Context):
        pass


    # Enter a parse tree produced by LangGrammar#comandoComposto.
    def enterComandoComposto(self, ctx:LangGrammar.ComandoCompostoContext):
        pass

    # Exit a parse tree produced by LangGrammar#comandoComposto.
    def exitComandoComposto(self, ctx:LangGrammar.ComandoCompostoContext):
        pass


    # Enter a parse tree produced by LangGrammar#comandoComposto1.
    def enterComandoComposto1(self, ctx:LangGrammar.ComandoComposto1Context):
        pass

    # Exit a parse tree produced by LangGrammar#comandoComposto1.
    def exitComandoComposto1(self, ctx:LangGrammar.ComandoComposto1Context):
        pass


    # Enter a parse tree produced by LangGrammar#comando.
    def enterComando(self, ctx:LangGrammar.ComandoContext):
        pass

    # Exit a parse tree produced by LangGrammar#comando.
    def exitComando(self, ctx:LangGrammar.ComandoContext):
        pass


    # Enter a parse tree produced by LangGrammar#atribuicao.
    def enterAtribuicao(self, ctx:LangGrammar.AtribuicaoContext):
        pass

    # Exit a parse tree produced by LangGrammar#atribuicao.
    def exitAtribuicao(self, ctx:LangGrammar.AtribuicaoContext):
        pass


    # Enter a parse tree produced by LangGrammar#chamadaProcedimento.
    def enterChamadaProcedimento(self, ctx:LangGrammar.ChamadaProcedimentoContext):
        pass

    # Exit a parse tree produced by LangGrammar#chamadaProcedimento.
    def exitChamadaProcedimento(self, ctx:LangGrammar.ChamadaProcedimentoContext):
        pass


    # Enter a parse tree produced by LangGrammar#chamadaProcedimento1.
    def enterChamadaProcedimento1(self, ctx:LangGrammar.ChamadaProcedimento1Context):
        pass

    # Exit a parse tree produced by LangGrammar#chamadaProcedimento1.
    def exitChamadaProcedimento1(self, ctx:LangGrammar.ChamadaProcedimento1Context):
        pass


    # Enter a parse tree produced by LangGrammar#comandoCondicional.
    def enterComandoCondicional(self, ctx:LangGrammar.ComandoCondicionalContext):
        pass

    # Exit a parse tree produced by LangGrammar#comandoCondicional.
    def exitComandoCondicional(self, ctx:LangGrammar.ComandoCondicionalContext):
        pass


    # Enter a parse tree produced by LangGrammar#comandoCondicional1.
    def enterComandoCondicional1(self, ctx:LangGrammar.ComandoCondicional1Context):
        pass

    # Exit a parse tree produced by LangGrammar#comandoCondicional1.
    def exitComandoCondicional1(self, ctx:LangGrammar.ComandoCondicional1Context):
        pass


    # Enter a parse tree produced by LangGrammar#comandoRepetitivo1.
    def enterComandoRepetitivo1(self, ctx:LangGrammar.ComandoRepetitivo1Context):
        pass

    # Exit a parse tree produced by LangGrammar#comandoRepetitivo1.
    def exitComandoRepetitivo1(self, ctx:LangGrammar.ComandoRepetitivo1Context):
        pass


    # Enter a parse tree produced by LangGrammar#listaExpressao.
    def enterListaExpressao(self, ctx:LangGrammar.ListaExpressaoContext):
        pass

    # Exit a parse tree produced by LangGrammar#listaExpressao.
    def exitListaExpressao(self, ctx:LangGrammar.ListaExpressaoContext):
        pass


    # Enter a parse tree produced by LangGrammar#listaExpressao1.
    def enterListaExpressao1(self, ctx:LangGrammar.ListaExpressao1Context):
        pass

    # Exit a parse tree produced by LangGrammar#listaExpressao1.
    def exitListaExpressao1(self, ctx:LangGrammar.ListaExpressao1Context):
        pass



del LangGrammar