def parse_expression(tokens):

    if len(tokens) == 1:
        return tokens[0]

    # x + y
    if len(tokens) == 3 and tokens[1] == "+":
        return {
            "type": "add",
            "left": tokens[0],
            "right": tokens[2]
        }

    # x - y
    if len(tokens) == 3 and tokens[1] == "-":
        return {
            "type": "subtract",
            "left": tokens[0],
            "right": tokens[2]
        }

    # x * y
    if len(tokens) == 3 and tokens[1] == "*":
        return {
            "type": "multiply",
            "left": tokens[0],
            "right": tokens[2]
        }

    # x / y
    if len(tokens) == 3 and tokens[1] == "/":
        return {
            "type": "divide",
            "left": tokens[0],
            "right": tokens[2]
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
            "value": tokens[3]
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

    return None