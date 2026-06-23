# KnightLang

KnightLang is a custom interpreted programming language built from scratch in Python.

## Current Features

- Variables
- Integers
- Strings
- Arithmetic operations (+, -, *, /)
- Operator precedence
- Parentheses for grouped expressions
- Lists / arrays
- List indexing
- String concatenation
- Assignment statements
- Comparison operators (>, <, >=, <=, ==, !=)
- Conditional execution with if/else
- While loops
- Functions
- Function parameters
- Return values
- Indentation-based block execution
- Lexer
- Parser
- Abstract Syntax Tree (AST)
- Recursive expression evaluation
- Interpreter execution engine
- Built-in `len()` function
- Cleaner runtime error handling

## Example

```
let name = "DAndre"

print("Hello " + name)
```

```
let count = 0

while count < 5
    print(count)
    count = count + 1
```

```
func greet
    print("Hello from KnightLang")

greet()
```

```
print((2 + 3) * 4)
print(2 + 3 * 4)
```

```
let numbers = [10, 20, 30]

print(numbers[0])
print(len(numbers))
```

## Roadmap

- Better error messages with line numbers
- Boolean values (`true` / `false`)
- Logical operators (`and`, `or`, `not`)
- List methods such as `append()` and `remove()`
- For loops
- Comments
- Standard library functions
- File input/output
- Python transpiler
- Bit assistant integration
