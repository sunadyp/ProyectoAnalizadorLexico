import ply.lex as lex

# Palabras clave
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'def': 'DEF',
    'return': 'RETURN',
    'print': 'PRINT',
}

# Lista de tokens
tokens = [
    'IDENTIFIER', 'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD', 'POWER',
    'EQUALS',
    'EQ', 'NE', 'GT', 'LT', 'GE', 'LE',
    'LPAREN', 'RPAREN', 'COLON', 'COMMA'
] + list(reserved.values())

# Reglas simples de expresiones regulares

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_MOD     = r'%'
t_POWER   = r'\*\*'
t_EQUALS  = r'='

t_EQ      = r'=='
t_NE      = r'!='
t_GT      = r'>'
t_LT      = r'<'
t_GE      = r'>='
t_LE      = r'<='

t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_COLON   = r':'
t_COMMA   = r','

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Identificadores y palabras clave
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

# Números

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Saltos de línea

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores

def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()