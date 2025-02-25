from pygments import lex
from pygments.lexers import GoLexer
from pygments.token import Token
import os

def common_operators_parsing():
    file_path = os.path.abspath("Go/main.go")

    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    tokens = lex(code, GoLexer())

    for token_type, value in tokens: 
        print(f"{token_type} - {value}")

common_operators_parsing()
