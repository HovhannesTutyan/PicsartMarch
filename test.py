# def book_ticket(destination, price, discount=5, *extras, **details):
#     print(f"Booking to {destination} for ${price - discount}")
#     if extras:
#         print(f"Extras: {', '.join(extras)}")
#     if details:
#         print(f"Details: {details}")

# book_ticket("Paris", 100, 10, "")

# data = [2,3,3,4,5]
# l = []
# for x in data:
#     if x in l:
#         continue
#     l.append(x)
# print(l)

# def make_unique(dupl_list):
#     unique_list = []
#     for x in dupl_list:
#         if x in unique_list:
#             continue
#         unique_list.append(x)
#     return unique_list

# def reverse_list(random_list):
#     rev_list = []
#     for i in range(1, len(random_list)+1):
#         rev_list.append(random_list[-i])
#     return rev_list

# u = [2,3,4,5,5,6,6,7]
# rev = reverse_list(u)
# print(make_unique(rev))

# y = 5
# def tester(start):
#     x = start
#     def inner():
#         global y
#         y+= x
#         return(y)
#     return inner
# a = tester(1)
# print(y)
# print(a())

# def intersect(*args):
#     res = []
#     for x in args[0]:
#         print('args[0]', args[0])
#         print("args[1:]", args[1:])
#         if x in res:
#             continue
#         for other in args[1:]:
#             if x not in other:
#                 break
#             else:
#                 res.append(x)
#     return res

# print(intersect([65,41,27], (77, 52, 27), (4,5,6)))

def func(a, b, c=3, d=4):
    print(a,b,c,d)

func(1, *(4,5))

print((4,5))
print(pow(-3, -2))

# Task 7: Sum of Digits
def sum_of_digits(n):
    if n == 0:
        return 0
    i = 0
    number = 0
    sum = 0
    while i <= n:
        number = n % 10
        sum += number 
        n //= 10
        i += 1
    return sum
print(sum_of_digits(3234))

ls1 = [1,2]
ls2 = [2]
print(ls1 > ls2)

s1 = "hello"
s2 = "hello"
print(s1 is s2)
x = {}
print(type(x))

d = {0, 1, 2}
for i in range(1):
    print("i", i)

a,b,c, = "afd"
print(a,b,c)

x,y,*z,p = range(7)
print("x,y,z,p", x,y,z,p)

asd = [[1,2],3,4,5,6]
ad, *bd = asd
print(ad, bd)

print(asd[2:])

x = "python"
while x:
    print(x)
    x = x[1:]
res = ['v1', 'v2'][bool(x)]
print(res)

tp = ((1,2,3),(4,5,6),(7,8,9))
a,b,c = tp
print(a,b,c, end="|")

lls = ["hi", 7, 8]
lls1 = lls
lls1.append(9)
lls1 = lls1 + ["Buy"]

print(lls, lls1)
print(lls[1:])

def _inch9():
    print("hello") 
_inch9()

def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if variable in letters:
        return True
    else:
        return False
    
sequence = ['g', 'e', 'e', 'k', 'l', 'e', 'a', 'b', 'c']
filtered = filter(fun, sequence)
for s in filtered:
    print(s)

names = ['james', 'john', 'alice', 'adfsa']
ages = [3,4,5]
zipped = zip(names, list(enumerate(ages, ages[1])))
for (x,y) in zipped:
    print(x,y)

#####################################################
for x in range(5):
    if x % 2 != 0:
        for y in range(x):
            if y // 2 == 1:
                print("Bew y", y)

print([y for x in range(5) if x % 2 != 0 for y in range (x) if y // 2 == 1])

adsfadsf = "hell"
print(set(adsfadsf))

def foo():
    def inner():
        yield 5
    x = inner()
    return x

y = foo()
# print(next(y))

# def f(x):
#     yield x + 1
#     print("test")
#     yield x + 2

# g = f(9)
# print(g)
# print("next(g)", next(g))
# print("next(g)", next(g))
# # print("next(g)", next(g))

# def foo(size, * , flag):
#     print(size) if flag else None
# foo(1024, False)

# def foo():
#     for i in range(5):
#         yield i

# res = foo()
# # print(list(res))
# print(next(res))

# def gen_a():
#     num = 1
#     while True:
#         yield num

# print(next(gen_a()), next(gen_a()))

# def gen_a():
#     a = 5
#     while a:
#         yield a
#         a -= 1

# for b in gen_a():
#     print(b)

# def foo():
#     for i in range(5):
#         yield i + 1
#         print("hi")
# x = foo()
# print(next(x))
# print(next(x))

# def foo():
#     yield 1
#     return 25
# print(next(foo()))
# print(next(foo()))

# message = "hi"
# print([item1 + item2 for item1 in message for item2 in message[::-1]])
# # print([item1 for item1 in message[::-1]])

# ls = [pow(x,x) for x in range(5) if x % 2 == 0]
# print(ls)

# arr = []
# for x in range(5):
#     if x % 2 == 0:
#         arr.append(pow(x,x))
# print(arr)

# print(ord("h"))

# x = {x:y for x in [1,2,3] for y in [4,5,6]}
# print(x)

# def changing_dict(**kwargs):
#     kwargs['lists'][0][1] = 'muchacha'
#     print(kwargs)
# changing_dict(lists=[[1] * 2] * 3)
# print(changing_dict)

# print([[1]*2]*3)

# def outer(N):
#    for i in range(4):
#       yield lambda X : X * N
# result = outer(5)
# for foo in result:
#    print(foo(3))

# def find_dupl(numb):
#     temp = []
#     for x in numb:
#         if numb.count(x) == 1:
#             temp.append(x)
#     return temp
# print(find_dupl([2,3,4,5,6,5,4]))

# def gen_n(n):
#     for i in range(1, n):
#         if i % 3 == 0:
#             yield i

# gn = gen_n(9)
# print(next(gn))

# def find_target(nums, target):
#     dupl_list = []
#     for i, x in enumerate(nums):
#         if target - x in nums:
#             dupl_list.append(i)
#     return dupl_list

# num = [2,7,11,15]
# targ = 9
# print(find_target(num, targ))

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

                