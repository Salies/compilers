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
        4,1,47,109,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,1,1,1,1,2,1,2,1,2,5,2,40,8,2,10,2,
        12,2,43,9,2,1,3,3,3,46,8,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,55,8,
        4,1,5,1,5,1,5,1,6,1,6,1,6,3,6,63,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,3,7,73,8,7,1,8,1,8,1,8,1,9,3,9,79,8,9,1,10,1,10,1,10,1,11,1,
        11,1,11,1,12,1,12,1,12,3,12,90,8,12,1,13,1,13,1,13,4,13,95,8,13,
        11,13,12,13,96,1,13,1,13,1,14,1,14,1,14,1,14,3,14,105,8,14,1,15,
        1,15,1,15,0,0,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,6,
        1,0,41,42,1,0,34,39,3,0,20,20,23,23,25,25,2,0,22,22,26,26,3,0,19,
        19,22,22,26,26,1,0,8,9,103,0,32,1,0,0,0,2,34,1,0,0,0,4,36,1,0,0,
        0,6,45,1,0,0,0,8,54,1,0,0,0,10,56,1,0,0,0,12,62,1,0,0,0,14,72,1,
        0,0,0,16,74,1,0,0,0,18,78,1,0,0,0,20,80,1,0,0,0,22,83,1,0,0,0,24,
        89,1,0,0,0,26,91,1,0,0,0,28,104,1,0,0,0,30,106,1,0,0,0,32,33,7,0,
        0,0,33,1,1,0,0,0,34,35,7,1,0,0,35,3,1,0,0,0,36,41,3,14,7,0,37,38,
        7,2,0,0,38,40,3,14,7,0,39,37,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,
        41,42,1,0,0,0,42,5,1,0,0,0,43,41,1,0,0,0,44,46,7,3,0,0,45,44,1,0,
        0,0,45,46,1,0,0,0,46,47,1,0,0,0,47,48,3,4,2,0,48,49,3,8,4,0,49,7,
        1,0,0,0,50,51,7,4,0,0,51,52,3,4,2,0,52,53,3,8,4,0,53,55,1,0,0,0,
        54,50,1,0,0,0,54,55,1,0,0,0,55,9,1,0,0,0,56,57,3,6,3,0,57,58,3,12,
        6,0,58,11,1,0,0,0,59,60,3,2,1,0,60,61,3,6,3,0,61,63,1,0,0,0,62,59,
        1,0,0,0,62,63,1,0,0,0,63,13,1,0,0,0,64,73,3,16,8,0,65,73,3,0,0,0,
        66,67,5,27,0,0,67,68,3,10,5,0,68,69,5,28,0,0,69,73,1,0,0,0,70,71,
        5,21,0,0,71,73,3,14,7,0,72,64,1,0,0,0,72,65,1,0,0,0,72,66,1,0,0,
        0,72,70,1,0,0,0,73,15,1,0,0,0,74,75,5,40,0,0,75,76,3,18,9,0,76,17,
        1,0,0,0,77,79,3,10,5,0,78,77,1,0,0,0,78,79,1,0,0,0,79,19,1,0,0,0,
        80,81,3,30,15,0,81,82,3,22,11,0,82,21,1,0,0,0,83,84,5,40,0,0,84,
        85,3,24,12,0,85,23,1,0,0,0,86,87,5,6,0,0,87,88,5,40,0,0,88,90,3,
        24,12,0,89,86,1,0,0,0,89,90,1,0,0,0,90,25,1,0,0,0,91,92,3,20,10,
        0,92,94,3,28,14,0,93,95,5,3,0,0,94,93,1,0,0,0,95,96,1,0,0,0,96,94,
        1,0,0,0,96,97,1,0,0,0,97,98,1,0,0,0,98,99,5,0,0,1,99,27,1,0,0,0,
        100,101,5,3,0,0,101,102,3,20,10,0,102,103,3,28,14,0,103,105,1,0,
        0,0,104,100,1,0,0,0,104,105,1,0,0,0,105,29,1,0,0,0,106,107,7,5,0,
        0,107,31,1,0,0,0,9,41,45,54,62,72,78,89,96,104
    ]

