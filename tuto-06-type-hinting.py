"""Type Hinting"""

def get_addition_10(x: int) -> int:
    return x + 10

def get_multication_2(x: int) -> int:
    return x * 2

def print_data(x: str) -> None:
    print(f"Value of x = {x}")

x = get_multication_2(get_addition_10(5))
# print_data(x)

# Sử dụng công cụ kiểm tra như mypy trong việc bắt lỗi sớm.
# $ mypy tuto-06-type-hinting.py
# tuto-06-type-hinting.py:13: error: Argument 1 to "print_data" has incompatible type "int"; expected "str"  [arg-type]
# Found 1 error in 1 file (checked 1 source file)

print_data(str(x))
# $ mypy tuto-06-type-hinting.py
# Success: no issues found in 1 source file

# $ python tuto-06-type-hinting.py
# Value of x = 30

# $ mypy tuto-06-type-hinting.py
# Command 'mypy' not found, but can be installed with:
# sudo apt install mypy
