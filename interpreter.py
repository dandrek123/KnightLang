def run(filename):
    variables = {}

    with open(filename, "r") as file:
        lines = file.readlines()

    def get_value(token):
        token = token.strip()

        if token.isdigit():
            return int(token)

        if token.startswith('"') and token.endswith('"'):
            return token.strip('"')

        return variables[token]

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if line.startswith("let "):
            parts = line[4:].split("=", 1)

            name = parts[0].strip()
            value = parts[1].strip()

            if value.isdigit():
                value = int(value)
            else:
                value = value.strip('"')

            variables[name] = value

        elif line.startswith("if "):
            condition = line[3:].strip()

            if ">" in condition:
                left, right = condition.split(">", 1)

                left = left.strip()
                right = right.strip()

                if get_value(left) > get_value(right):
                    print("Condition is TRUE")

        elif line.startswith("print("):
            content = line[6:-1].strip()

            if "+" in content:
                left, right = content.split("+", 1)

                left = left.strip()
                right = right.strip()

                print(get_value(left) + get_value(right))

            elif "-" in content:
                left, right = content.split("-", 1)

                left = left.strip()
                right = right.strip()

                print(get_value(left) - get_value(right))

            elif "*" in content:
                left, right = content.split("*", 1)

                left = left.strip()
                right = right.strip()

                print(get_value(left) * get_value(right))

            elif "/" in content:
                left, right = content.split("/", 1)

                left = left.strip()
                right = right.strip()

                print(get_value(left) / get_value(right))

            elif content in variables:
                print(variables[content])

            else:
                print(content.strip('"'))

def execute(ast, variables):

    if ast["type"] == "let":

        value = ast["value"]

        if value.isdigit():
            value = int(value)

        variables[ast["name"]] = value

        print("Stored:", ast["name"], "=", value)

    elif ast["type"] == "print":

        expression = ast["expression"]

        if isinstance(expression, str):

            if expression.isdigit():
                print(int(expression))

            elif expression in variables:
                print(variables[expression])

            else:
                print(expression)

        elif expression["type"] == "add":

            left = expression["left"]
            right = expression["right"]

            left_value = variables.get(left, left)
            right_value = variables.get(right, right)

            if str(left_value).isdigit():
                left_value = int(left_value)

            if str(right_value).isdigit():
                right_value = int(right_value)

            print(left_value + right_value)