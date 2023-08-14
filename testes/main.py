import sys
from antlr4 import *
from ExprLexer import ExprLexer
 
def main(argv):
    input_stream = FileStream(argv[1])
    print(input_stream)
    lexer = ExprLexer(input_stream)
    tokens = lexer.getAllTokens()
    for token in tokens:
        print(token.text, lexer.symbolicNames[token.type])
 
if __name__ == '__main__':
    main(sys.argv)