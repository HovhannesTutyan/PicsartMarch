# 1. Write a program to identify all prime numbers between 1 and 100 using list comprehensions.

def is_prime(nums):
    arr = []
    for x in nums:
        for j in range(2, int(x ** 0.5)+1):
            if x % j == 0:
                break
        else:
            arr.append(x)
    return arr

print(is_prime([2,3,4,5,6, 7, 8, 9, 11, 13]))

def is_prime_list(nums):
    # return [x for x in nums for j in range(2, int(x ** 0.5)+1) if x % j != 0]
    return [x for x in nums if all (x % j != 0 for j in range(2, int(x ** 0.5) + 1))]
print(is_prime_list([2,3,4,5,6, 7, 8, 9, 11, 12, 13]))

# 2 Using a list comprehension, create a new list from [1, 2, 3, -4, -5, 6] that contains only the positive numbers.
z_list = [1, 2, 3, -4, -5, 6]
new_list = [x for x in z_list if x > 0]
print(new_list)

# 3 Write a program that categorizes numbers in a list as "Even", "Odd", or "Prime" using if-elif inside a loop.
def categorize(nums):
    odd_list = []
    even_list= []
    prime_list = is_prime_list(nums)
    for num in nums:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    return (odd_list, even_list, prime_list)

n_list = [2,3,4,5,6,7,8,9]
print(categorize(n_list))

# 4 Create a nested list comprehension to generate a multiplication table (1-10).
def multip_table_iter(num):
    i = 1
    while i <= 10:
        print(f"{i} * {num} = {i * num}")
        i += 1
# multip_table_iter(12)

def multip_table_compr(num):
    print([num * j for j  in range(1, 10)])
multip_table_compr(5)

# 5 Write a program to filter and print words from a list of strings that start with vowels using list comprehension.

def vowels_filter(letters):
    vowels = ['a', 'o', 'u', 'e', 'i', 'y']
    return [x for x in letters if x[0] in vowels]

words = ['this', 'is', 'a', 'long', 'string', 'ahead', 'of', 'elements', ' ']
print(vowels_filter(words))

# 6. Write a function calculate_average that takes any number of numerical arguments and returns their average.
def calculate_average(*nums):
    total = 0
    for num in nums:
        total += num
    avg = total / len(nums)
    return avg

print(f"The average of numbers is {calculate_average(2,3,4,5,6,7)}")

# 7. Implement a function reverse_string that accepts a string and returns it reversed without using built-in methods.
def reverse_string(string):
    rev_list = ""
    for i in range(1, len(string)+1):
        rev_list += string[-i]
    return rev_list

print(reverse_string("hello James, how are you"))

# 8 Write a function personal_greeting that takes a required name argument and an optional greeting argument. The default greeting should be "Hi".
def personal_greeting(name, greeting="Hi"):
    print(f"{name} says {greeting}")

personal_greeting('Jack')
personal_greeting('James', greeting="Good moring")

# 9 Create a function all_greater that takes a list and a number as arguments and checks if all elements in the list are greater than the number.
def all_greater(iter, num):
    flag = True
    for item in iter:
        if item < num:
            flag = False
            break
    return flag

def all_greater_compr(iter, num):
    return [all(x> num for x in iter)]
print(all_greater_compr([18,13,14,12,16,17], 9))
print(all_greater([18,13,14,12,16,17], 9))

# 10 Write a function divide_numbers that accepts two numbers and returns their division result. Add error handling for division by zero.
def devide_number(numerator, denominator):
    if denominator == 0:
        print("Devision to 0 is forbidden")
        return -1
    return numerator / denominator
print(devide_number(2, 0))

# 11 Implement custom_enumerate using yield, similar to the Python built-in enumerate.
def custom_enumerate(arr):
    for i in range(len(arr)):
       yield (i, arr[i])

arr_list = (custom_enumerate([65,54,34,23,23]))
print(next(arr_list))
print(next(arr_list))

