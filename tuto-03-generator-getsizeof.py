"""Generator"""
def my_generator(n):
    for x in range(1, n):
        yield 2**x

values = my_generator(100)

print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))

import sys
print(f"Size of generator: {sys.getsizeof(values)}")  # No changing

# Output in terminal:
# 2
# 4
# 8
# Size of generator: 208