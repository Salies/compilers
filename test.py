import sys
from antlr4 import *
from LangLexer import LangLexer
 
def main(argv):
    input_stream = FileStream(argv[1])
    #print(input_stream)
    lexer = LangLexer(input_stream)
    tokens = lexer.getAllTokens()
    #print('tokens', tokens)
    for token in tokens:
        print(token.text, lexer.symbolicNames[token.type])
 
if __name__ == '__main__':
    main(sys.argv)