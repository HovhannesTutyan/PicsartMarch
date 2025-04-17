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

import typing
def custom_reduce(func, iter, init=None):
    if not isinstance(iter, typing.Iterable):
        raise TypeError("Give me an iterable")
    if not callable(func):
        raise TypeError("Give me callable")
    if init == None:
        raise TypeError("Give me initilazer")
    if init != None:
        res1 = init
        start = 0
    else: 
        res1 = iter[0]
    for i in range(start, len(iter)):
        res1 = func(res1, iter[i])
    return res1 

ls = [1,2,3,4,5]
print(custom_reduce(lambda x,y:x+y,ls, init=0))

# 5. Implementing enumerate

def custom_enumerate(iterable, start = 0):
    temp = []
    for i in range(start, len(iterable)):
        tempTuple = (i, iterable[i])
        temp.append(tempTuple)
    return temp

print(custom_enumerate(numbers, start=0))
