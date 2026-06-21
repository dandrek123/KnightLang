from lexer import tokenize
from parser import parse
from interpreter import execute

variables = {}
last_if_result = None

def get_indent(line):

    count = 0

    for char in line:

        if char == " ":
            count += 1
        else:
            break

    return count

def get_block(lines, start_index):

    block = []

    block_indent = get_indent(lines[start_index])

    while start_index < len(lines):

        line = lines[start_index]

        if not line.strip():
            start_index += 1
            continue

        if get_indent(line) < block_indent:
            break

        block.append(line.strip())

        start_index += 1

    return block

def run_line(line, variables):

    tokens = tokenize(line)

    ast = parse(tokens)

    if ast:
        return execute(ast, variables)

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

        elif ast["type"] == "while":

            block = get_block(lines, i + 1)

            while execute(ast, variables):

                for block_line in block:

                    run_line(block_line, variables)

            i += len(block)

            continue

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