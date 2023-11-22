from anal_lexica import csv_table, lexical_analysis
from context_free_grammar_file import ContextFreeGrammarFile


arquivo_gramatica = ContextFreeGrammarFile('convcc20231.txt')
grammar = arquivo_gramatica.read_file()

code_file = input('Nome do arquivo: ')
with open('exemples/'+ code_file, 'r') as arquivo:
    # Análise léxica
    code = arquivo.read()
    symbol_table = lexical_analysis(code)

    if symbol_table != None:
        # Análise sintática
        code = code.replace(" ", "").replace("\n", "").replace("\t", "")
        sentence_recognized = grammar.recognize_sentence_ll1(code, symbol_table)
        if sentence_recognized:
            csv_table(symbol_table)
