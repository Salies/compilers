# Nosso parser de erros.
# O ANTLR requisita a implementação da interface ANTLRErrorListener
# para tratamento de erros sintáticos.
# https://www.antlr.org/api/Java/org/antlr/v4/runtime/ANTLRErrorListener.html

from antlr4.error.ErrorListener import ErrorListener as ANTLRErrorListener

class ErrorListener(ANTLRErrorListener):
    pass