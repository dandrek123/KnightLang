from lexer import tokenize
from parser import parse
from interpreter import execute

variables = {}
last_if_result = None

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
            
            last_if_result = result

            i += 1

            next_line = lines[i].strip()

            if result:

                next_ast = parse(tokenize(next_line))

                execute(next_ast, variables)

        elif ast["type"] == "else":

            i += 1

            next_line = lines[i].strip()

            if last_if_result == False:

                next_ast = parse(tokenize(next_line))

                execute(next_ast, variables)

            i += 1

            continue
        else:
            execute(ast, variables)

    i += 1