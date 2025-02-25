from pygments import lex
from pygments.lexers import GoLexer
from pygments.token import Token

def common_operators_parsing(operators, code):

    tokens = lex(code, GoLexer())

    operator_values = {
        "+", "-", "*", "/", "%", "&", "|", "^", "<<", ">>", "&^",
        "==", "!=", "<", "<=", ">", ">=", "&&", "||", "!", "=",
        "+=", "-=", "*=", "/=", "%=", "<<=", ">>=", "&=", "|=", "^=", "&^=",
        "<-", "if", "switch", "for", "range", "goto", "break", "continue", 
        "fallthrough", "return", "defer", "go"
    }
    
    else_flag = False

    for token_type, value in tokens: 
        if value == "else":
            else_flag = True
            continue
        if else_flag and value != " ":
            else_flag = False
            if value == "if":
                continue
        
        if token_type in Token.Operator or value in operator_values:
            if value in operators:
                operators[value] += 1
            else:
                operators[value] = 1

"""operators = {}
file_path = os.path.abspath("Go/main.go")

with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

common_operators_parsing(operators, code)
for key in operators:
    print(f"{key} : {operators[key]}")"""
