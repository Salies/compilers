# Generated from LangLexer.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,11,65,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,4,0,25,8,0,11,0,12,0,
        26,1,1,4,1,30,8,1,11,1,12,1,31,1,1,1,1,4,1,36,8,1,11,1,12,1,37,1,
        2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,4,8,53,8,8,11,
        8,12,8,54,1,8,1,8,1,9,4,9,60,8,9,11,9,12,9,61,1,10,1,10,1,61,0,11,
        1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,1,0,2,1,0,48,
        57,3,0,9,10,12,13,32,32,69,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,
        7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,
        1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,1,24,1,0,0,0,3,29,1,0,0,0,5,39,
        1,0,0,0,7,41,1,0,0,0,9,43,1,0,0,0,11,45,1,0,0,0,13,47,1,0,0,0,15,
        49,1,0,0,0,17,52,1,0,0,0,19,59,1,0,0,0,21,63,1,0,0,0,23,25,7,0,0,
        0,24,23,1,0,0,0,25,26,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,2,1,
        0,0,0,28,30,7,0,0,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,
        32,1,0,0,0,32,33,1,0,0,0,33,35,5,46,0,0,34,36,7,0,0,0,35,34,1,0,
        0,0,36,37,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,4,1,0,0,0,39,40,
        5,43,0,0,40,6,1,0,0,0,41,42,5,42,0,0,42,8,1,0,0,0,43,44,5,47,0,0,
        44,10,1,0,0,0,45,46,5,45,0,0,46,12,1,0,0,0,47,48,5,40,0,0,48,14,
        1,0,0,0,49,50,5,41,0,0,50,16,1,0,0,0,51,53,7,1,0,0,52,51,1,0,0,0,
        53,54,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,56,1,0,0,0,56,57,6,
        8,0,0,57,18,1,0,0,0,58,60,3,21,10,0,59,58,1,0,0,0,60,61,1,0,0,0,
        61,62,1,0,0,0,61,59,1,0,0,0,62,20,1,0,0,0,63,64,9,0,0,0,64,22,1,
        0,0,0,6,0,26,31,37,54,61,1,6,0,0
    ]

class LangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    REAL = 2
    SUM = 3
    MUL = 4
    DIV = 5
    SUB = 6
    LP = 7
    RP = 8
    WS = 9
    INVALID_TOKEN = 10
    INVALID = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'*'", "'/'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "REAL", "SUM", "MUL", "DIV", "SUB", "LP", "RP", "WS", 
            "INVALID_TOKEN", "INVALID" ]

    ruleNames = [ "INT", "REAL", "SUM", "MUL", "DIV", "SUB", "LP", "RP", 
                  "WS", "INVALID_TOKEN", "INVALID" ]

    grammarFileName = "LangLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


