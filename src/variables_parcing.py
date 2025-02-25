from pygments import lex
from pygments.lexers import GoLexer
from pygments.token import Token

def variables_parsing(operands, code):
    tokens = list(lex(code, GoLexer())) 

    operator_values = {
        "+", "-", "*", "/", "%", "&", "|", "^", "<<", ">>", "&^",
        "==", "!=", "<", "<=", ">", ">=", "&&", "||", "!", "=",
        "+=", "-=", "*=", "/=", "%=", "<<=", ">>=", "&=", "|=", "^=", "&^=",
        "<-"
    }
    
    for i, (tok_type, value) in enumerate(tokens):
        if tok_type == Token.Name.Other:
            left_whitespace = i > 0 and tokens[i - 1][0] == Token.Text.Whitespace
            right_whitespace = i < len(tokens) - 1 and tokens[i + 1][0] == Token.Text.Whitespace
            left_open_brace = i > 0 and tokens[i - 1][1] == "("
            right_close_brace = i < len(tokens) - 1 and tokens[i + 1][1] == ")"
            left_colon = i > 0 and tokens[i - 1][1] == ","
            right_colon = i < len(tokens) - 1 and tokens[i + 1][1] == ","
            left_operator = i > 0 and tokens[i - 1][1] in operator_values
            right_operator = i < len(tokens) - 1 and tokens[i + 1][1] in operator_values
            right_figure_brace = i < len(tokens) - 1 and tokens[i + 1][1] == "{"
        
            if (left_whitespace or left_open_brace or left_colon or left_operator) and (right_whitespace or right_close_brace or right_colon or right_operator or right_figure_brace):
                if value in operands:
                    operands[value] += 1
                else:
                    operands[value] = 1
    

