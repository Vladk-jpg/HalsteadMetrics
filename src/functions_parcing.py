from pygments import lex
from pygments.lexers import GoLexer
from pygments.token import Token

def functions_parcing(operands, code):
    tokens = lex(code, GoLexer())

    name_flag = False
    name = ""
    for token_type, value in tokens: 
        if token_type in Token.Name:
            name_flag = True
            name = value
            continue
        if name_flag and (value == "("):
            if name in operands:
                operands[name] += 1
            else:
                operands[name] = 1
        name_flag = False