class LangGrammar ( Parser ):

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
    RULE_expressaoSimples1 = 4
    RULE_expressao = 5
    RULE_expressao1 = 6
    RULE_fator = 7
    RULE_variavel = 8
    RULE_variavel1 = 9
    RULE_declaracaoVariavel = 10
    RULE_listaIdentificadores = 11
    RULE_listaIdentificadores1 = 12
    RULE_parteDeclaracaoVariavel = 13
    RULE_parteDeclaracaoVariavel1 = 14
    RULE_tipo = 15

    ruleNames =  [ "numero", "relacao", "termo", "expressaoSimples", "expressaoSimples1", 
                   "expressao", "expressao1", "fator", "variavel", "variavel1", 
                   "declaracaoVariavel", "listaIdentificadores", "listaIdentificadores1", 
                   "parteDeclaracaoVariavel", "parteDeclaracaoVariavel1", 
                   "tipo" ]

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
            return self.getToken(LangGrammar.INT, 0)

        def REAL(self):
            return self.getToken(LangGrammar.REAL, 0)

        def getRuleIndex(self):
            return LangGrammar.RULE_numero

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)




    def numero(self):

        localctx = LangGrammar.NumeroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_numero)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
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
            return self.getToken(LangGrammar.EQUAL, 0)

        def DIFF(self):
            return self.getToken(LangGrammar.DIFF, 0)

        def LT(self):
            return self.getToken(LangGrammar.LT, 0)

        def LTE(self):
            return self.getToken(LangGrammar.LTE, 0)

        def GT(self):
            return self.getToken(LangGrammar.GT, 0)

        def GTE(self):
            return self.getToken(LangGrammar.GTE, 0)

        def getRuleIndex(self):
            return LangGrammar.RULE_relacao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelacao" ):
                listener.enterRelacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelacao" ):
                listener.exitRelacao(self)




    def relacao(self):

        localctx = LangGrammar.RelacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_relacao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
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
                return self.getTypedRuleContexts(LangGrammar.FatorContext)
            else:
                return self.getTypedRuleContext(LangGrammar.FatorContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(LangGrammar.MUL)
            else:
                return self.getToken(LangGrammar.MUL, i)

        def INT_DIV(self, i:int=None):
            if i is None:
                return self.getTokens(LangGrammar.INT_DIV)
            else:
                return self.getToken(LangGrammar.INT_DIV, i)

        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(LangGrammar.AND)
            else:
                return self.getToken(LangGrammar.AND, i)

        def getRuleIndex(self):
            return LangGrammar.RULE_termo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo" ):
                listener.enterTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo" ):
                listener.exitTermo(self)




    def termo(self):

        localctx = LangGrammar.TermoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_termo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.fator()
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 37
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 42991616) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 38
                    self.fator() 
                self.state = 43
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

        def termo(self):
            return self.getTypedRuleContext(LangGrammar.TermoContext,0)


        def expressaoSimples1(self):
            return self.getTypedRuleContext(LangGrammar.ExpressaoSimples1Context,0)


        def SUM(self):
            return self.getToken(LangGrammar.SUM, 0)

        def SUB(self):
            return self.getToken(LangGrammar.SUB, 0)

        def getRuleIndex(self):
            return LangGrammar.RULE_expressaoSimples

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressaoSimples" ):
                listener.enterExpressaoSimples(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressaoSimples" ):
                listener.exitExpressaoSimples(self)




    def expressaoSimples(self):

        localctx = LangGrammar.ExpressaoSimplesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expressaoSimples)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22 or _la==26:
                self.state = 44
                _la = self._input.LA(1)
                if not(_la==22 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 47
            self.termo()
            self.state = 48
            self.expressaoSimples1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoSimples1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo(self):
            return self.getTypedRuleContext(LangGrammar.TermoContext,0)


        def expressaoSimples1(self):
            return self.getTypedRuleContext(LangGrammar.ExpressaoSimples1Context,0)


        def SUM(self):
            return self.getToken(LangGrammar.SUM, 0)

        def SUB(self):
            return self.getToken(LangGrammar.SUB, 0)

        def OR(self):
            return self.getToken(LangGrammar.OR, 0)

        def getRuleIndex(self):
            return LangGrammar.RULE_expressaoSimples1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressaoSimples1" ):
                listener.enterExpressaoSimples1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressaoSimples1" ):
                listener.exitExpressaoSimples1(self)




    def expressaoSimples1(self):

        localctx = LangGrammar.ExpressaoSimples1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expressaoSimples1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 50
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 71827456) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 51
                self.termo()
                self.state = 52
                self.expressaoSimples1()


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

        def expressaoSimples(self):
            return self.getTypedRuleContext(LangGrammar.ExpressaoSimplesContext,0)


        def expressao1(self):
            return self.getTypedRuleContext(LangGrammar.Expressao1Context,0)


        def getRuleIndex(self):
            return LangGrammar.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)




    def expressao(self):

        localctx = LangGrammar.ExpressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expressao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.expressaoSimples()
            self.state = 57
            self.expressao1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expressao1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relacao(self):
            return self.getTypedRuleContext(LangGrammar.RelacaoContext,0)


        def expressaoSimples(self):
            return self.getTypedRuleContext(LangGrammar.ExpressaoSimplesContext,0)


        def getRuleIndex(self):
            return LangGrammar.RULE_expressao1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao1" ):
                listener.enterExpressao1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao1" ):
                listener.exitExpressao1(self)




    def expressao1(self):

        localctx = LangGrammar.Expressao1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expressao1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 59
                self.relacao()
                self.state = 60
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
            return self.getTypedRuleContext(LangGrammar.VariavelContext,0)


        def numero(self):
            return self.getTypedRuleContext(LangGrammar.NumeroContext,0)


        def LP(self):
            return self.getToken(LangGrammar.LP, 0)

        def expressao(self):
            return self.getTypedRuleContext(LangGrammar.ExpressaoContext,0)


        def RP(self):
            return self.getToken(LangGrammar.RP, 0)

        def NOT(self):
            return self.getToken(LangGrammar.NOT, 0)

        def fator(self):
            return self.getTypedRuleContext(LangGrammar.FatorContext,0)


        def getRuleIndex(self):
            return LangGrammar.RULE_fator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFator" ):
                listener.enterFator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFator" ):
                listener.exitFator(self)




    def fator(self):

        localctx = LangGrammar.FatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_fator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.state = 64
                self.variavel()
                pass
            elif token in [41, 42]:
                self.state = 65
                self.numero()
                pass
            elif token in [27]:
                self.state = 66
                self.match(LangGrammar.LP)
                self.state = 67
                self.expressao()
                self.state = 68
                self.match(LangGrammar.RP)
                pass
            elif token in [21]:
                self.state = 70
                self.match(LangGrammar.NOT)
                self.state = 71
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
            return self.getToken(LangGrammar.IDENTIFICADOR, 0)

        def variavel1(self):
            return self.getTypedRuleContext(LangGrammar.Variavel1Context,0)


        def getRuleIndex(self):
            return LangGrammar.RULE_variavel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariavel" ):
                listener.enterVariavel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariavel" ):
                listener.exitVariavel(self)




    def variavel(self):

        localctx = LangGrammar.VariavelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_variavel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(LangGrammar.IDENTIFICADOR)
            self.state = 75
            self.variavel1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variavel1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(LangGrammar.ExpressaoContext,0)


        def getRuleIndex(self):
            return LangGrammar.RULE_variavel1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariavel1" ):
                listener.enterVariavel1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariavel1" ):
                listener.exitVariavel1(self)




    def variavel1(self):

        localctx = LangGrammar.Variavel1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_variavel1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 77
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
            return self.getTypedRuleContext(LangGrammar.TipoContext,0)


        def listaIdentificadores(self):
            return self.getTypedRuleContext(LangGrammar.ListaIdentificadoresContext,0)


        def getRuleIndex(self):
            return LangGrammar.RULE_declaracaoVariavel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracaoVariavel" ):
                listener.enterDeclaracaoVariavel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracaoVariavel" ):
                listener.exitDeclaracaoVariavel(self)




    def declaracaoVariavel(self):

        localctx = LangGrammar.DeclaracaoVariavelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_declaracaoVariavel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.tipo()
            self.state = 81
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

        def IDENTIFICADOR(self):
            return self.getToken(LangGrammar.IDENTIFICADOR, 0)

        def listaIdentificadores1(self):
            return self.getTypedRuleContext(LangGrammar.ListaIdentificadores1Context,0)


        def getRuleIndex(self):
            return LangGrammar.RULE_listaIdentificadores

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaIdentificadores" ):
                listener.enterListaIdentificadores(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaIdentificadores" ):
                listener.exitListaIdentificadores(self)




    def listaIdentificadores(self):

        localctx = LangGrammar.ListaIdentificadoresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_listaIdentificadores)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(LangGrammar.IDENTIFICADOR)
            self.state = 84
            self.listaIdentificadores1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaIdentificadores1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(LangGrammar.COMMA, 0)

        def IDENTIFICADOR(self):
            return self.getToken(LangGrammar.IDENTIFICADOR, 0)

        def listaIdentificadores1(self):
            return self.getTypedRuleContext(LangGrammar.ListaIdentificadores1Context,0)


        def getRuleIndex(self):
            return LangGrammar.RULE_listaIdentificadores1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaIdentificadores1" ):
                listener.enterListaIdentificadores1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaIdentificadores1" ):
                listener.exitListaIdentificadores1(self)




    def listaIdentificadores1(self):

        localctx = LangGrammar.ListaIdentificadores1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_listaIdentificadores1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 86
                self.match(LangGrammar.COMMA)
                self.state = 87
                self.match(LangGrammar.IDENTIFICADOR)
                self.state = 88
                self.listaIdentificadores1()


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

        def declaracaoVariavel(self):
            return self.getTypedRuleContext(LangGrammar.DeclaracaoVariavelContext,0)


        def parteDeclaracaoVariavel1(self):
            return self.getTypedRuleContext(LangGrammar.ParteDeclaracaoVariavel1Context,0)


        def EOF(self):
            return self.getToken(LangGrammar.EOF, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(LangGrammar.SEMICOLON)
            else:
                return self.getToken(LangGrammar.SEMICOLON, i)

        def getRuleIndex(self):
            return LangGrammar.RULE_parteDeclaracaoVariavel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParteDeclaracaoVariavel" ):
                listener.enterParteDeclaracaoVariavel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParteDeclaracaoVariavel" ):
                listener.exitParteDeclaracaoVariavel(self)




    def parteDeclaracaoVariavel(self):

        localctx = LangGrammar.ParteDeclaracaoVariavelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parteDeclaracaoVariavel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.declaracaoVariavel()
            self.state = 92
            self.parteDeclaracaoVariavel1()
            self.state = 94 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 93
                self.match(LangGrammar.SEMICOLON)
                self.state = 96 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
                    break

            self.state = 98
            self.match(LangGrammar.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParteDeclaracaoVariavel1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(LangGrammar.SEMICOLON, 0)

        def declaracaoVariavel(self):
            return self.getTypedRuleContext(LangGrammar.DeclaracaoVariavelContext,0)


        def parteDeclaracaoVariavel1(self):
            return self.getTypedRuleContext(LangGrammar.ParteDeclaracaoVariavel1Context,0)


        def getRuleIndex(self):
            return LangGrammar.RULE_parteDeclaracaoVariavel1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParteDeclaracaoVariavel1" ):
                listener.enterParteDeclaracaoVariavel1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParteDeclaracaoVariavel1" ):
                listener.exitParteDeclaracaoVariavel1(self)




    def parteDeclaracaoVariavel1(self):

        localctx = LangGrammar.ParteDeclaracaoVariavel1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_parteDeclaracaoVariavel1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 100
                self.match(LangGrammar.SEMICOLON)
                self.state = 101
                self.declaracaoVariavel()
                self.state = 102
                self.parteDeclaracaoVariavel1()


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
            return self.getToken(LangGrammar.TYPE_BOOL, 0)

        def TYPE_INT(self):
            return self.getToken(LangGrammar.TYPE_INT, 0)

        def getRuleIndex(self):
            return LangGrammar.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = LangGrammar.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
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





