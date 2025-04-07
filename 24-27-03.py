import typing
# 1. Implementing filter

def is_even(x):
    return x % 2 == 0

numbers = [x for x in range(1,16)]
def cutom_filter(func, iterable):
    if func is None:
        func = lambda y: y
    elif not isinstance(func, typing.Callable):
        raise TypeError("Not a function")
    if len(iterable) < 1:
        return iterable
    temp = []
    for x in iterable:
        if func(x):
            temp.append(x)
    return temp
print(cutom_filter(func=None, iterable=numbers))

# 2. Implementing map
def add3(*args):
    return sum(args)

def custom_map(func, *iterables):
    min_len = len(min(iterables, key=lambda x: len(x)))
    res = []
    for i in range(min_len):
        temp = []
        for x in iterables:
            temp.append(x[i])
        res.append(func(*temp))
    return res
z = custom_map(add3,[5,6,4,5,6,7,8],[3,4,5,6])
print(list(z))

# 3. Implementing zip

def custom_zip(*iterables):
    min_len = len(min(iterables, key=lambda x: len(x)))
    temp = []
    for i in range(min_len):
        temp_tuple = []
        for key in iterables:
            temp_tuple.append(key[i])
        temp.append(temp_tuple)
    return temp

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e', 'f']
print(custom_zip(list1, list2))

# 4. Implementing reduce

from functools import reduce

def add1(x, y):
    return x + y
numbers1 = [1,2,3,4,5,6,7]

def custom_reduce1(func, iterable, init=None):
    it = iter(iterable)
    if init is None:
        value = next(it)
    else:
        value = init
    for element in it:
        value = func(value, element)
    return value
print(custom_reduce1(add1, numbers1))

# 5. Implementing enumerate

def custom_enumerate(iterable, start = 0):
    temp = []
    for i in range(start, len(iterable)):
        tempTuple = (i, iterable[i])
        temp.append(tempTuple)
    return temp

print(custom_enumerate(numbers, start=0))
