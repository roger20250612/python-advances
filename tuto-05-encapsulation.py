"""Encapsulation - mô phỏng tính encapsulation (đóng gói) trong OOP

Bundling data (attributes) and methods (functions) into a single unit (class).
Hiding internal state and requiring all interaction through methods.
Access modifiers in Python:
    public (default): accessible from anywhere.
    protected (_name): meant for internal use only (convention).
    private (__name): name mangling to prevent direct access.
"""

class Person:
    def __init__(self, name, age=0):  # Thêm giá trị mặc định cho age
        self.__name = name if isinstance(name, str) else "Default Name"
        self.__age = age if isinstance(age, int) else 0

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            print(f"Cannot set name based on value: {value}; with type: {type(value)}. Only support string for name")
            self.__name = "Default Name"

    def __repr__(self):
        return f"Person(name={self.__name}, age={self.__age})"

    @staticmethod
    def print_data():
        print("Called static method")

# Call static method
Person.print_data()

p = Person("Peter", 36)
p.print_data()
print(p)

p2 = Person("Bob")
print(p2)

p2.Name = 12345   # Sẽ in thông báo loi và gán lại thành "Default Name"
print(p2)

# Sau khi cap nhat code tren:
# $ python tuto-05-encapsulation.py
# Called static method
# Called static method
# Person(name=Peter, age=36)
# Person(name=Bob, age=0)
# Cannot set name based on value: 12345; with type: <class 'int'>. Only support string for name
# Person(name=Default Name, age=0)

# $ python tuto-05-encapsulation.py
# Called static method
# Called static method
# Person(name=Peter, age=36)
# Traceback (most recent call last):
#   File "/home/lavie/dev/work/hoc_them/python-advances/tuto-05-encapsulation.py", line 33, in <module>
#     p2 = Person("Bob")
#          ^^^^^^^^^^^^^
# TypeError: Person.__init__() missing 1 required positional argument: 'age'
