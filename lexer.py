def tokenize(line):
    tokens = []
    current = ""

    for char in line:

        if char in " ()=+-*/><":

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