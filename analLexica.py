import ply.lex as lex


# Definição dos tokens.
tokens = (
    'NUMERO_INTEIRO',
    'NUMERO_PONTO_FLUTUANTE',
    'IDENTIFICADOR',
    'PALAVRA_RESERVADA',
    'PARENTESES',
    'CHAVE',
    'COLCHETE',
    'OPERADOR_ARITMETICO',
    'OPERADOR_COMPARACAO',
    'OPERADOR_ATRIBUICAO',
    'PONTO_VIRGULA',
    'VIRGULA',
    'TIPO'
)

# Definição das expressões regulares para os tokens.
t_NUMERO_INTEIRO = r'-?\d+'
t_NUMERO_PONTO_FLUTUANTE = r'-?\d+\.\d+'
t_IDENTIFICADOR = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_PALAVRA_RESERVADA = r'(def|for|if|else|read|print|return|new|break|null)'
t_PARENTESES = r'\(|\)'
t_CHAVE = r'\{|\}'
t_COLCHETE = r'\[|\]'
t_OPERADOR_ARITMETICO = r'\+|\-|\*|\/|\%'
t_OPERADOR_COMPARACAO = r'\>|\<|\>\=|\<\=|\=\=|\!\='
t_OPERADOR_ATRIBUICAO = r'\='
t_PONTO_VIRGULA = r'\;'
t_VIRGULA = r'\,'
t_TIPO = r'(int|float|string|int_constant|float_constant|string_constant)'

# Ignorar espaços em branco e quebra de linha.
t_ignore = ' \t\n'

# Manipulador de erro para caracteres desconhecidos
def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)

if __name__ == "__main__":
    arquivo_analise = input('Nome do arquivo: ')
    with open(arquivo_analise, 'r') as arquivo:
        codigo = arquivo.read()

    # Crie o analisador léxico.
    lexer = lex.lex()

    # Teste o analisador léxico com uma string de entrada.
    lexer.input(codigo)

    for token in lexer:
        print(f"Tipo: {token.type}, Valor: {token.value}")
