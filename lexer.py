def tokenize(line):
    tokens = []
    current = ""
    in_string = False

    i = 0

    while i < len(line):

        char = line[i]

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

        elif i + 1 < len(line) and line[i:i+2] in ["==", "!=", ">=", "<="]:

            if current:
                tokens.append(current)
                current = ""

            tokens.append(line[i:i+2])

            i += 1

        elif char in " (),[]=+-*/><":

            if current:
                tokens.append(current)
                current = ""

            if char != " ":
                tokens.append(char)

        else:
            current += char

        i += 1

    if current:
        tokens.append(current)

    return tokens