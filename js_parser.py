__author__ = 'Christine'
import sys
import os
from pygments.lexers import get_lexer_by_name
from pygments import lex

if len(sys.argv) < 2:
    print("usage: python js_parser.py path_to_code_file")
    exit()

codeFilePath = os.path.abspath(sys.argv[1])
codeLines = (open(codeFilePath, 'r').readlines())[0]

lexer = get_lexer_by_name('javascript', encoding='utf-8')
tokens = lex(codeLines, lexer)
tokensList = list(tokens)
print(tokensList)
