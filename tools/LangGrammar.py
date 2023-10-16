# Generated from ./tools/LangGrammar.g4 by ANTLR 4.13.0
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
        4,1,47,263,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,1,0,1,1,1,1,1,2,1,2,1,2,5,
        2,82,8,2,10,2,12,2,85,9,2,1,3,3,3,88,8,3,1,3,1,3,1,3,1,4,1,4,1,4,
        1,4,3,4,97,8,4,1,5,1,5,1,5,1,6,1,6,1,6,3,6,105,8,6,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,117,8,7,1,8,1,8,1,8,1,9,3,9,123,8,
        9,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,3,12,134,8,12,1,13,
        1,13,1,13,1,13,1,14,1,14,1,14,1,14,3,14,144,8,14,1,15,1,15,1,16,
        1,16,1,16,1,16,1,16,4,16,153,8,16,11,16,12,16,154,1,16,1,16,1,17,
        3,17,160,8,17,1,17,3,17,163,8,17,1,17,1,17,1,18,1,18,1,18,1,18,1,
        19,1,19,1,19,1,19,3,19,175,8,19,1,20,1,20,1,20,1,20,1,20,1,20,1,
        21,3,21,184,8,21,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,3,
        23,195,8,23,1,24,3,24,198,8,24,1,24,1,24,1,24,1,24,1,25,1,25,3,25,
        206,8,25,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,3,27,217,8,
        27,1,28,1,28,1,28,1,28,1,28,3,28,224,8,28,1,29,1,29,1,29,1,29,1,
        30,1,30,1,30,1,31,1,31,1,31,1,31,3,31,237,8,31,1,32,1,32,1,32,1,
        32,1,32,1,32,1,33,1,33,3,33,247,8,33,1,34,1,34,1,34,1,34,1,34,1,
        35,1,35,1,35,1,36,1,36,1,36,1,36,3,36,261,8,36,1,36,0,0,37,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,62,64,66,68,70,72,0,7,1,0,41,42,1,0,34,39,3,0,
        20,20,23,23,25,25,2,0,22,22,26,26,3,0,19,19,22,22,26,26,1,0,8,9,
        2,0,10,11,40,40,253,0,74,1,0,0,0,2,76,1,0,0,0,4,78,1,0,0,0,6,87,
        1,0,0,0,8,96,1,0,0,0,10,98,1,0,0,0,12,104,1,0,0,0,14,116,1,0,0,0,
        16,118,1,0,0,0,18,122,1,0,0,0,20,124,1,0,0,0,22,127,1,0,0,0,24,133,
        1,0,0,0,26,135,1,0,0,0,28,143,1,0,0,0,30,145,1,0,0,0,32,147,1,0,
        0,0,34,159,1,0,0,0,36,166,1,0,0,0,38,174,1,0,0,0,40,176,1,0,0,0,
        42,183,1,0,0,0,44,185,1,0,0,0,46,194,1,0,0,0,48,197,1,0,0,0,50,205,
        1,0,0,0,52,207,1,0,0,0,54,216,1,0,0,0,56,223,1,0,0,0,58,225,1,0,
        0,0,60,229,1,0,0,0,62,236,1,0,0,0,64,238,1,0,0,0,66,246,1,0,0,0,
        68,248,1,0,0,0,70,253,1,0,0,0,72,260,1,0,0,0,74,75,7,0,0,0,75,1,
        1,0,0,0,76,77,7,1,0,0,77,3,1,0,0,0,78,83,3,14,7,0,79,80,7,2,0,0,
        80,82,3,14,7,0,81,79,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,
        0,0,0,84,5,1,0,0,0,85,83,1,0,0,0,86,88,7,3,0,0,87,86,1,0,0,0,87,
        88,1,0,0,0,88,89,1,0,0,0,89,90,3,4,2,0,90,91,3,8,4,0,91,7,1,0,0,
        0,92,93,7,4,0,0,93,94,3,4,2,0,94,95,3,8,4,0,95,97,1,0,0,0,96,92,
        1,0,0,0,96,97,1,0,0,0,97,9,1,0,0,0,98,99,3,6,3,0,99,100,3,12,6,0,
        100,11,1,0,0,0,101,102,3,2,1,0,102,103,3,6,3,0,103,105,1,0,0,0,104,
        101,1,0,0,0,104,105,1,0,0,0,105,13,1,0,0,0,106,117,3,16,8,0,107,
        117,3,0,0,0,108,109,5,27,0,0,109,110,3,10,5,0,110,111,5,28,0,0,111,
        117,1,0,0,0,112,113,5,21,0,0,113,117,3,14,7,0,114,117,5,12,0,0,115,
        117,5,13,0,0,116,106,1,0,0,0,116,107,1,0,0,0,116,108,1,0,0,0,116,
        112,1,0,0,0,116,114,1,0,0,0,116,115,1,0,0,0,117,15,1,0,0,0,118,119,
        5,40,0,0,119,120,3,18,9,0,120,17,1,0,0,0,121,123,3,10,5,0,122,121,
        1,0,0,0,122,123,1,0,0,0,123,19,1,0,0,0,124,125,3,30,15,0,125,126,
        3,22,11,0,126,21,1,0,0,0,127,128,5,40,0,0,128,129,3,24,12,0,129,
        23,1,0,0,0,130,131,5,6,0,0,131,132,5,40,0,0,132,134,3,24,12,0,133,
        130,1,0,0,0,133,134,1,0,0,0,134,25,1,0,0,0,135,136,3,20,10,0,136,
        137,3,28,14,0,137,138,5,3,0,0,138,27,1,0,0,0,139,140,5,3,0,0,140,
        141,3,20,10,0,141,142,3,28,14,0,142,144,1,0,0,0,143,139,1,0,0,0,
        143,144,1,0,0,0,144,29,1,0,0,0,145,146,7,5,0,0,146,31,1,0,0,0,147,
        148,5,1,0,0,148,149,5,40,0,0,149,150,5,3,0,0,150,152,3,34,17,0,151,
        153,5,33,0,0,152,151,1,0,0,0,153,154,1,0,0,0,154,152,1,0,0,0,154,
        155,1,0,0,0,155,156,1,0,0,0,156,157,5,0,0,1,157,33,1,0,0,0,158,160,
        3,26,13,0,159,158,1,0,0,0,159,160,1,0,0,0,160,162,1,0,0,0,161,163,
        3,36,18,0,162,161,1,0,0,0,162,163,1,0,0,0,163,164,1,0,0,0,164,165,
        3,52,26,0,165,35,1,0,0,0,166,167,3,40,20,0,167,168,3,38,19,0,168,
        169,5,3,0,0,169,37,1,0,0,0,170,171,5,3,0,0,171,172,3,40,20,0,172,
        173,3,38,19,0,173,175,1,0,0,0,174,170,1,0,0,0,174,175,1,0,0,0,175,
        39,1,0,0,0,176,177,5,2,0,0,177,178,5,40,0,0,178,179,3,42,21,0,179,
        180,5,3,0,0,180,181,3,34,17,0,181,41,1,0,0,0,182,184,3,44,22,0,183,
        182,1,0,0,0,183,184,1,0,0,0,184,43,1,0,0,0,185,186,5,27,0,0,186,
        187,3,48,24,0,187,188,3,46,23,0,188,189,5,28,0,0,189,45,1,0,0,0,
        190,191,5,3,0,0,191,192,3,48,24,0,192,193,3,46,23,0,193,195,1,0,
        0,0,194,190,1,0,0,0,194,195,1,0,0,0,195,47,1,0,0,0,196,198,5,7,0,
        0,197,196,1,0,0,0,197,198,1,0,0,0,198,199,1,0,0,0,199,200,3,22,11,
        0,200,201,5,5,0,0,201,202,3,50,25,0,202,49,1,0,0,0,203,206,5,40,
        0,0,204,206,3,30,15,0,205,203,1,0,0,0,205,204,1,0,0,0,206,51,1,0,
        0,0,207,208,5,14,0,0,208,209,3,56,28,0,209,210,3,54,27,0,210,211,
        5,15,0,0,211,53,1,0,0,0,212,213,5,3,0,0,213,214,3,56,28,0,214,215,
        3,54,27,0,215,217,1,0,0,0,216,212,1,0,0,0,216,217,1,0,0,0,217,55,
        1,0,0,0,218,224,3,58,29,0,219,224,3,60,30,0,220,224,3,52,26,0,221,
        224,3,64,32,0,222,224,3,68,34,0,223,218,1,0,0,0,223,219,1,0,0,0,
        223,220,1,0,0,0,223,221,1,0,0,0,223,222,1,0,0,0,224,57,1,0,0,0,225,
        226,3,16,8,0,226,227,5,4,0,0,227,228,3,10,5,0,228,59,1,0,0,0,229,
        230,7,6,0,0,230,231,3,62,31,0,231,61,1,0,0,0,232,233,5,27,0,0,233,
        234,3,70,35,0,234,235,5,28,0,0,235,237,1,0,0,0,236,232,1,0,0,0,236,
        237,1,0,0,0,237,63,1,0,0,0,238,239,5,16,0,0,239,240,3,10,5,0,240,
        241,5,17,0,0,241,242,3,56,28,0,242,243,3,66,33,0,243,65,1,0,0,0,
        244,245,5,18,0,0,245,247,3,56,28,0,246,244,1,0,0,0,246,247,1,0,0,
        0,247,67,1,0,0,0,248,249,5,31,0,0,249,250,3,10,5,0,250,251,5,32,
        0,0,251,252,3,56,28,0,252,69,1,0,0,0,253,254,3,10,5,0,254,255,3,
        72,36,0,255,71,1,0,0,0,256,257,5,6,0,0,257,258,3,10,5,0,258,259,
        3,72,36,0,259,261,1,0,0,0,260,256,1,0,0,0,260,261,1,0,0,0,261,73,
        1,0,0,0,21,83,87,96,104,116,122,133,143,154,159,162,174,183,194,
        197,205,216,223,236,246,260
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
    RULE_programa = 16
    RULE_bloco = 17
    RULE_parteDeclaracaoSubRotina = 18
    RULE_parteDeclaracaoSubRotina1 = 19
    RULE_declaracaoProcedimento = 20
    RULE_declaracaoProcedimento1 = 21
    RULE_parametrosFormais = 22
    RULE_parametrosFormais1 = 23
    RULE_secaoParametrosFormais = 24
    RULE_secaoParametrosFormais1 = 25
    RULE_comandoComposto = 26
    RULE_comandoComposto1 = 27
    RULE_comando = 28
    RULE_atribuicao = 29
    RULE_chamadaProcedimento = 30
    RULE_chamadaProcedimento1 = 31
    RULE_comandoCondicional = 32
    RULE_comandoCondicional1 = 33
    RULE_comandoRepetitivo1 = 34
    RULE_listaExpressao = 35
    RULE_listaExpressao1 = 36

    ruleNames =  [ "numero", "relacao", "termo", "expressaoSimples", "expressaoSimples1", 
                   "expressao", "expressao1", "fator", "variavel", "variavel1", 
                   "declaracaoVariavel", "listaIdentificadores", "listaIdentificadores1", 
                   "parteDeclaracaoVariavel", "parteDeclaracaoVariavel1", 
                   "tipo", "programa", "bloco", "parteDeclaracaoSubRotina", 
                   "parteDeclaracaoSubRotina1", "declaracaoProcedimento", 
                   "declaracaoProcedimento1", "parametrosFormais", "parametrosFormais1", 
                   "secaoParametrosFormais", "secaoParametrosFormais1", 
                   "comandoComposto", "comandoComposto1", "comando", "atribuicao", 
                   "chamadaProcedimento", "chamadaProcedimento1", "comandoCondicional", 
                   "comandoCondicional1", "comandoRepetitivo1", "listaExpressao", 
                   "listaExpressao1" ]

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
        self.checkVersion("4.13.0")
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
            self.state = 74
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
            self.state = 76
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
            self.state = 78
            self.fator()
            self.state = 83
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 79
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 42991616) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 80
                    self.fator() 
                self.state = 85
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
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22 or _la==26:
                self.state = 86
                _la = self._input.LA(1)
                if not(_la==22 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 89
            self.termo()
            self.state = 90
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
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 92
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 71827456) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 93
                self.termo()
                self.state = 94
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
            self.state = 98
            self.expressaoSimples()
            self.state = 99
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
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 101
                self.relacao()
                self.state = 102
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


        def CONST_TRUE(self):
            return self.getToken(LangGrammar.CONST_TRUE, 0)

        def CONST_FALSE(self):
            return self.getToken(LangGrammar.CONST_FALSE, 0)

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
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.state = 106
                self.variavel()
                pass
            elif token in [41, 42]:
                self.state = 107
                self.numero()
                pass
            elif token in [27]:
                self.state = 108
                self.match(LangGrammar.LP)
                self.state = 109
                self.expressao()
                self.state = 110
                self.match(LangGrammar.RP)
                pass
            elif token in [21]:
                self.state = 112
                self.match(LangGrammar.NOT)
                self.state = 113
                self.fator()
                pass
            elif token in [12]:
                self.state = 114
                self.match(LangGrammar.CONST_TRUE)
                pass
            elif token in [13]:
                self.state = 115
                self.match(LangGrammar.CONST_FALSE)
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
            self.state = 118
            self.match(LangGrammar.IDENTIFICADOR)
            self.state = 119
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
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 121
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
            self.state = 124
            self.tipo()
            self.state = 125
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
            self.state = 127
            self.match(LangGrammar.IDENTIFICADOR)
            self.state = 128
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
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 130
                self.match(LangGrammar.COMMA)
                self.state = 131
                self.match(LangGrammar.IDENTIFICADOR)
                self.state = 132
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


        def SEMICOLON(self):
            return self.getToken(LangGrammar.SEMICOLON, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.declaracaoVariavel()
            self.state = 136
            self.parteDeclaracaoVariavel1()
            self.state = 137
            self.match(LangGrammar.SEMICOLON)
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
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 139
                self.match(LangGrammar.SEMICOLON)
                self.state = 140
                self.declaracaoVariavel()
                self.state = 141
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
            self.state = 145
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


    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(LangGrammar.PROGRAM, 0)

        def IDENTIFICADOR(self):
            return self.getToken(LangGrammar.IDENTIFICADOR, 0)

        def SEMICOLON(self):
            return self.getToken(LangGrammar.SEMICOLON, 0)

        def bloco(self):
            return self.getTypedRuleContext(LangGrammar.BlocoContext,0)


        def EOF(self):
            return self.getToken(LangGrammar.EOF, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(LangGrammar.DOT)
            else:
                return self.getToken(LangGrammar.DOT, i)

        def getRuleIndex(self):
            return LangGrammar.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = LangGrammar.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(LangGrammar.PROGRAM)
            self.state = 148
            self.match(LangGrammar.IDENTIFICADOR)
            self.state = 149
            self.match(LangGrammar.SEMICOLON)
            self.state = 150
            self.bloco()
            self.state = 152 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 151
                self.match(LangGrammar.DOT)
                self.state = 154 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==33):
                    break

            self.state = 156
            self.match(LangGrammar.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comandoComposto(self):
            return self.getTypedRuleContext(LangGrammar.ComandoCompostoContext,0)


        def parteDeclaracaoVariavel(self):
            return self.getTypedRuleContext(LangGrammar.ParteDeclaracaoVariavelContext,0)


        def parteDeclaracaoSubRotina(self):
            return self.getTypedRuleContext(LangGrammar.ParteDeclaracaoSubRotinaContext,0)


        def getRuleIndex(self):
            return LangGrammar.RULE_bloco

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloco" ):
                listener.enterBloco(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloco" ):
                listener.exitBloco(self)




    def bloco(self):

        localctx = LangGrammar.BlocoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_bloco)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8 or _la==9:
                self.state = 158
                self.parteDeclaracaoVariavel()


            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 161
                self.parteDeclaracaoSubRotina()


            self.state = 164
            self.comandoComposto()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParteDeclaracaoSubRotinaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracaoProcedimento(self):
            return self.getTypedRuleContext(LangGrammar.DeclaracaoProcedimentoContext,0)


        def parteDeclaracaoSubRotina1(self):
            return self.getTypedRuleContext(LangGrammar.ParteDeclaracaoSubRotina1Context,0)


        def SEMICOLON(self):
            return self.getToken(LangGrammar.SEMICOLON, 0)

        def getRuleIndex(self):
            return LangGrammar.RULE_parteDeclaracaoSubRotina

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParteDeclaracaoSubRotina" ):
                listener.enterParteDeclaracaoSubRotina(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParteDeclaracaoSubRotina" ):
                listener.exitParteDeclaracaoSubRotina(self)




    def parteDeclaracaoSubRotina(self):

        localctx = LangGrammar.ParteDeclaracaoSubRotinaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_parteDeclaracaoSubRotina)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.declaracaoProcedimento()
            self.state = 167
            self.parteDeclaracaoSubRotina1()
            self.state = 168
            self.match(LangGrammar.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParteDeclaracaoSubRotina1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(LangGrammar.SEMICOLON, 0)

        def declaracaoProcedimento(self):
            return self.getTypedRuleContext(LangGrammar.DeclaracaoProcedimentoContext,0)


        def parteDeclaracaoSubRotina1(self):
            return self.getTypedRuleContext(LangGrammar.ParteDeclaracaoSubRotina1Context,0)


        def getRuleIndex(self):
            return LangGrammar.RULE_parteDeclaracaoSubRotina1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParteDeclaracaoSubRotina1" ):
                listener.enterParteDeclaracaoSubRotina1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParteDeclaracaoSubRotina1" ):
                listener.exitParteDeclaracaoSubRotina1(self)




    def parteDeclaracaoSubRotina1(self):

        localctx = LangGrammar.ParteDeclaracaoSubRotina1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_parteDeclaracaoSubRotina1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 170
                self.match(LangGrammar.SEMICOLON)
                self.state = 171
                self.declaracaoProcedimento()
                self.state = 172
                self.parteDeclaracaoSubRotina1()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoProcedimentoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROCEDURE(self):
            return self.getToken(LangGrammar.PROCEDURE, 0)

        def IDENTIFICADOR(self):
            return self.getToken(LangGrammar.IDENTIFICADOR, 0)

        def declaracaoProcedimento1(self):
            return self.getTypedRuleContext(LangGrammar.DeclaracaoProcedimento1Context,0)


        def SEMICOLON(self):
            return self.getToken(LangGrammar.SEMICOLON, 0)

        def bloco(self):
            return self.getTypedRuleContext(LangGrammar.BlocoContext,0)


        def getRuleIndex(self):
            return LangGrammar.RULE_declaracaoProcedimento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracaoProcedimento" ):
                listener.enterDeclaracaoProcedimento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracaoProcedimento" ):
                listener.exitDeclaracaoProcedimento(self)




    def declaracaoProcedimento(self):

        localctx = LangGrammar.DeclaracaoProcedimentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_declaracaoProcedimento)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(LangGrammar.PROCEDURE)
            self.state = 177
            self.match(LangGrammar.IDENTIFICADOR)
            self.state = 178
            self.declaracaoProcedimento1()
            self.state = 179
            self.match(LangGrammar.SEMICOLON)
            self.state = 180
            self.bloco()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoProcedimento1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametrosFormais(self):
            return self.getTypedRuleContext(LangGrammar.ParametrosFormaisContext,0)


        def getRuleIndex(self):
            return LangGrammar.RULE_declaracaoProcedimento1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracaoProcedimento1" ):
                listener.enterDeclaracaoProcedimento1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracaoProcedimento1" ):
                listener.exitDeclaracaoProcedimento1(self)




    def declaracaoProcedimento1(self):

        localctx = LangGrammar.DeclaracaoProcedimento1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_declaracaoProcedimento1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 182
                self.parametrosFormais()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosFormaisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(LangGrammar.LP, 0)

        def secaoParametrosFormais(self):
            return self.getTypedRuleContext(LangGrammar.SecaoParametrosFormaisContext,0)


        def parametrosFormais1(self):
            return self.getTypedRuleContext(LangGrammar.ParametrosFormais1Context,0)


        def RP(self):
            return self.getToken(LangGrammar.RP, 0)

        def getRuleIndex(self):
            return LangGrammar.RULE_parametrosFormais

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametrosFormais" ):
                listener.enterParametrosFormais(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametrosFormais" ):
                listener.exitParametrosFormais(self)




    def parametrosFormais(self):

        localctx = LangGrammar.ParametrosFormaisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_parametrosFormais)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(LangGrammar.LP)
            self.state = 186
            self.secaoParametrosFormais()
            self.state = 187
            self.parametrosFormais1()
            self.state = 188
            self.match(LangGrammar.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosFormais1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(LangGrammar.SEMICOLON, 0)

        def secaoParametrosFormais(self):
            return self.getTypedRuleContext(LangGrammar.SecaoParametrosFormaisContext,0)


        def parametrosFormais1(self):
            return self.getTypedRuleContext(LangGrammar.ParametrosFormais1Context,0)


        def getRuleIndex(self):
            return LangGrammar.RULE_parametrosFormais1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametrosFormais1" ):
                listener.enterParametrosFormais1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametrosFormais1" ):
                listener.exitParametrosFormais1(self)




    def parametrosFormais1(self):

        localctx = LangGrammar.ParametrosFormais1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_parametrosFormais1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 190
                self.match(LangGrammar.SEMICOLON)
                self.state = 191
                self.secaoParametrosFormais()
                self.state = 192
                self.parametrosFormais1()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SecaoParametrosFormaisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listaIdentificadores(self):
            return self.getTypedRuleContext(LangGrammar.ListaIdentificadoresContext,0)


        def COLON(self):
            return self.getToken(LangGrammar.COLON, 0)

        def secaoParametrosFormais1(self):
            return self.getTypedRuleContext(LangGrammar.SecaoParametrosFormais1Context,0)


        def VAR(self):
            return self.getToken(LangGrammar.VAR, 0)

        def getRuleIndex(self):
            return LangGrammar.RULE_secaoParametrosFormais

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSecaoParametrosFormais" ):
                listener.enterSecaoParametrosFormais(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSecaoParametrosFormais" ):
                listener.exitSecaoParametrosFormais(self)




    def secaoParametrosFormais(self):

        localctx = LangGrammar.SecaoParametrosFormaisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_secaoParametrosFormais)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 196
                self.match(LangGrammar.VAR)


            self.state = 199
            self.listaIdentificadores()
            self.state = 200
            self.match(LangGrammar.COLON)
            self.state = 201
            self.secaoParametrosFormais1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SecaoParametrosFormais1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(LangGrammar.IDENTIFICADOR, 0)

        def tipo(self):
            return self.getTypedRuleContext(LangGrammar.TipoContext,0)


        def getRuleIndex(self):
            return LangGrammar.RULE_secaoParametrosFormais1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSecaoParametrosFormais1" ):
                listener.enterSecaoParametrosFormais1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSecaoParametrosFormais1" ):
                listener.exitSecaoParametrosFormais1(self)




    def secaoParametrosFormais1(self):

        localctx = LangGrammar.SecaoParametrosFormais1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_secaoParametrosFormais1)
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.match(LangGrammar.IDENTIFICADOR)
                pass
            elif token in [8, 9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.tipo()
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


    class ComandoCompostoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(LangGrammar.BEGIN, 0)

        def comando(self):
            return self.getTypedRuleContext(LangGrammar.ComandoContext,0)


        def comandoComposto1(self):
            return self.getTypedRuleContext(LangGrammar.ComandoComposto1Context,0)


        def END(self):
            return self.getToken(LangGrammar.END, 0)

        def getRuleIndex(self):
            return LangGrammar.RULE_comandoComposto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoComposto" ):
                listener.enterComandoComposto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoComposto" ):
                listener.exitComandoComposto(self)




    def comandoComposto(self):

        localctx = LangGrammar.ComandoCompostoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_comandoComposto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(LangGrammar.BEGIN)
            self.state = 208
            self.comando()
            self.state = 209
            self.comandoComposto1()
            self.state = 210
            self.match(LangGrammar.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoComposto1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(LangGrammar.SEMICOLON, 0)

        def comando(self):
            return self.getTypedRuleContext(LangGrammar.ComandoContext,0)


        def comandoComposto1(self):
            return self.getTypedRuleContext(LangGrammar.ComandoComposto1Context,0)


        def getRuleIndex(self):
            return LangGrammar.RULE_comandoComposto1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoComposto1" ):
                listener.enterComandoComposto1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoComposto1" ):
                listener.exitComandoComposto1(self)




    def comandoComposto1(self):

        localctx = LangGrammar.ComandoComposto1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_comandoComposto1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 212
                self.match(LangGrammar.SEMICOLON)
                self.state = 213
                self.comando()
                self.state = 214
                self.comandoComposto1()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atribuicao(self):
            return self.getTypedRuleContext(LangGrammar.AtribuicaoContext,0)


        def chamadaProcedimento(self):
            return self.getTypedRuleContext(LangGrammar.ChamadaProcedimentoContext,0)


        def comandoComposto(self):
            return self.getTypedRuleContext(LangGrammar.ComandoCompostoContext,0)


        def comandoCondicional(self):
            return self.getTypedRuleContext(LangGrammar.ComandoCondicionalContext,0)


        def comandoRepetitivo1(self):
            return self.getTypedRuleContext(LangGrammar.ComandoRepetitivo1Context,0)


        def getRuleIndex(self):
            return LangGrammar.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)




    def comando(self):

        localctx = LangGrammar.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_comando)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 218
                self.atribuicao()
                pass

            elif la_ == 2:
                self.state = 219
                self.chamadaProcedimento()
                pass

            elif la_ == 3:
                self.state = 220
                self.comandoComposto()
                pass

            elif la_ == 4:
                self.state = 221
                self.comandoCondicional()
                pass

            elif la_ == 5:
                self.state = 222
                self.comandoRepetitivo1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variavel(self):
            return self.getTypedRuleContext(LangGrammar.VariavelContext,0)


        def ATTRIB(self):
            return self.getToken(LangGrammar.ATTRIB, 0)

        def expressao(self):
            return self.getTypedRuleContext(LangGrammar.ExpressaoContext,0)


        def getRuleIndex(self):
            return LangGrammar.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)




    def atribuicao(self):

        localctx = LangGrammar.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.variavel()
            self.state = 226
            self.match(LangGrammar.ATTRIB)
            self.state = 227
            self.expressao()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChamadaProcedimentoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def chamadaProcedimento1(self):
            return self.getTypedRuleContext(LangGrammar.ChamadaProcedimento1Context,0)


        def IDENTIFICADOR(self):
            return self.getToken(LangGrammar.IDENTIFICADOR, 0)

        def PROC_READ(self):
            return self.getToken(LangGrammar.PROC_READ, 0)

        def PROC_WRITE(self):
            return self.getToken(LangGrammar.PROC_WRITE, 0)

        def getRuleIndex(self):
            return LangGrammar.RULE_chamadaProcedimento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChamadaProcedimento" ):
                listener.enterChamadaProcedimento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChamadaProcedimento" ):
                listener.exitChamadaProcedimento(self)




    def chamadaProcedimento(self):

        localctx = LangGrammar.ChamadaProcedimentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_chamadaProcedimento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1099511630848) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 230
            self.chamadaProcedimento1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChamadaProcedimento1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(LangGrammar.LP, 0)

        def listaExpressao(self):
            return self.getTypedRuleContext(LangGrammar.ListaExpressaoContext,0)


        def RP(self):
            return self.getToken(LangGrammar.RP, 0)

        def getRuleIndex(self):
            return LangGrammar.RULE_chamadaProcedimento1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChamadaProcedimento1" ):
                listener.enterChamadaProcedimento1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChamadaProcedimento1" ):
                listener.exitChamadaProcedimento1(self)




    def chamadaProcedimento1(self):

        localctx = LangGrammar.ChamadaProcedimento1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_chamadaProcedimento1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 232
                self.match(LangGrammar.LP)
                self.state = 233
                self.listaExpressao()
                self.state = 234
                self.match(LangGrammar.RP)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoCondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(LangGrammar.IF, 0)

        def expressao(self):
            return self.getTypedRuleContext(LangGrammar.ExpressaoContext,0)


        def THEN(self):
            return self.getToken(LangGrammar.THEN, 0)

        def comando(self):
            return self.getTypedRuleContext(LangGrammar.ComandoContext,0)


        def comandoCondicional1(self):
            return self.getTypedRuleContext(LangGrammar.ComandoCondicional1Context,0)


        def getRuleIndex(self):
            return LangGrammar.RULE_comandoCondicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoCondicional" ):
                listener.enterComandoCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoCondicional" ):
                listener.exitComandoCondicional(self)




    def comandoCondicional(self):

        localctx = LangGrammar.ComandoCondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_comandoCondicional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(LangGrammar.IF)
            self.state = 239
            self.expressao()
            self.state = 240
            self.match(LangGrammar.THEN)
            self.state = 241
            self.comando()
            self.state = 242
            self.comandoCondicional1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoCondicional1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(LangGrammar.ELSE, 0)

        def comando(self):
            return self.getTypedRuleContext(LangGrammar.ComandoContext,0)


        def getRuleIndex(self):
            return LangGrammar.RULE_comandoCondicional1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoCondicional1" ):
                listener.enterComandoCondicional1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoCondicional1" ):
                listener.exitComandoCondicional1(self)




    def comandoCondicional1(self):

        localctx = LangGrammar.ComandoCondicional1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_comandoCondicional1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 244
                self.match(LangGrammar.ELSE)
                self.state = 245
                self.comando()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoRepetitivo1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(LangGrammar.WHILE, 0)

        def expressao(self):
            return self.getTypedRuleContext(LangGrammar.ExpressaoContext,0)


        def DO(self):
            return self.getToken(LangGrammar.DO, 0)

        def comando(self):
            return self.getTypedRuleContext(LangGrammar.ComandoContext,0)


        def getRuleIndex(self):
            return LangGrammar.RULE_comandoRepetitivo1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoRepetitivo1" ):
                listener.enterComandoRepetitivo1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoRepetitivo1" ):
                listener.exitComandoRepetitivo1(self)




    def comandoRepetitivo1(self):

        localctx = LangGrammar.ComandoRepetitivo1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_comandoRepetitivo1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(LangGrammar.WHILE)
            self.state = 249
            self.expressao()
            self.state = 250
            self.match(LangGrammar.DO)
            self.state = 251
            self.comando()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(LangGrammar.ExpressaoContext,0)


        def listaExpressao1(self):
            return self.getTypedRuleContext(LangGrammar.ListaExpressao1Context,0)


        def getRuleIndex(self):
            return LangGrammar.RULE_listaExpressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaExpressao" ):
                listener.enterListaExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaExpressao" ):
                listener.exitListaExpressao(self)




    def listaExpressao(self):

        localctx = LangGrammar.ListaExpressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_listaExpressao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.expressao()
            self.state = 254
            self.listaExpressao1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaExpressao1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(LangGrammar.COMMA, 0)

        def expressao(self):
            return self.getTypedRuleContext(LangGrammar.ExpressaoContext,0)


        def listaExpressao1(self):
            return self.getTypedRuleContext(LangGrammar.ListaExpressao1Context,0)


        def getRuleIndex(self):
            return LangGrammar.RULE_listaExpressao1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaExpressao1" ):
                listener.enterListaExpressao1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaExpressao1" ):
                listener.exitListaExpressao1(self)




    def listaExpressao1(self):

        localctx = LangGrammar.ListaExpressao1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_listaExpressao1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 256
                self.match(LangGrammar.COMMA)
                self.state = 257
                self.expressao()
                self.state = 258
                self.listaExpressao1()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





