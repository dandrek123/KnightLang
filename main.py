from lexer import tokenize
from parser import parse
from interpreter import execute, evaluate

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


def run_function_call(call_ast):
    function_name = call_ast["name"]

    if function_name == "len":
        if len(call_ast["args"]) == 0:
            print("len() expects one argument")
            return None

        value = evaluate(call_ast["args"][0], variables)
        return len(value)

    if function_name not in functions:
        print("Function not found:", function_name)
        return None

    function_data = functions[function_name]
    params = function_data["params"]
    body = function_data["body"]
    args = call_ast["args"]

    old_values = {}

    for index, param in enumerate(params):
        if param in variables:
            old_values[param] = variables[param]

        if index < len(args):
            variables[param] = evaluate(args[index], variables)

    return_value = run_lines(body)

    for param in params:
        if param in old_values:
            variables[param] = old_values[param]
        elif param in variables:
            del variables[param]

    return return_value


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

        if ast["type"] in ["let", "assign"] and isinstance(ast.get("value"), dict) and ast["value"].get("type") == "call":
            variables[ast["name"]] = run_function_call(ast["value"])
            i += 1
            continue

        if ast["type"] == "print" and isinstance(ast.get("expression"), dict) and ast["expression"].get("type") == "call":
            print(run_function_call(ast["expression"]))
            i += 1
            continue

        if ast["type"] == "if":
            result = execute(ast, variables)
            last_if_result = result

            block, next_index = get_block(lines, i + 1, get_indent(raw_line))

            if result:
                return_value = run_lines(block)

                if return_value is not None:
                    return return_value

            i = next_index
            continue

        elif ast["type"] == "else":
            block, next_index = get_block(lines, i + 1, get_indent(raw_line))

            if last_if_result == False:
                return_value = run_lines(block)

                if return_value is not None:
                    return return_value

            i = next_index
            continue

        elif ast["type"] == "while":
            block, next_index = get_block(lines, i + 1, get_indent(raw_line))

            while execute(ast, variables):
                return_value = run_lines(block)

                if return_value is not None:
                    return return_value

            i = next_index
            continue

        elif ast["type"] == "func":
            block, next_index = get_block(lines, i + 1, get_indent(raw_line))
            functions[ast["name"]] = {
                "params": ast["params"],
                "body": block
            }

            i = next_index
            continue

        elif ast["type"] == "call":
            run_function_call(ast)

        else:
            result = execute(ast, variables)

            if ast["type"] == "return":
                return result

        i += 1


with open("test.kn", "r") as file:
    lines = file.readlines()

run_lines(lines)
