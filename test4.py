#########################################
foo = False
if foo:
    def foo():
        return foo.__name__
else:
    def foo():
        foo.__name__ = "main"
        return foo.__name__
print(foo())
########################################## 7 1 7 49
def foo(num:int)-> bool:
    if isinstance(num, int):
        foo.member_data *= 7
        return True
    else:
        foo.member_data //=7
        return False
    
foo.member_data = 1
foo(18)
print(foo.member_data, end=" | ")
foo(19.4)
print(foo.member_data, end=" | ")
foo(0)
print(foo.member_data, end=" | ")
foo(-9)
print(foo.member_data, end=" | | ")
########################################## 64 99
# num = 99
# def foo():
#     num = 64
#     print(num, end=" | ")
# foo()
# print(num)
########################################## error
# num = 99
# def foo():
#     print(num, end=" | ")
#     num = 64
# foo()
# print(num)
########################################## 99 64
# num = 99
# def foo():
#     global num
#     print(num, end=" | ")
#     num = 64
# foo()
# print(num)
########################################## 88 99
# num = 99
# def foo1():
#     num = 88
#     def foo2():
#         print(num, end=" | ")
#     foo2()
# foo1()
# print(num)

########################################## 88
# cout = print
# print = 99
# def f1():
#     print = 88
#     def f2(print=print):
#         cout(print)
#     f2()
# f1()

########################################## 77 88 77
# num = 99
# def f1():
#     num = 88
#     def f2():
#         global num
#         num = 77
#         print(num, end=" | ")
#     f2()
#     print(num, end=" | ")
# f1()
# print(num)
########################################## 77 77 99
# num = 99
# def f1():
#     num = 88
#     def f2():
#         nonlocal num
#         num = 77
#         print(num, end=" | ")
#     f2()
#     print(num, end=" | ")
# f1()
# print(num)
########################################## error
# num = 99
# def f1():
#     def f2():
#         nonlocal num
#         num = 77
#         print(num, end=" | ")
#     f2()
#     print(num, end=" | ")
# f1()
# print(num)
########################################## 88 77 77
num = 99
def f1():
    global num
    num = 88
    def f2():
        global num
        print(num, end=" | ")
        num = 77
    f2()
    print(num, end=" | ")
f1()
print(num)