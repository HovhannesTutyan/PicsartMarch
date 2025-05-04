# myDict = {}
# myList = [65, 41, 27, 52, 34, "hello", 45.67, 67.89, "James", "hello", 41, 52]
# for i in myList:
#     if i not in myDict:
#         myDict[i] = 1
#     else:
#         myDict[i] += 1
# print(myDict)
# print(f"the occurance of 41 is {myList.count(41)}")
##############Reverse a number###########################
# myNumb = 923456
# firstDigit = myNumb % 10
# revNumb = 0
# while myNumb > 0:
#     lastDig = myNumb % 10
#     revNumb = revNumb * 10 + lastDig
#     myNumb //= 10
# print(revNumb)
# lastDig = revNumb % 10
# print(firstDigit, lastDig)

# i = 10
# mySum = 0
# while i > 0:
#     j = int(input('enter a number'))
#     if j == 0:
#         print("enter a different number")
#     mySum += j
#     print(mySum)
#     i -= 1


# myList = [6555,3,2,43999,45,56,67,3,599]
# ind = 0
# it = iter(myList)
# maxNumb = next(it)
# for i, j in enumerate(myList):
#     if j > maxNumb:
#         maxNumb = j
#         ind = i
# print(ind)

# dictStr = "the cat andddd the hate"
# ds = dictStr.split()
# myDict = {}
# for i in ds:
#     key = len(i)
#     if key not in myDict:
#         myDict[key] = [i]
#     else:
#         myDict[key].append(i)
# print(myDict)


# numbList1 = [65,41,27,77,52,37,89]
# numbList2 = [65,42,27,67,72,97,-89]
# for i in numbList1:
#     if i in numbList2:
#         print(i)
# set1 = set(numbList1)
# set2 = set(numbList2)
# print(set1.difference(set2))

# myNumb = 65412712341324
# count = 0
# rev = 0
# mySum = 0
# while myNumb > 0:
#     lastDig = myNumb % 10
#     mySum += lastDig
#     rev = rev * 10 + lastDig
#     myNumb //= 10
#     count += 1
# print(count)
# print(rev)
# print(mySum)

# def disp_st_inf(pos, *args, grade, age=20, **kwargs):
#     print(pos, args, age, kwargs, grade)
# disp_st_inf("positional","hello",  grade="hello", age=30, name="Alice")

# def outer(total = 0):
#     def inner(n = None):
#         if n is None:
#             return total
#         return outer(total + n)
#     return inner
# print(outer()(1)(2)(3)())

# def cb(numb):
#     bin_rep = ""
#     while numb > 0:
#         bin_rep = str(numb & 1) + bin_rep
#         numb = numb >> 1
#     return bin_rep
# print(cb(7))

# def add(x, y):
#     return x + y
# def outer(func):
#     count = 0
#     def inner(*args, **kwargs):
#         nonlocal count
#         count += 1
#         res = func(*args, **kwargs)
#         return (res, count)
#     return inner

# x = outer(add)
# print(x(3,5))
# print(x(12,5))

# def print_rec(n):
#     if not n:
#         return 0
#     if n < 0:
#         print(n)
#         return print_rec(n+1)
#     else:
#         print(n)
#         return print_rec(n-1)
# print(print_rec(5))

# def print_char(s):
#     if not s:
#         return 0
#     print(s[0])
#     return print_char(s[1:])
# print_char('hello')

# def fact(n):
#     if n < 1:
#         return 1
#     return n * fact(n-1)

# print(fact(5))


# def is_palindrom(myStr):
#     left = 0
#     right = len(myStr) - 1
#     while left <= right:
#         if myStr[left] != myStr[right]:
#             return False
#         left += 1
#         right -= 1 
#     return True
# print(is_palindrom("racecar"))

