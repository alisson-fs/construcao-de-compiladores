from analLexica import lexical_analysis
from context_free_grammar_file import ContextFreeGrammarFile

arquivo_gramatica = ContextFreeGrammarFile('convcc20231.txt')
grammar = arquivo_gramatica.read_file()

code_file = input('Nome do arquivo: ')
with open(code_file, 'r') as arquivo:
    # Análise léxica
    code = arquivo.read()
    symbol_table = lexical_analysis(code)

    # Análise sintática
    # code = arquivo.read()
    # code = code.replace(" ", "").replace("\n", "")
    # print(grammar.recognize_sentence_ll1(code, symbol_table))