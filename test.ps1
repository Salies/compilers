java -jar ./antlr-4.13.0-complete.jar -Dlanguage=Python3 ./tools/LangLexer.g4
java -jar ./antlr-4.13.0-complete.jar -Dlanguage=Python3 -visitor -listener ./tools/LangGrammar.g4
cp .\LangLexer.py .\tools\LangLexer.py
cp .\LangGrammar.py .\tools\LangGrammar.py
cp .\LangGrammarListener.py .\tools\LangGrammarListener.py
cp .\LangGrammarVisitor.py .\tools\LangGrammarVisitor.py
python main.py
rm .\LangLexer.*
rm .\LangGrammar.*
rm .\LangGrammarListener.*
rm .\LangGrammarVisitor.*