def parse_expression(tokens):

    if len(tokens) == 1:
        return tokens[0]

    if len(tokens) >= 3 and tokens[1] == "(" and tokens[-1] == ")":
        return {
            "type": "call",
            "name": tokens[0],
            "args": tokens[2:-1]
        }

    left = parse_expression(tokens[:-2])

    operator = tokens[-2]

    right = tokens[-1]

    if operator == "+":
        return {
            "type": "add",
            "left": left,
            "right": right
        }

    if operator == "-":
        return {
            "type": "subtract",
            "left": left,
            "right": right
        }

    if operator == "*":
        return {
            "type": "multiply",
            "left": left,
            "right": right
        }

    if operator == "/":
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
            "args": tokens[2:-1]
        }

    return None