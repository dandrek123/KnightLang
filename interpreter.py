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

def evaluate(node, variables):

    if isinstance(node, str):

        if node.isdigit():
            return int(node)

        return variables[node]

    if node["type"] == "add":

        left = evaluate(node["left"], variables)

        right = evaluate(node["right"], variables)

        return left + right

def execute(ast, variables):

    if ast["type"] == "let":

        value = ast["value"]

        if value.isdigit():
            value = int(value)

        variables[ast["name"]] = value

        print("Stored:", ast["name"], "=", value)

    elif ast["type"] == "print":

        result = evaluate(ast["expression"], variables)

        print(result)