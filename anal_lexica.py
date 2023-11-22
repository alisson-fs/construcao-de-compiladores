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

# Lista para armazenar os tokens encontrados.
symbol_table = []

# Ignorar espaços em branco e quebra de linha.
t_ignore = ' \t\n'


# Manipulador de erro para caracteres desconhecidos.
def t_error(t):
    position = update_position(t)
    raise Exception(f'Erro léxico na linha {position[0]} e coluna {position[1]}, com o seguinte caracter: {t.value[0]}')


# Função para atualizar a posição (linha e coluna) do token.
def update_position(token):
    line_num = 1  # Começar na primeira linha
    column_num = 1  # Começar na primeira coluna

    # Iterar por cada caractere na entrada até o token atual
    for i in range(token.lexpos):
        if token.lexer.lexdata[i] == '\n':  # Se encontrar uma quebra de linha, incrementar número de linha e definir o início da próxima linha
            line_num += 1
            column_num = 1  # Reiniciar na primeira coluna da próxima linha
        elif token.lexer.lexdata[i] == ' ':  # Se encontrar um espaço em branco, incrementar número de coluna
            column_num += 1
        elif token.lexer.lexdata[i] == '\t':
            column_num += 4
        else:
            column_num += 1  # Incrementar número de coluna normalmente

    return line_num, column_num


def t_STRING(t):
    r'(\"[^\"]*\"|\'[^\']*\')'
    t.type = 'STRING'
    # Adicionar o identificador e sua posição à tabela de símbolos
    position = update_position(t)
    symbol_table.append((t.value, position))

    return t


def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in {'def', 'for', 'if', 'else', 'read', 'print', 'return', 'new', 'break', 'null'}:
        t.type = 'PALAVRA_RESERVADA'
    elif t.value in {'int', 'float', 'string', 'int_constant', 'float_constant', 'string_constant'}:
        t.type = 'TIPO'
    else:
        t.type = 'IDENTIFICADOR'
    # Adicionar o token e sua posição na tabela de símbolos
    position = update_position(t)
    symbol_table.append((t.value, position))

    return t


def t_PALAVRA_RESERVADA(t):
    r'(def|for|if|else|read|print|return|new|break|null)'
    t.type = 'IDENTIFICADOR'
    position = update_position(t)
    symbol_table.append((t.value, position))

    return t


def t_ABRE_PARENTESES(t):
    r'\('
    t.type = 'ABRE_PARENTESES'
    position = update_position(t)
    symbol_table.append((t.value, position))

    return t


def t_FECHA_PARENTESES(t):
    r'\)'
    t.type = 'FECHA_PARENTESES'
    position = update_position(t)
    symbol_table.append((t.value, position))

    return t


def t_ABRE_CHAVE(t):
    r'\{'
    t.type = 'ABRE_CHAVE'
    position = update_position(t)
    symbol_table.append((t.value, position))

    return t


def t_FECHA_CHAVE(t):
    r'\}'
    t.type = 'FECHA_CHAVE'
    position = update_position(t)
    symbol_table.append((t.value, position))

    return t


def t_ABRE_COLCHETE(t):
    r'\['
    t.type = 'ABRE_COLCHETE'
    position = update_position(t)
    symbol_table.append((t.value, position))

    return t


def t_FECHA_COLCHETE(t):
    r'\]'
    t.type = 'FECHA_COLCHETE'
    position = update_position(t)
    symbol_table.append((t.value, position))

    return t


def t_OPERADOR_ARITMETICO(t):
    r'\+|\-|\*|\/|\%'
    t.type = 'OPERADOR_ARITMETICO'
    position = update_position(t)
    symbol_table.append((t.value, position))

    return t


def t_OPERADOR_COMPARACAO(t):
    r'\>\=|\<\=|\=\=|\!\=|\>|\<'
    t.type = 'OPERADOR_COMPARACAO'
    position = update_position(t)
    symbol_table.append((t.value, position))

    return t


def t_OPERADOR_ATRIBUICAO(t):
    r'\='
    t.type = 'OPERADOR_ATRIBUICAO'
    position = update_position(t)
    symbol_table.append((t.value, position))

    return t


def t_PONTO_VIRGULA(t):
    r'\;'
    t.type = 'PONTO_VIRGULA'
    position = update_position(t)
    symbol_table.append((t.value, position))

    return t


def t_VIRGULA(t):
    r'\,'
    t.type = 'VIRGULA'
    position = update_position(t)
    symbol_table.append((t.value, position))

    return t


def t_TIPO(t):
    r'(int|float|string|int_constant|float_constant|string_constant)'#
    t.type = 'TIPO'
    position = update_position(t)
    symbol_table.append((t.value, position))

    return t


def t_NUMERO_INTEIRO(t):
    r'-?\d+'
    t.type = 'NUMERO_INTEIRO'
    # Adicionar o identificador e sua posição à tabela de símbolos
    position = update_position(t)
    symbol_table.append((t.value, position))

    return t


def t_NUMERO_PONTO_FLUTUANTE(t):
    r'-?\d+\.\d+'
    t.type = 'NUMERO_PONTO_FLUTUANTE'
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
        if i['value'].replace(" ", "") == value:
            return i['type']
    return None


def lexical_analysis(code: str):
    lexer = lex.lex()
    lexer.input(code)
    try:
        symbol_table = create_table(lexer)
        print('Análise léxica finalizada com sucesso.')
        return symbol_table
    except Exception as e:
        print(e)
        return None
    