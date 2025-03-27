def fibonaccy(n):
    if n < 1:
        return 1
    i = 2
    a, b = 0, 1
    while i <= n:
        a, b = b, a + b
        i += 1
    return b

print(fibonaccy(8))

def factorial(n):
    if n < 1:
        return 1
    i = 1
    a = 1
    while i < n:
        a *= i
        i += 1
    return a

print(factorial(7))

def is_prime(n):
    if n < 1:
        return 1
    i = 2
    while i < n/2:
        if n % i == 0:
            return False
        i += 1
    return True
print(is_prime(7)) 

def reverse_string(s):
    myStr = ''
    for i in range(1, len(s)+1):
        myStr += s[-i]
    return myStr

print(reverse_string('hello buy there is me'))

def sum_of_digits(n):
    mySum = 0
    while n > 0:
        mySum += n % 10
        n = n // 10
    return mySum
print(sum_of_digits(3274))

def is_sum_of_prime(n):
    i = 2
    while i < n:
        if is_prime(i) and is_prime(n - i):
            return 0
        i += 1
    return 1
print(is_sum_of_prime(6))