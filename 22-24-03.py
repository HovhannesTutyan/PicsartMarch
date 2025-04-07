# 1) Write a function print_down_from_n(n) that prints numbers from n to 1 using recursion.
def print_down_from_n(n):
    if not n:
        return 0
    if n < 0:
        print(n)
        return print_down_from_n(n+1)
    else:
        print(n)
        return print_down_from_n(n-1)
    
print(print_down_from_n(5))

# 2) Write a function print_characters(s) that prints each character of a string on a new line using recursion.
def print_characters(s):
    if not s:
        return 0
    print(s[0])
    return print_characters(s[1:])
print_characters('hello')

# Task 1: Calculate Factorial
def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n-1)
print(factorial(4))

# Task 2: Sum of Natural Numbers
def sum_natural(n):
    if n <= 0:
        return 0
    return n + sum_natural(n-1)
print(sum_natural(3))

# Task 3: Fibonacci Sequence
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1: 
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))

# Task 4: Reverse a String
def reverse_string(s):
    if len(s) < 1:
        return s
    return (s[-1] + reverse_string(s[:-1]))
print(reverse_string('hello world'))

# Task 5: Palindrome Check
def is_palindrom(s):
    if len(s) < 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrom(s[1:-1])
print(is_palindrom('racecar'))

# Task 6: Power of a Number
def power_of_n(x,n):
    if n == 0:
        return 1
    if n < 0:
        return 1 /  power_of_n(x, -n)
    else:
        return x * power_of_n(x, n-1)
print(power_of_n(-3,-2))

# Task 7: Sum of Digits
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)
print(sum_of_digits(3234))


# Task 9: Binary Search (recursive and after iterative)
def binary_search_rec(arr, low, high, numb):
    if high >= low:
        mid = (low + high) // 2
        if arr[mid] == numb:
            return mid
        elif arr[mid] < numb:
            return binary_search_rec(arr, mid + 1, high, numb)
        else:
            return binary_search_rec(arr, low, mid - 1, numb)
    else: 
        return -1
    
def binary_search(arr, numb):
    low = 0
    high = len(arr) - 1
    while high >= low:
        mid = (low + high) // 2
        if arr[mid] < numb:
            low = mid + 1
        elif arr[mid] > numb:
            high = mid - 1
        else:
            return mid
    return -1
        
arr_bin_search = [23,34,45,56,67,78,89]
print(binary_search(arr_bin_search, 78))


# Task 12: Flatten a Nested List
def flatten_tree(L):
    if len(L) == 0:
        return 0
    tree = []
    for x in L:
        if not isinstance(x, list):
            tree.append(x)
        else:
            tree += flatten_tree(x)
    return tree

L = [1, [2, [3, 4], 5], 6, [7, 8]]  
print(flatten_tree(L))

# Task 13: Find the Maximum Element in a List
