# Generated from ExprLexer.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,42,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,0,1,0,1,1,1,1,1,1,1,2,4,2,22,8,2,11,2,12,2,23,1,3,4,3,27,
        8,3,11,3,12,3,28,1,3,5,3,32,8,3,10,3,12,3,35,9,3,1,4,1,4,1,5,1,5,
        1,5,1,5,0,0,6,1,1,3,2,5,3,7,4,9,5,11,6,1,0,2,1,0,48,57,3,0,65,90,
        95,95,97,122,44,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,
        0,9,1,0,0,0,0,11,1,0,0,0,1,13,1,0,0,0,3,17,1,0,0,0,5,21,1,0,0,0,
        7,26,1,0,0,0,9,36,1,0,0,0,11,38,1,0,0,0,13,14,5,97,0,0,14,15,5,110,
        0,0,15,16,5,100,0,0,16,2,1,0,0,0,17,18,5,111,0,0,18,19,5,114,0,0,
        19,4,1,0,0,0,20,22,7,0,0,0,21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,
        0,0,23,24,1,0,0,0,24,6,1,0,0,0,25,27,7,1,0,0,26,25,1,0,0,0,27,28,
        1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,33,1,0,0,0,30,32,7,0,0,0,
        31,30,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,8,1,0,
        0,0,35,33,1,0,0,0,36,37,9,0,0,0,37,10,1,0,0,0,38,39,5,32,0,0,39,
        40,1,0,0,0,40,41,6,5,0,0,41,12,1,0,0,0,4,0,23,28,33,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AND = 1
    OR = 2
    INT = 3
    ID = 4
    ERR_TOKEN = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'and'", "'or'", "' '" ]

    symbolicNames = [ "<INVALID>",
            "AND", "OR", "INT", "ID", "ERR_TOKEN", "WS" ]

    ruleNames = [ "AND", "OR", "INT", "ID", "ERR_TOKEN", "WS" ]

    grammarFileName = "ExprLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


