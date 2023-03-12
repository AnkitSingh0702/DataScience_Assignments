# Type annotations in Python are a way of adding explicit type information to function and variable declarations. Type annotations are optional, and Python will still allow you to write code without them, but they can provide additional information to tools like IDEs and linters, and make it easier to catch certain types of bugs.

def add(x: int, y: int) -> int:
    return x + y

new_val: int = add(7, 4)
print(new_val)
