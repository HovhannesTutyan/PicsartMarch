import functools
import inspect
# calls = 0 
# def tracer(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         global calls
#         calls += 1
#         return (func(*args, **kwargs), calls)
#     return wrapper

# @tracer # spam = tracer(spam)
# def spam(a,b,c):
#     return a + b + c

# @tracer 
# def eggs(x,y):
#     return x ** y

# print(spam(1,2,3))
# print(spam(a = 4, b = 5, c = 6))

# 1. Write a decorator greet_decorator that adds a greeting message before and after the execution of the decorated function.
def greet_decorator(func):
    @functools.wraps(func)
    def inner(message1, message2):
        print(message1)
        func()
        print(message2)
    return inner

@greet_decorator
def say_name():
    print("My name is python")

say_name("hello", "buy")

# 2. Create a decorator log_execution that logs the name of the function being executed along with its arguments and return value.
def log_execution(func):
    @functools.wraps(func)
    def inner():
        print(f"{inner.__name__} is being executed, the arguments are ")
        print(inspect.signature(func))
    return inner

@log_execution
def add(x, y):
    return x + y

@log_execution
def subtract(x, y):
    return x - y

add()
subtract()

# 3 Write a decorator execution_timer that measures and prints the time taken by the decorated function to execute.
import time 

def execution_timer(func):
    @functools.wraps(func)
    def inner(seconds):
        t0 = time.perf_counter()
        func(seconds)
        elapsed = time.perf_counter() - t0
        print(f"{inner.__name__} took {elapsed:.4f} seconds to finish")
    return inner 

@execution_timer
def slow_function(seconds):
    time.sleep(seconds)
    print("Finished Execution")

slow_function(2)

# 4 Create a decorator require_login that only allows a function to execute if a global variable is_logged_in is True. If not, raise an exception.
def require_login(func):
    def decorate(is_login=False):
        return func(is_login)
    return decorate

@require_login
def view_profile(is_login):
    if is_login:
        print("Accessing your profile")
    else:
        print("Raise exception for not logged in")

view_profile(is_login=True)