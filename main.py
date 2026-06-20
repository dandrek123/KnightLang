from lexer import tokenize
from parser import parse
from interpreter import execute

variables = {}

ast = parse(tokenize("let age = 22"))
execute(ast, variables)

ast = parse(tokenize("print(age + 5)"))
execute(ast, variables)