import ply.lex as lex
from tabulate import tabulate


# Definição dos tokens.
tokens = (
    'NUMERO_INTEIRO',
    'NUMERO_PONTO_FLUTUANTE',
    'STRING',
    'IDENTIFICADOR',
    'PALAVRA_RESERVADA',
    'ABRE_PARENTESES',
    'FECHA_PARENTESES',
    'ABRE_CHAVE',
    'FECHA_CHAVE',
    'ABRE_COLCHETE',
    'FECHA_COLCHETE',
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
t_STRING = r'(\"[^\"]*\"|\'[^\']*\')'
t_PALAVRA_RESERVADA = r'(def|for|if|else|read|print|return|new|break|null)'
t_ABRE_PARENTESES = r'\('
t_FECHA_PARENTESES = r'\)'
t_ABRE_CHAVE = r'\{'
t_FECHA_CHAVE = r'\}'
t_ABRE_COLCHETE = r'\['
t_FECHA_COLCHETE = r'\]'
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
    print(f"Erro léxico neste caracter: {t.value[0]}")
    t.lexer.skip(1)


# Lista para armazenar os identificadores encontrados
symbol_table = []


# Função para atualizar a posição (linha e coluna) do token
def update_position(token):
    line_num = 1  # Começar na primeira linha
    column_num = 1  # Começar na primeira coluna

    # Iterar por cada caractere na entrada até o token atual
    for i in range(token.lexpos):
        if token.lexer.lexdata[i] == '\n':  # Se encontrar uma quebra de linha, incrementar número de linha e definir o início da próxima linha
            line_num += 1
            column_num = 1  # Reiniciar na primeira coluna da próxima linha
        elif token.lexer.lexdata[i] in [' ', '\t']:  # Se encontrar um espaço em branco, incrementar número de coluna
            column_num += 1
        else:
            column_num += 1  # Incrementar número de coluna normalmente

    return line_num, column_num


# Token para identificadores
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Verificar se é uma palavra reservada
    if t.value in {'def', 'for', 'if', 'else', 'read', 'print', 'return', 'new', 'break', 'null'}:
        t.type = 'PALAVRA_RESERVADA'
    elif t.value in {'int', 'float', 'string', 'int_constant', 'float_constant', 'string_constant'}:
        t.type = 'TIPO'
    else:
        t.type = 'IDENTIFICADOR'
        # Adicionar o identificador e sua posição à tabela de símbolos
        position = update_position(t)
        symbol_table.append((t.value, position))

    return t


def create_table(lexer):
    table = []
    tokens = []
    for token in lexer:
        if token.value == 'i':
            pass
        if token.value not in tokens:
            token_dict = {}
            token_dict['value'] = token.value
            token_dict['type'] = token.type
            token_dict['occurrence'] = []
            table.append(token_dict)
            tokens.append(token.value)


    for identifier, position in symbol_table:
        for i in table:
            if i['value'] == identifier:
                i['occurrence'].append((position[0], position[1]))
    
    return table


def show_table(table):
    table_data = []
    for i in table:
        row = []
        for j in i.values():
            row.append(j)
        table_data.append(row)

    table = tabulate(
        tabular_data=table_data, 
        headers=['value', 'type', 'occurrence'], 
        tablefmt="fancy_grid", 
        stralign="center"
    )

    print(table)


def get_type(value, symbol_table):
    for i in symbol_table:
        if i['value'] == value:
            return i['type']
    return None


def lexical_analysis(code: str):
    lexer = lex.lex()
    lexer.input(code)
    symbol_table = create_table(lexer)
    print('Análise léxica finalizada com sucesso.')
    return symbol_table
