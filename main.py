from Parser import parse_code
from ast_nodes import ASTNode

def print_ast(node, indent=0):
    pad = "  " * indent
    if isinstance(node, list):
        for n in node:
            print_ast(n, indent)
    elif isinstance(node, ASTNode):
        print(f"{pad}{node.__class__.__name__}")
        for attr, value in vars(node).items():
            if isinstance(value, ASTNode) or isinstance(value, list):
                print(f"{pad}  {attr}:")
                print_ast(value, indent + 2)
            else:
                print(f"{pad}  {attr}: {value}")
    else:
        print(f"{pad}{node}")

def main():
    print("=== Intérprete simple (con AST) ===")
    print("Escribe tu código. Escribe una línea vacía para procesar.\n")

    lines = []
    while True:
        try:
            line = input(">>> ")
            if line.strip() == "":
                break
            lines.append(line)
        except EOFError:
            break

    code = "\n".join(lines)

    try:
        ast = parse_code(code)
        print("\n=== Árbol de Sintaxis Abstracta (AST) ===")
        print_ast(ast)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
