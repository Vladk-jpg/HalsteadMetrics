from pygments import lex
from pygments.lexers import GoLexer
from pygments.token import Token

def punctuation_parsing(operators, code):

    tokens = lex(code, GoLexer())

    punctuation_values = {
        "{", "[", ",", ";"
    }

    temp_value = ""
    for token_type, value in tokens: 
        if value in punctuation_values:
            if value == "{":
                temp_value = "{}"
            elif value == "[":
                temp_value = "[]"
            else:
                temp_value = value
            if temp_value in operators:
                operators[temp_value] += 1
            else:
                operators[temp_value] = 1
