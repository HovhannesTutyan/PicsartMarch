# import copy
# li1 = [65, 41, 27, [77, 52, 33]]
# # li2 = li1
# # li2[3][1] = 88
# # li2 = li1 + [4]
# # li2 = li1.append(4)

# # l3 = li1.copy()


# # l3[2]= 987

# # print(li1, l3)

# li2 = copy.copy(li1)
# li2[3].append(4)
# print(li1)

# lst = [7,8,9,10,11]
# for i in lst:
#     if i % 3 == 0:
#         continue
#     elif i == 10:
#         break
#     else:
#         print(i, end=" ")

# for i in range (1,6):
#     square = i ** 2
#     print(square)
#     if(square == 9):
#         break

# di = {"a":1, "b":2, "c":3}
# for i in di.values():
#     print(i)

# words = ["python", "java", "c++"]
# for word in words:
#     print(word[0])

# for x in "spam":
#     print(x)
# print("spam".split())

# x = 10 
# if x > "5":
#     print('x')

# words = ['Python', 'c++', 'Java', 'Javascript']
# for i in range(0, len(words)):
#     words[i] = words[i].swapcase()
# words.sort(key=len, reverse=True,)
# print(words)


# branch = {'spam': 1.25,
#     'ham': 1.99,
#     'eggs': 0.99,
#     'branch': 5.99
#     }
# print(branch.get(branch["eggs"], "hello"))

# def foo(x: int, y: int)-> int:
#     return x + y
# print(foo('hello', 'buy'))

# def foo(x, y=[]):
#     y.append(x)
#     return y

# print(foo(5))
# print(foo(5, [12]))
# print(foo(10))
# print(foo.__annotations__)

# x = 99
# def foo(y):
#     # x += y this will not work, can't change x 
#     z = x + y
#     return z
# print(foo(1))
# print(x)

# y, z = 10, 12
# def foo():
#     global x
#     x = y + z
#     return x
# print(y)
# print(foo())
# print(x)

# def foo():
#     x.append(56)
#     return x
# x = [9 ,34]
# print(x)
# foo()
# print(x)

def intersect(*args):
    # res = set()
    # for x in args[0]:
    #     for other in args[1]:
    #         if x == other:
    #             res.add(x)
    # return res
    res = []
    for x in args[0]:
        if x in res:
            continue
        for other in args[1:]:
            if x not in other:
                break
            else:
                res.append(x)
    return res

print(intersect([65,41,27], [65,34,45, 34, 27]))


