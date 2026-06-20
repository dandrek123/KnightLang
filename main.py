from lexer import tokenize
from parser import parse
from interpreter import execute

variables = {}

execute(
    parse(tokenize("let age = 22")),
    variables
)

execute(
    parse(tokenize("print(age + 5 * 2)")),
    variables
)