# def is_pal_rec(myStr):
#     if len(myStr) < 1:
#         return True
#     if myStr[0] != myStr[-1]:
#         return False
#     return is_pal_rec(myStr[1:-1])
# print(is_pal_rec("racecadsfar"))

# def sum_rec(numb):
#     if numb == 0:
#         return 0
#     return numb % 10 + sum_rec(numb // 10)

# print(sum_rec(25))
    
# def bin_search(myArr, numb):
#     low = 0
#     high = len(myArr) - 1
#     while high >= low:
#         med = (low + high) // 2
#         if myArr[med] < numb:
#             low = med + 1
#         elif myArr[med] > numb:
#             high = med - 1
#         else:
#             return med
#     return -1
# print(bin_search([65,41,27,33,18],18))

# def bin_search_rec(myArr, numb, low, high):
#     if high >= low:
#         med = (low + high) // 2
#         if myArr[med] == numb:
#             return numb
#         if myArr[med] < numb:
#             return bin_search_rec(myArr, numb, med+1, high)
#         else:
#             return bin_search_rec(myArr, numb, low, med - 1)
#     return -1
# print(bin_search([65,41,27,33,18,29],18))


# def flatten_tree(myArr):
#     if len(myArr) == 0:
#         return 0
#     tree = []
#     for i in myArr:
#         if not isinstance(i, list):
#             tree.append(i)
#         else:
#             tree += flatten_tree(i)
#     return tree

# myArr = [1, [2, [3, 4], 5], 6, [7, 8]]  
# print(flatten_tree(myArr))
import typing
# def ispos(x):
#     return x > 0
# def cust_filt(func, it):
#     if not isinstance(func, typing.Callable):
#         raise Exception("The function is not callable")
#     elif len(it) < 1:
#         return it
#     elif func is None:
#         return lambda y: y
#     temp = []
#     for i in it:
#         if func(i):
#             temp.append(i)
#     return temp
# print(cust_filt(None, [65,43,-10,5, -6]))

def add(x, y):
    return x + y

# def custom_map(func, *it):
#     min_len = min([len(x) for x in it])
#     res = []
#     for i in range(min_len):
#         temp = []
#         for j in it:
#             temp.append(j[i])
#         res.append(func(*temp))
#     return res
# x = custom_map(add, [2,3,4,5,6], [3,4,5])
# print(list(x))

# def custom_zip(*iterables):
#     min_len = min([len(x) for x in iterables])
#     res = []
#     for i in range(min_len):
#         temp = []
#         for j in iterables:
#             temp.append(j[i])
#         res.append(temp)
#     return res

# x = custom_zip([2,3,4], [5,6])
# print(list(x))

# def custom_reduce(func, it, init=None):
#     if init != None:
#         res1 = init
#         start = 0
#     else:
#         res1 = it[0]
#     for i in range(start, len(it)):
#         res1 = func(res1, it[i])
#     return res1

# print(custom_reduce(lambda x, y: x + y, [2,3,4,5,6] , init =2))

# def custom_enum(it, start=0):
#     temp = []
#     for i in range(start, len(it)):
#         tempTuple = (i, it[i])
#         temp.append(tempTuple)
#     return temp

# def gen_func(n):
#     for x in range(1, n):
#         yield x
# x = (gen_func(5))
# print(next(x))
# print(next(x))
# A generator function is a special type of function that returns an iterator object. 
# Instead of using return to send back a single value, generator functions use yield to produce a series of results over time. 
# This allows the function to generate values and pause its execution after each yield, maintaining its state between iterations.

def is_prime(nums):
    arr = []
    for i in nums:
        for j in range(2, int(i ** 0.5)+1):
            if i % j == 0:
                break
        else:
            arr.append(i)
    return arr

print(is_prime([2,3,4,5,6,7,8]))
    
def is_prime_list(nums):
    return [x for x in nums if all(x % j != 0 for j in range(2, int(x ** 0.5)+1))]
print(is_prime_list([2,3,4,5,6,7,8]))
