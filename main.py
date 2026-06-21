from lexer import tokenize
from parser import parse
from interpreter import execute

variables = {}
functions = {}


def get_indent(line):
    count = 0

    for char in line:
        if char == " ":
            count += 1
        else:
            break

    return count


def get_block(lines, start_index, parent_indent):
    block = []
    i = start_index

    while i < len(lines):
        line = lines[i]

        if not line.strip():
            i += 1
            continue

        if get_indent(line) <= parent_indent:
            break

        block.append(line)
        i += 1

    return block, i


def run_line(line):
    tokens = tokenize(line.strip())
    ast = parse(tokens)

    if ast:
        return execute(ast, variables)

    return None


def run_lines(lines):
    i = 0
    last_if_result = None

    while i < len(lines):
        raw_line = lines[i]
        line = raw_line.strip()

        if not line:
            i += 1
            continue

        tokens = tokenize(line)
        ast = parse(tokens)

        if not ast:
            i += 1
            continue

        if ast["type"] == "if":
            result = execute(ast, variables)
            last_if_result = result

            block, next_index = get_block(lines, i + 1, get_indent(raw_line))

            if result:
                run_lines(block)

            i = next_index
            continue

        elif ast["type"] == "else":
            block, next_index = get_block(lines, i + 1, get_indent(raw_line))

            if last_if_result == False:
                run_lines(block)

            i = next_index
            continue

        elif ast["type"] == "while":
            block, next_index = get_block(lines, i + 1, get_indent(raw_line))

            while execute(ast, variables):
                run_lines(block)

            i = next_index
            continue

        elif ast["type"] == "func":
            block, next_index = get_block(lines, i + 1, get_indent(raw_line))
            functions[ast["name"]] = block

            i = next_index
            continue

        elif ast["type"] == "call":
            function_name = ast["name"]

            if function_name in functions:
                run_lines(functions[function_name])
            else:
                print("Function not found:", function_name)

        else:
            execute(ast, variables)

        i += 1


with open("test.kn", "r") as file:
    lines = file.readlines()

run_lines(lines)