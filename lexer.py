def tokenize(line):
    tokens = []
    current = ""
    in_string = False

    for char in line:

        if char == '"':
            current += char

            if in_string:
                tokens.append(current)
                current = ""
                in_string = False
            else:
                in_string = True

        elif in_string:
            current += char

        elif char in " ()=+-*/><":

            if current:
                tokens.append(current)
                current = ""

            if char != " ":
                tokens.append(char)

        else:
            current += char

    if current:
        tokens.append(current)

    return tokens