# 12 Write a generator function range_generator that mimics the behavior of range(start, stop, step) using yield.
def range_generator(arr, start, stop, step):
    while start <= stop:
        yield arr[start:start+step]
        start += step

range_gen = range_generator([65,41,27,77,78,89,90,91], 1, 8, 3)
print(next(range_gen))
print(next(range_gen))
print(next(range_gen))

# 13 Create a function custom_map_with_yield that applies a transformation to elements of an iterable and yields each result.
def add2(*x):
    return sum(x)

def custom_map_with_iter(func, *iter):
    min_len = min([len(x) for x in iter])
    temp = []
    for i in range(min_len):
        temp_arr = []
        for j in iter:
            temp_arr.append(j[i])
        temp.append(func(*temp_arr)) 
    return temp

def custom_map_with_yield(func, *iter):
    min_len = min([len(x) for x in iter])
    for i in range(min_len):
        temp_arr = []
        for j in iter:
            temp_arr.append(j[i])
        yield(func(*temp_arr))

# print(custom_map_with_iter(add2, [2,3], [3,4,5]))
cmwy = (custom_map_with_yield(add2, [2,3],[3,4,5]))
print(next(cmwy))
print(next(cmwy))

# 14 Implement custom_filter_with_yield that yields items from an iterable that satisfy a given condition.

def is_even(num):
    return num % 2 == 0

def custom_filter_iter(func, iter):
    temp = []
    for i in iter:
        if func(i):
            temp.append(i)
    return temp
def custom_filter_yield(func, iter):
    for i in iter:
        if func(i):
            yield(i)
# print(list(custom_filter_iter(is_even, [3,4,5,6,7,8,9])))
cfy = custom_filter_yield(is_even, [4,5,6,7,8,9])
print(next(cfy))
print(next(cfy))
print(next(cfy))

# 15 Write a zip_generator that takes multiple iterables and yields tuples, similar to Python’s zip.

def custom_zip_iter(*iter):
    min_len = min([len(x) for x in iter])
    arr = []
    for i in range(min_len):
        temp = []
        for j in iter:
            temp.append(j[i])
        arr.append(temp)
    return arr
        
# print(custom_zip_iter([2,3,4,5], [6,7,8,9]))

def custom_zip_gen(*iter):
    min_len = min([len(x) for x in iter])
    for i in range(min_len):
        for j in iter:
            yield j[i]

czg = custom_zip_iter([2,3,4,5], [6,7,8,9,10])
print("czg", czg)

# 16 Write a closure that creates a counter. Each call to the inner function should increment the counter by 1 and return the current count.
def wrapper(counter):
    def inner():
        nonlocal counter
        counter += 1
        return counter
    return inner

i1 = wrapper(1)
print(i1())
print(i1())

# 17 Create a closure that takes a multiplier as an argument and returns a function that multiplies any given number by that multiplier.
def wrapper2(x):
    def inner2(y):
        return x * y
    return inner2
i2 = wrapper2(4)
print(i2(5))

# 18 Write a closure that tracks the number of times a specific function is called.
def wrapper3(counter):
    def inner3(func, args):
        nonlocal counter
        result = func(args)
        counter += 1
        return (result, counter)
    return inner3
i3 = wrapper3(1)
print(i3(lambda x: x ** 2, 4))
print(i3(lambda x: x ** 2, 4))

# 19 Implement a closure that takes a string as input and allows appending to or resetting the string when the inner function is called.
def wrapper4(string):
    def inner4(modifier):
        nonlocal string
        string += modifier
        return string
    return inner4

# 20 find vowels in string
def find_vowels(words, vowels):
    temp = {}
    for word in words:
        count = 0
        for letter in word:
            if letter in vowels:
                count += 1
                temp[word] = count
    return (temp,count)

vow = ['a', 'e', 'i', 'o', 'u']
wor= ['administration', 'decrease', 'demonstration', 'intelligence', 'temporary']
print("find_vowels(wor, vow)",find_vowels(wor, vow))