import ply.yacc as yacc
from lexer import tokens
from ast_nodes import *
# Precedencia de operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('right', 'POWER'),
)

# Programa → lista de sentencias
def p_program(p):
    '''program : statements'''
    p[0] = Program(p[1])

# Lista de sentencias
def p_statements_multiple(p):
    '''statements : statements statement'''
    p[0] = p[1] + [p[2]]

def p_statements_single(p):
    '''statements : statement'''
    p[0] = [p[1]]

# Sentencias posibles
def p_statement(p):
    '''statement : assignment
                 | print
                 | if_else
                 | func_def
                 | func_call
                 | return_stmt
                 | expression'''
    p[0] = p[1]

# Asignación: x = expr
def p_assignment(p):
    '''assignment : IDENTIFIER EQUALS expression'''
    p[0] = Assignment(p[1], p[3])

# Expresiones aritméticas
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MOD expression
                  | expression POWER expression'''
    p[0] = BinOp(p[2], p[1], p[3])

def p_expression_compare(p):
    '''expression : expression EQ expression
                  | expression NE expression
                  | expression GT expression
                  | expression LT expression
                  | expression GE expression
                  | expression LE expression'''
    p[0] = BinOp(p[2], p[1], p[3])

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = Number(p[1])

def p_expression_identifier(p):
    '''expression : IDENTIFIER'''
    p[0] = Identifier(p[1])

def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

# print(x)
def p_print(p):
    '''print : PRINT LPAREN expression RPAREN'''
    p[0] = Print(p[3])

# if x > y: ...
def p_if_else(p):
    '''if_else : IF expression COLON statement ELSE COLON statement
               | IF expression COLON statement'''
    if len(p) == 8:
        p[0] = IfElse(p[2], [p[4]], [p[7]])
    else:
        p[0] = IfElse(p[2], [p[4]])

# return expression
def p_return_stmt(p):
    '''return_stmt : RETURN expression'''
    p[0] = Return(p[2])

# def f(x, y): ...
def p_func_def(p):
    '''func_def : DEF IDENTIFIER LPAREN param_list RPAREN COLON statements'''
    p[0] = FuncDef(p[2], p[4], p[7])

# Llamada a función
def p_func_call(p):
    '''func_call : IDENTIFIER LPAREN arg_list RPAREN'''
    p[0] = FuncCall(p[1], p[3])

def p_param_list(p):
    '''param_list : IDENTIFIER
                  | param_list COMMA IDENTIFIER'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_param_list_empty(p):
    'param_list : '
    p[0] = []

def p_arg_list(p):
    '''arg_list : expression
                | arg_list COMMA expression'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_arg_list_empty(p):
    'arg_list : '
    p[0] = []


def p_error(p):
    if p:
        print(f"[Error de sintaxis]\n  → Token inesperado: '{p.value}' en línea {p.lineno}\n  → Tipo de token: {p.type}")
    else:
        print("[Error de sintaxis] Fin inesperado")

# Construcción del parser
parser = yacc.yacc()

# Función de entrada para analizar texto
def parse_code(code):
    return parser.parse(code)
