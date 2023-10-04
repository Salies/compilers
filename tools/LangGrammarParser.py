# Generated from LangGrammar.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,47,90,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,1,1,1,1,2,1,2,1,2,
        5,2,30,8,2,10,2,12,2,33,9,2,1,3,3,3,36,8,3,1,3,1,3,1,3,5,3,41,8,
        3,10,3,12,3,44,9,3,1,4,1,4,1,4,1,4,3,4,50,8,4,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,3,5,60,8,5,1,6,1,6,3,6,64,8,6,1,7,1,7,1,7,1,8,1,8,
        1,8,5,8,72,8,8,10,8,12,8,75,9,8,1,9,1,9,1,9,5,9,80,8,9,10,9,12,9,
        83,9,9,1,9,1,9,1,9,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,
        20,0,6,1,0,41,42,1,0,34,39,3,0,20,20,23,23,25,25,2,0,22,22,26,26,
        3,0,19,19,22,22,26,26,1,0,8,9,88,0,22,1,0,0,0,2,24,1,0,0,0,4,26,
        1,0,0,0,6,35,1,0,0,0,8,45,1,0,0,0,10,59,1,0,0,0,12,61,1,0,0,0,14,
        65,1,0,0,0,16,68,1,0,0,0,18,76,1,0,0,0,20,87,1,0,0,0,22,23,7,0,0,
        0,23,1,1,0,0,0,24,25,7,1,0,0,25,3,1,0,0,0,26,31,3,10,5,0,27,28,7,
        2,0,0,28,30,3,10,5,0,29,27,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,
        32,1,0,0,0,32,5,1,0,0,0,33,31,1,0,0,0,34,36,7,3,0,0,35,34,1,0,0,
        0,35,36,1,0,0,0,36,37,1,0,0,0,37,42,3,4,2,0,38,39,7,4,0,0,39,41,
        3,4,2,0,40,38,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,
        43,7,1,0,0,0,44,42,1,0,0,0,45,49,3,6,3,0,46,47,3,2,1,0,47,48,3,6,
        3,0,48,50,1,0,0,0,49,46,1,0,0,0,49,50,1,0,0,0,50,9,1,0,0,0,51,60,
        3,12,6,0,52,60,3,0,0,0,53,54,5,27,0,0,54,55,3,8,4,0,55,56,5,28,0,
        0,56,60,1,0,0,0,57,58,5,21,0,0,58,60,3,10,5,0,59,51,1,0,0,0,59,52,
        1,0,0,0,59,53,1,0,0,0,59,57,1,0,0,0,60,11,1,0,0,0,61,63,5,40,0,0,
        62,64,3,8,4,0,63,62,1,0,0,0,63,64,1,0,0,0,64,13,1,0,0,0,65,66,3,
        20,10,0,66,67,3,16,8,0,67,15,1,0,0,0,68,73,5,40,0,0,69,70,5,6,0,
        0,70,72,5,40,0,0,71,69,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,
        1,0,0,0,74,17,1,0,0,0,75,73,1,0,0,0,76,81,3,14,7,0,77,78,5,3,0,0,
        78,80,3,14,7,0,79,77,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,
        0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,5,3,0,0,85,86,5,0,0,1,86,
        19,1,0,0,0,87,88,7,5,0,0,88,21,1,0,0,0,8,31,35,42,49,59,63,73,81
    ]

