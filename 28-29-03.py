# 1. Simple Number Sequence Generator

def simple_sequence(start, end):
    if end < start:
        start, end = end, start
    elif start == end:
        yield start
    for x in range(start, end):
        yield x
gen_simple = simple_sequence(10, 18)
print(next(gen_simple))


# 2. Countdown Generator with Print Statements
def countdown(n):
    temp = n
    for x in range(n):
        temp -= 1
        yield temp

cdown = countdown(5)
print(f"Yielding x - {next(cdown)}")
print(f"Yielding x - {next(cdown)}")
print(f"Yielding x - {next(cdown)}")

# 3. Generator Expression for Data Transformation
numbers = list(range(1, 11))
squares_list = [x ** 2 for x in numbers]
print(f"Squares list - {squares_list}")
def square_gen(n):
    for x in n:
        yield x ** 2
sq_gen = square_gen(numbers)
print(next(sq_gen))
print(next(sq_gen))
for x in sq_gen:
    print(x)


# 4. Fibonacci Generator (Intermediate)
def fib_gen(limit=None): 
    a, b = 0, 1
    for i in range(5):
        yield b
        a, b = b, a + b

fib = fib_gen(limit=10)
for x in fib:
    print(x)

# 6. Even Numbers Generator
def even_numbers(nums):
    for num in nums:
        if num % 2 == 0:
            yield num

numbers_list = [1, 2, 3, 4, 5, 10, 11, 14]
n = even_numbers(numbers_list)
# print(next(n))
# print(next(n))
for even in even_numbers(numbers_list):
    print(even)

 
# 7. Cumulative Sum Generator

def cumulative_sum(nums):
    total = 0
    for x in nums:
        total += x
        print(f"({total - x}+ {x}) = {total}")
        yield total
numbers = [1,3,5,7]
for partial_sum in cumulative_sum(numbers):
    print(partial_sum)

