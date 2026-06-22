def split_arguments(tokens):
    args = []
    current = []
    depth = 0

    for token in tokens:
        if token in ["(", "["]:
            depth += 1
        elif token in [")", "]"]:
            depth -= 1

        if token == "," and depth == 0:
            if current:
                args.append(parse_expression(current))
                current = []
        else:
            current.append(token)

    if current:
        args.append(parse_expression(current))

    return args

def tokens_are_list(tokens):
    if len(tokens) < 2:
        return False

    if tokens[0] != "[" or tokens[-1] != "]":
        return False

    depth = 0

    for index, token in enumerate(tokens):
        if token == "[":
            depth += 1
        elif token == "]":
            depth -= 1

        if depth == 0 and index != len(tokens) - 1:
            return False

    return depth == 0

def tokens_are_wrapped(tokens):
    if len(tokens) < 2:
        return False

    if tokens[0] != "(" or tokens[-1] != ")":
        return False

    depth = 0

    for index, token in enumerate(tokens):
        if token == "(":
            depth += 1
        elif token == ")":
            depth -= 1

        if depth == 0 and index != len(tokens) - 1:
            return False

    return depth == 0


def find_operator_outside_parentheses(tokens, operators):
    depth = 0

    for index in range(len(tokens) - 1, -1, -1):
        token = tokens[index]

        if token in [")", "]"]:
            depth += 1
        elif token in ["(", "["]:
            depth -= 1
        elif depth == 0 and token in operators:
            return index

    return -1


def tokens_are_index(tokens):
    if len(tokens) < 4:
        return False

    if tokens[1] != "[" or tokens[-1] != "]":
        return False

    depth = 0

    for index in range(1, len(tokens)):
        token = tokens[index]

        if token == "[":
            depth += 1
        elif token == "]":
            depth -= 1

        if depth == 0 and index != len(tokens) - 1:
            return False

    return depth == 0

def parse_expression(tokens):

    if tokens_are_wrapped(tokens):
        return parse_expression(tokens[1:-1])

    if tokens_are_list(tokens):
        return {
            "type": "list",
            "items": split_arguments(tokens[1:-1])
        }

    if tokens_are_index(tokens):
        return {
            "type": "index",
            "list": parse_expression([tokens[0]]),
            "index": parse_expression(tokens[2:-1])
        }

    if len(tokens) == 1:
        return tokens[0]

    if len(tokens) >= 3 and tokens[1] == "(" and tokens[-1] == ")":
        return {
            "type": "call",
            "name": tokens[0],
            "args": split_arguments(tokens[2:-1])
        }

    operator_index = find_operator_outside_parentheses(tokens, ["+", "-"])

    if operator_index != -1:
        left = parse_expression(tokens[:operator_index])
        right = parse_expression(tokens[operator_index + 1:])

        if tokens[operator_index] == "+":
            return {
                "type": "add",
                "left": left,
                "right": right
            }

        if tokens[operator_index] == "-":
            return {
                "type": "subtract",
                "left": left,
                "right": right
            }

    operator_index = find_operator_outside_parentheses(tokens, ["*", "/"])

    if operator_index != -1:
        left = parse_expression(tokens[:operator_index])
        right = parse_expression(tokens[operator_index + 1:])

        if tokens[operator_index] == "*":
            return {
                "type": "multiply",
                "left": left,
                "right": right
            }

        if tokens[operator_index] == "/":
            return {
                "type": "divide",
                "left": left,
                "right": right
            }

    return tokens


def parse(tokens):

    if not tokens:
        return None

    # let age = 22
    if tokens[0] == "let":
        return {
            "type": "let",
            "name": tokens[1],
            "value": parse_expression(tokens[3:])
        }
    
    # count = count + 1
    if len(tokens) >= 3 and tokens[1] == "=":

        return {
            "type": "assign",
            "name": tokens[0],
            "value": parse_expression(tokens[2:])
        }

    if tokens[0] == "else":
        return {
            "type": "else"
        }

    if tokens[0] == "return":
        return {
            "type": "return",
            "value": parse_expression(tokens[1:])
        }

    if tokens[0] == "func":
        return {
            "type": "func",
            "name": tokens[1],
            "params": tokens[2:]
        }
    
    elif tokens[0] == "while":

        return {
            "type": "while",
            "left": tokens[1],
            "operator": tokens[2],
            "right": tokens[3]
        }

    # print(...)
    elif tokens[0] == "print":
        return {
            "type": "print",
            "expression": parse_expression(tokens[2:-1])
        }

    # if age > 18
    elif tokens[0] == "if":
        return {
            "type": "if",
            "left": tokens[1],
            "operator": tokens[2],
            "right": tokens[3]
        }

    if len(tokens) >= 3 and tokens[1] == "(" and tokens[-1] == ")":
        return {
            "type": "call",
            "name": tokens[0],
            "args": split_arguments(tokens[2:-1])
        }

    return None