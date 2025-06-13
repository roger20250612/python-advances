"""Decorator"""
import sys
import time
from functools import wraps

############################################################
# Demo 04 - Logging to file "tuto-02-decorator-logged.txt"
file_output_path = "./tuto-02-decorator-logged.txt"
def logged(my_function_args):
    @wraps(my_function_args)  # Để giữ thông tin hàm gốc (tên, docstring), bạn nên thêm functools.wraps vào các decorator
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print("Applying decorator with arguments...")
        res = my_function_args(*args, **kwargs)
        duration = f"Duration to finish the function {my_function_args.__name__} is: {time.time()-start_time:.2f}(seconds)."
        with open(file_output_path, mode="a", encoding="utf8") as f:
            f.write(duration + "\n")
        return res
    return wrapper

def duration2(my_function_args):
    @wraps(my_function_args)  # Để giữ thông tin hàm gốc (tên, docstring), bạn nên thêm functools.wraps vào các decorator
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = my_function_args(*args, **kwargs)
        print(f"Duration to finish the function {my_function_args.__name__} is: {time.time()-start_time:.2f}(seconds).")
        return res
    return wrapper

@duration2
@logged
def get_list_numbers(n):
    s = 0
    for i in range(1, n):
        s += 2**i
    return s

get_list_numbers(90000)
sys.exit(0)
# In log file: Duration to finish the function get_list_numbers is: 7.96(seconds).

# In terminal:
# $ python tuto-02-decorator.py
# Applying decorator with arguments...
# Duration to finish the function wrapper is: 7.96(seconds).

# Chú ý thứ tự: @duration bên ngoài để in ra console, @logged bên trong để ghi vào file — cả hai decorator sẽ thực thi đúng logic.

# Để giữ thông tin hàm gốc (tên, docstring), bạn nên thêm functools.wraps vào các decorator.
# Neu khong dung functools.wraps thi se hien thi sai thong tin ten ham
############################################################
# Demo 03 - Duration of performance
def duration(my_function_args):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = my_function_args(*args, **kwargs)
        print(f"Duration to finish the function {my_function_args.__name__} is: {time.time()-start_time:.2f}(seconds).")
        return res
    return wrapper

@duration
def get_list_numbers(n):
    s = 0
    for i in range(1, n):
        s += 2**i
    return s

get_list_numbers(9000)
sys.exit(0)
# $ python tuto-02-decorator.py
# Duration to finish the function get_list_numbers is: 0.07(seconds).

############################################################
# Demo 02 - Given arguments
def my_decorator_args(my_function_args):
    def wrapper(*args, **kwargs):
        print("Applying decorator with given arguments...")
        return my_function_args(*args, **kwargs)
    return wrapper

@my_decorator_args
def hello_person(name, class_name):
    return f"Hello {name} in class {class_name}"

print(hello_person("Peter", "CM2"))
sys.exit(0)
# $ python tuto-02-decorator.py
# Applying decorator with given arguments...
# Hello Peter in class CM2

############################################################
# Demo 01 - No arguments
def my_decorator(my_function):
    def wrapper():
        print("Applying decorator ...")
        my_function()
    return wrapper

def hello_world():
    print("Hello world")

my_decorator(hello_world)()
# $ python tuto-02-decorator.py
# Applying decorator ...
# Hello world