from context_free_grammar_file import ContextFreeGrammarFile
from context_free_grammar import ContextFreeGrammar

arquivo_gramatica = ContextFreeGrammarFile('convcc20231.txt')
g = arquivo_gramatica.read_file()
print(g.isLL1())

# IFSTAT -> if(EXPRESSION)STATEMENTIFSTATOPTS
# IFSTATOPTS -> elseSTATEMENT

# Esse ajuste faz ser LL1.

# IFSTAT -> if(EXPRESSION){STATEMENT}IFSTATOPTS
# IFSTATOPTS -> else{STATEMENT}

arquivo_analise = 'codigo1.txt'
with open(arquivo_analise, 'r') as arquivo:
    codigo = arquivo.read()
    codigo = codigo.replace(" ", "").replace("\n", "")
    print(g.recognize_sentence_ll1(codigo))