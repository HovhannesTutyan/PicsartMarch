# 1) Write a function sum_numbers that accepts an arbitrary number of positional arguments and returns their sum.
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(65,41,27))
print(sum_numbers())

# 2) Write a function display_student_info that accepts any number of keyword arguments and prints them in the format: key: value.
def display_student_info(**kwargs):
    print(kwargs)
display_student_info(name='Alice', age=20, major='CS')

# 3) Write a function order_item that accepts:
def order_item(req, *args, quan=1, **kwargs):
    print(req, quan, args, kwargs)
order_item(12, 65, 41,27, quan=34, name="James", job="CS")

# 4) Write a function register_user that accepts:
def register_user(username, *, email):
    print(username, email)
register_user("johnSnow", email="a@a.com")

# 5) Analyze the following code, explain why it raises an error, and fix the function call: 
# here the extras are taken as keyword arguments, and printed in details.
def book_ticket(destination, price, discount=0, *extras, **details):
    print(f"Booking to {destination} for ${price - discount}")
    print('destination', destination, 'price', price, 'discount', discount, 'extras', extras, 'details', details)
    if extras:
        print(f"Extras: {', '.join(extras)}")
    if details:
        print(f"Details: {details} ")
book_ticket("Paris", 100, 10, "Window seat", "meal")

# 6) Implement a function process_data that accepts a mix of positional arguments, default arguments, arbitrary positional arguments (*args), and arbitrary keyword arguments (**kwargs).
def process_data(operation, data=[], freshold = None, *args, **kwargs):
    for x in args:
        data.append(x)
    if operation == 'sum':
        return sum(data)
    elif operation == 'multiply':
        base = 1
        for x in data:
            base *= x
        return base
    elif operation == 'filter':
        if freshold == 'None':
            return data
        reversed = kwargs['reverse']
        unique = kwargs['unique']
        orig_list = [x for x in data if x > freshold]
        if reversed == True and unique == False:
            return reverse_list(orig_list)
        elif unique == True and reversed == False:
           return make_unique(orig_list)
        elif unique and reversed:
            un_list = make_unique(orig_list)
            rev_list = reverse_list(un_list)
            return rev_list
        else:
            return orig_list
    else:
        print("Not correct selection")
def reverse_list(random_list):
    rev_list = []
    for i in range(1, len(random_list)+1):
        rev_list.append(random_list[-i])
    return rev_list
def make_unique(dupl_list):
    unique_list = []
    for x in dupl_list:
        if x in unique_list:
            continue
        unique_list.append(x)
    return unique_list

print(process_data('filter', [], 4, 5,7,8,9,9,12,3,4, 2, reverse=False, unique=False))

# 7) Write a closure that creates a counter. Each call to the inner function should increment the counter by 1 and return the current count.
def tester(start):
    global state
    state = start
    def inner():
        global state
        state += 1
        print(state)
    return inner
f = tester(0)
f()
f()

# 8) Create a closure that takes a multiplier as an argument and returns a function that multiplies any given number by that multiplier.
def wrapper(mult):
    def inner(number):
        nonlocal mult
        return mult * number
    return inner
w = wrapper(5)
print(w(7))

# 9) Write a closure that tracks the number of times a specific function is called.
def func_tracker(func):
    c = 0
    def inner(*args, **kwargs):
        nonlocal c
        c += 1
        print(c)
        return func(*args, **kwargs)
    return inner
z = func_tracker(sum)
z([4,5])
z([2,3])
z([2,3])
z([2,3])


