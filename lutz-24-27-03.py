import time
## sum of list items with while loop

# start = time.time()
# l = [1,2,3,4,5]
# sum = 0
# while l:
#     sum += l[0]
#     l = l[1:] 
# print(sum)
# end = time.time()
# print("The time of execution of while loop is ", (end - start) * 10 ** 3, " ms") 
# 0.08726119995117188  ms

## sum of list items with for loop

# start = time.time()
# forSum = 0
# for i in l:
#     forSum += i
# print(forSum)
# end = time.time()
# print("The time of execution of while loop is ", (end - start) * 10 ** 3, " ms")
# 0.16379356384277344  ms

## sum of list items with recursion
# start = time.time()
# def mySum(L):
#     if not L:
#         return 0
#     else:
#         return L[0] + mySum(L[1:]) 
# print(mySum(l))
# end = time.time()
# print("The time of execution of while loop is ", (end - start) * 10 ** 3, " ms")
# 0.2434253692626953  ms

# sum of items in a not flat list with recursion

# fl = [[[[[1], 2], 3], 4], 5]
# def sumTree(L):
#     tot = 0
#     for x in L:
#         if not isinstance(x, list):
#             tot += x
#         else:
#             tot += sumTree(x)
#     return tot
# print(sumTree(fl))

# sum of items in a not flat list with queues and stacks

# def sumTree(L):
#     tot = 0
#     items = list(L)
#     while items:
#         front = items.pop(0)
#         if not isinstance(front, list):
#             tot += front
#         else:
#             items.extend(front)
#     return tot
# print(sumTree([1, [2, [3, [4, [5]]]]]))

ft = [1, [2, [3, [4, [5]]]]]
fn = ft
fn.append(45)
print(ft)