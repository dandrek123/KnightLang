from lexer import tokenize
from parser import parse
from interpreter import execute

variables = {}

with open("test.kn", "r") as file:
    lines = file.readlines()

i = 0

while i < len(lines):

    line = lines[i].strip()

    if not line:
        i += 1
        continue

    tokens = tokenize(line)

    ast = parse(tokens)

    if ast:

        if ast["type"] == "if":

            result = execute(ast, variables)

            i += 1

            next_line = lines[i].strip()

            if result:

                next_ast = parse(tokenize(next_line))

                execute(next_ast, variables)

        else:
            execute(ast, variables)

    i += 1