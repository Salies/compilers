# Projeto de Compiladores
# FCT-UNESP, 2023
# Daniel Serezane e Gabriel Nozawa
# Parser de erros
# -------------------------------------------------------------------------------
# O ANTLR requisita a implementação da interface ANTLRErrorListener
# para tratamento de erros sintáticos.
# https://www.antlr.org/api/Java/org/antlr/v4/runtime/ANTLRErrorListener.html

# Se houver trechos em Inglês, é porque foram extraídos de clases do próprio ANTLR

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener as ANTLRErrorListener
from antlr4.error.ErrorStrategy import DefaultErrorStrategy
from antlr4.error.Errors import RecognitionException, NoViableAltException, InputMismatchException, FailedPredicateException

# Error strategy customizado para traduzir os erros
# msg = "entrada " + input + " não compatível, espera-se " + expectedString
class CustomErrorStrategy(DefaultErrorStrategy):
    def reportInputMismatch(self, recognizer: Parser, e: InputMismatchException):
        errDisplay = self.getTokenErrorDisplay(e.offendingToken)
        errDisplay = errDisplay[1:-1]
        expected = e.getExpectedTokens().toString(recognizer.literalNames, recognizer.symbolicNames)
        msg = "entrada não reconhecida " +  errDisplay + ", esperava-se " + expected + "."
        recognizer.notifyErrorListeners(msg, e.offendingToken, e)

    def reportNoViableAlternative(self, recognizer:Parser, e:NoViableAltException):
        tokens = recognizer.getTokenStream()
        if tokens is not None:
            if e.startToken.type==Token.EOF:
                input = "<EOF>"
            else:
                input = tokens.getText(e.startToken, e.offendingToken)
        else:
            input = "<entrada desconhecida>"
        msg = "sem alternativa viável para entrada " + self.escapeWSAndQuote(input)
        recognizer.notifyErrorListeners(msg, e.offendingToken, e)

    def reportFailedPredicate(self, recognizer, e):
        ruleName = recognizer.ruleNames[recognizer._ctx.getRuleIndex()]
        msg = "regra " + ruleName + " " + e.message
        recognizer.notifyErrorListeners(msg, e.offendingToken, e)

    def reportUnwantedToken(self, recognizer:Parser):
        if self.inErrorRecoveryMode(recognizer):
            return

        self.beginErrorCondition(recognizer)
        t = recognizer.getCurrentToken()
        tokenName = self.getTokenErrorDisplay(t)
        expecting = self.getExpectedTokens(recognizer)
        msg = "entrada estranha " + tokenName + " esperava-se " \
            + expecting.toString(recognizer.literalNames, recognizer.symbolicNames)
        recognizer.notifyErrorListeners(msg, t, None)

    def reportMissingToken(self, recognizer:Parser):
        if self.inErrorRecoveryMode(recognizer):
            return
        self.beginErrorCondition(recognizer)
        t = recognizer.getCurrentToken()
        expecting = self.getExpectedTokens(recognizer)
        msg = "esperava-se " + expecting.toString(recognizer.literalNames, recognizer.symbolicNames)
        recognizer.notifyErrorListeners(msg, t, None)

    def reportError(self, recognizer:Parser, e:RecognitionException):
       # if we've already reported an error and have not matched a token
       # yet successfully, don't report any errors.
        if self.inErrorRecoveryMode(recognizer):
            return # don't report spurious errors
        self.beginErrorCondition(recognizer)
        if isinstance( e, NoViableAltException ):
            self.reportNoViableAlternative(recognizer, e)
        elif isinstance( e, InputMismatchException ):
            self.reportInputMismatch(recognizer, e)
        elif isinstance( e, FailedPredicateException ):
            self.reportFailedPredicate(recognizer, e)
        else:
            print("erro sintático desconhecido: " + type(e).__name__)
            recognizer.notifyErrorListeners(e.message, e.offendingToken, e)

    def recover(self, recognizer: Parser, e: RecognitionException):
        super().recover(recognizer, e)
        # if not EOF
        if e.offendingToken.type != Token.EOF:
            recognizer.consume()

class ErrorListener(ANTLRErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append("Erro na linha " + str(line) + ", coluna " + str(column) + ": " + msg)
    
    def getErrorsAsStr(self):
        return '\n\n'.join(self.errors) if len(self.errors) > 0 else ''
    
    def getErrors(self):
        return self.errors
    
    def addError(self, error_str, line, column):
        self.errors.append("Erro na linha " + str(line) + ", coluna " + str(column) + ": " + error_str)