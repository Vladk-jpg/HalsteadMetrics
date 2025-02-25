from main_window import show_table
from common_operators_parcing import common_operators_parsing
from common_literals_parcing import common_literals_parsing
from functions_parcing import functions_parcing
from variables_parcing import variables_parsing
from punctuation_parcing import punctuation_parsing
import os

def main():
    operators = {}
    operands = {}
    file_path = os.path.abspath("Go/main.go")

    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    common_literals_parsing(operands, code)
    common_operators_parsing(operators, code)
    functions_parcing(operators, code)
    variables_parsing(operands, code)
    punctuation_parsing(operators, code)

    show_table(operators, operands)

if __name__ == "__main__":
    main()
