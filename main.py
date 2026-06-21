from lexer import tokenize
from parser import parse
from interpreter import execute

variables = {}

with open("test.kn", "r") as file:
    lines = file.readlines()

for line in lines:

    line = line.strip()

    if not line:
        continue

    tokens = tokenize(line)

    ast = parse(tokens)

    if ast:
        execute(ast, variables)