class LangGrammarParser ( Parser ):

    grammarFileName = "LangGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'procedure'", "';'", "':='", 
                     "':'", "','", "'var'", "'int'", "'boolean'", "'read'", 
                     "'write'", "'true'", "'false'", "'begin'", "'end'", 
                     "'if'", "'then'", "'else'", "'or'", "'and'", "'not'", 
                     "'+'", "'*'", "'/'", "'div'", "'-'", "'('", "')'", 
                     "'['", "']'", "'while'", "'do'", "'.'", "'='", "'<>'", 
                     "'<'", "'>'", "'<='", "'>='" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "PROCEDURE", "SEMICOLON", 
                      "ATTRIB", "COLON", "COMMA", "VAR", "TYPE_INT", "TYPE_BOOL", 
                      "PROC_READ", "PROC_WRITE", "CONST_TRUE", "CONST_FALSE", 
                      "BEGIN", "END", "IF", "THEN", "ELSE", "OR", "AND", 
                      "NOT", "SUM", "MUL", "DIV", "INT_DIV", "SUB", "LP", 
                      "RP", "LB", "RB", "WHILE", "DO", "DOT", "EQUAL", "DIFF", 
                      "LT", "GT", "LTE", "GTE", "IDENTIFICADOR", "INT", 
                      "REAL", "COMMENT", "MULTILINE_COMMENT", "WS", "INVALID_TOKEN", 
                      "INVALID" ]

    RULE_numero = 0
    RULE_relacao = 1
    RULE_termo = 2
    RULE_expressaoSimples = 3
    RULE_expressao = 4
    RULE_fator = 5
    RULE_variavel = 6
    RULE_declaracaoVariavel = 7
    RULE_listaIdentificadores = 8
    RULE_parteDeclaracaoVariavel = 9
    RULE_tipo = 10

    ruleNames =  [ "numero", "relacao", "termo", "expressaoSimples", "expressao", 
                   "fator", "variavel", "declaracaoVariavel", "listaIdentificadores", 
                   "parteDeclaracaoVariavel", "tipo" ]

    EOF = Token.EOF
    PROGRAM=1
    PROCEDURE=2
    SEMICOLON=3
    ATTRIB=4
    COLON=5
    COMMA=6
    VAR=7
    TYPE_INT=8
    TYPE_BOOL=9
    PROC_READ=10
    PROC_WRITE=11
    CONST_TRUE=12
    CONST_FALSE=13
    BEGIN=14
    END=15
    IF=16
    THEN=17
    ELSE=18
    OR=19
    AND=20
    NOT=21
    SUM=22
    MUL=23
    DIV=24
    INT_DIV=25
    SUB=26
    LP=27
    RP=28
    LB=29
    RB=30
    WHILE=31
    DO=32
    DOT=33
    EQUAL=34
    DIFF=35
    LT=36
    GT=37
    LTE=38
    GTE=39
    IDENTIFICADOR=40
    INT=41
    REAL=42
    COMMENT=43
    MULTILINE_COMMENT=44
    WS=45
    INVALID_TOKEN=46
    INVALID=47

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class NumeroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(LangGrammarParser.INT, 0)

        def REAL(self):
            return self.getToken(LangGrammarParser.REAL, 0)

        def getRuleIndex(self):
            return LangGrammarParser.RULE_numero

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)




    def numero(self):

        localctx = LangGrammarParser.NumeroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_numero)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            _la = self._input.LA(1)
            if not(_la==41 or _la==42):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(LangGrammarParser.EQUAL, 0)

        def DIFF(self):
            return self.getToken(LangGrammarParser.DIFF, 0)

        def LT(self):
            return self.getToken(LangGrammarParser.LT, 0)

        def LTE(self):
            return self.getToken(LangGrammarParser.LTE, 0)

        def GT(self):
            return self.getToken(LangGrammarParser.GT, 0)

        def GTE(self):
            return self.getToken(LangGrammarParser.GTE, 0)

        def getRuleIndex(self):
            return LangGrammarParser.RULE_relacao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelacao" ):
                listener.enterRelacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelacao" ):
                listener.exitRelacao(self)




    def relacao(self):

        localctx = LangGrammarParser.RelacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_relacao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1082331758592) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangGrammarParser.FatorContext)
            else:
                return self.getTypedRuleContext(LangGrammarParser.FatorContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(LangGrammarParser.MUL)
            else:
                return self.getToken(LangGrammarParser.MUL, i)

        def INT_DIV(self, i:int=None):
            if i is None:
                return self.getTokens(LangGrammarParser.INT_DIV)
            else:
                return self.getToken(LangGrammarParser.INT_DIV, i)

        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(LangGrammarParser.AND)
            else:
                return self.getToken(LangGrammarParser.AND, i)

        def getRuleIndex(self):
            return LangGrammarParser.RULE_termo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo" ):
                listener.enterTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo" ):
                listener.exitTermo(self)




    def termo(self):

        localctx = LangGrammarParser.TermoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_termo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.fator()
            self.state = 31
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 27
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 42991616) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 28
                    self.fator() 
                self.state = 33
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoSimplesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangGrammarParser.TermoContext)
            else:
                return self.getTypedRuleContext(LangGrammarParser.TermoContext,i)


        def SUM(self, i:int=None):
            if i is None:
                return self.getTokens(LangGrammarParser.SUM)
            else:
                return self.getToken(LangGrammarParser.SUM, i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(LangGrammarParser.SUB)
            else:
                return self.getToken(LangGrammarParser.SUB, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(LangGrammarParser.OR)
            else:
                return self.getToken(LangGrammarParser.OR, i)

        def getRuleIndex(self):
            return LangGrammarParser.RULE_expressaoSimples

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressaoSimples" ):
                listener.enterExpressaoSimples(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressaoSimples" ):
                listener.exitExpressaoSimples(self)




    def expressaoSimples(self):

        localctx = LangGrammarParser.ExpressaoSimplesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expressaoSimples)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22 or _la==26:
                self.state = 34
                _la = self._input.LA(1)
                if not(_la==22 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 37
            self.termo()
            self.state = 42
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 38
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 71827456) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 39
                    self.termo() 
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressaoSimples(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangGrammarParser.ExpressaoSimplesContext)
            else:
                return self.getTypedRuleContext(LangGrammarParser.ExpressaoSimplesContext,i)


        def relacao(self):
            return self.getTypedRuleContext(LangGrammarParser.RelacaoContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)




    def expressao(self):

        localctx = LangGrammarParser.ExpressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expressao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.expressaoSimples()
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 46
                self.relacao()
                self.state = 47
                self.expressaoSimples()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variavel(self):
            return self.getTypedRuleContext(LangGrammarParser.VariavelContext,0)


        def numero(self):
            return self.getTypedRuleContext(LangGrammarParser.NumeroContext,0)


        def LP(self):
            return self.getToken(LangGrammarParser.LP, 0)

        def expressao(self):
            return self.getTypedRuleContext(LangGrammarParser.ExpressaoContext,0)


        def RP(self):
            return self.getToken(LangGrammarParser.RP, 0)

        def NOT(self):
            return self.getToken(LangGrammarParser.NOT, 0)

        def fator(self):
            return self.getTypedRuleContext(LangGrammarParser.FatorContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_fator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFator" ):
                listener.enterFator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFator" ):
                listener.exitFator(self)




    def fator(self):

        localctx = LangGrammarParser.FatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_fator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.state = 51
                self.variavel()
                pass
            elif token in [41, 42]:
                self.state = 52
                self.numero()
                pass
            elif token in [27]:
                self.state = 53
                self.match(LangGrammarParser.LP)
                self.state = 54
                self.expressao()
                self.state = 55
                self.match(LangGrammarParser.RP)
                pass
            elif token in [21]:
                self.state = 57
                self.match(LangGrammarParser.NOT)
                self.state = 58
                self.fator()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariavelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(LangGrammarParser.IDENTIFICADOR, 0)

        def expressao(self):
            return self.getTypedRuleContext(LangGrammarParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_variavel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariavel" ):
                listener.enterVariavel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariavel" ):
                listener.exitVariavel(self)




    def variavel(self):

        localctx = LangGrammarParser.VariavelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variavel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(LangGrammarParser.IDENTIFICADOR)
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 62
                self.expressao()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoVariavelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(LangGrammarParser.TipoContext,0)


        def listaIdentificadores(self):
            return self.getTypedRuleContext(LangGrammarParser.ListaIdentificadoresContext,0)


        def getRuleIndex(self):
            return LangGrammarParser.RULE_declaracaoVariavel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracaoVariavel" ):
                listener.enterDeclaracaoVariavel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracaoVariavel" ):
                listener.exitDeclaracaoVariavel(self)




    def declaracaoVariavel(self):

        localctx = LangGrammarParser.DeclaracaoVariavelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_declaracaoVariavel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.tipo()
            self.state = 66
            self.listaIdentificadores()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaIdentificadoresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self, i:int=None):
            if i is None:
                return self.getTokens(LangGrammarParser.IDENTIFICADOR)
            else:
                return self.getToken(LangGrammarParser.IDENTIFICADOR, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LangGrammarParser.COMMA)
            else:
                return self.getToken(LangGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return LangGrammarParser.RULE_listaIdentificadores

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaIdentificadores" ):
                listener.enterListaIdentificadores(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaIdentificadores" ):
                listener.exitListaIdentificadores(self)




    def listaIdentificadores(self):

        localctx = LangGrammarParser.ListaIdentificadoresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_listaIdentificadores)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(LangGrammarParser.IDENTIFICADOR)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 69
                self.match(LangGrammarParser.COMMA)
                self.state = 70
                self.match(LangGrammarParser.IDENTIFICADOR)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParteDeclaracaoVariavelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracaoVariavel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangGrammarParser.DeclaracaoVariavelContext)
            else:
                return self.getTypedRuleContext(LangGrammarParser.DeclaracaoVariavelContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(LangGrammarParser.SEMICOLON)
            else:
                return self.getToken(LangGrammarParser.SEMICOLON, i)

        def EOF(self):
            return self.getToken(LangGrammarParser.EOF, 0)

        def getRuleIndex(self):
            return LangGrammarParser.RULE_parteDeclaracaoVariavel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParteDeclaracaoVariavel" ):
                listener.enterParteDeclaracaoVariavel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParteDeclaracaoVariavel" ):
                listener.exitParteDeclaracaoVariavel(self)




    def parteDeclaracaoVariavel(self):

        localctx = LangGrammarParser.ParteDeclaracaoVariavelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parteDeclaracaoVariavel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.declaracaoVariavel()
            self.state = 81
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 77
                    self.match(LangGrammarParser.SEMICOLON)
                    self.state = 78
                    self.declaracaoVariavel() 
                self.state = 83
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 84
            self.match(LangGrammarParser.SEMICOLON)
            self.state = 85
            self.match(LangGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_BOOL(self):
            return self.getToken(LangGrammarParser.TYPE_BOOL, 0)

        def TYPE_INT(self):
            return self.getToken(LangGrammarParser.TYPE_INT, 0)

        def getRuleIndex(self):
            return LangGrammarParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = LangGrammarParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





