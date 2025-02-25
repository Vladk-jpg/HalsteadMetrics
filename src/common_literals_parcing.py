from pygments import lex
from pygments.lexers import GoLexer
from pygments.token import Token

def common_literals_parsing(operands, code):
    tokens = lex(code, GoLexer())

    for token_type, value in tokens: 
        if token_type in Token.Literal:
            if value in operands:
                operands[value] += 1
            else:
                operands[value] = 1

"""operands = {}
file_path = os.path.abspath("Go/main.go")
with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

common_literals_parsing(operands, code)
for key in operands:
    print(f"{key} : {operands[key]}")"""
