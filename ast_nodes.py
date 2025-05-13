# ast_nodes.py

class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class Number(ASTNode):
    def __init__(self, value):
        self.value = value

class Identifier(ASTNode):
    def __init__(self, name):
        self.name = name

class BinOp(ASTNode):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class Assignment(ASTNode):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Print(ASTNode):
    def __init__(self, value):
        self.value = value

class IfElse(ASTNode):
    def __init__(self, condition, if_body, else_body=None):
        self.condition = condition
        self.if_body = if_body
        self.else_body = else_body

class FuncDef(ASTNode):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

class FuncCall(ASTNode):
    def __init__(self, name, args):
        self.name = name
        self.args = args

class Return(ASTNode):
    def __init__(self, value):
        self.value = value
