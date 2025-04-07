# 1) Գրել ֆունկցիա, որը կվերադարձնի [1-200] միջակայքի բոլոր զույգ թվերը:
def even_numbers():
    en = [x for x in range(1,200) if x % 2 == 0]
    print(en)
    return en
even_numbers()

# 2) Գրել ֆունկցիա, որը կտպի տրված թվի բազմապատկման աղյուսակը։
def multip_table(number):
    x = 10 
    i = 1
    while i < x:
        print(f"{number} * {i} = {number * i}")
        i+= 1
multip_table(4)

# 3) Գրել ֆունկցիա, որը ստանում է n ամբողջ թիվը և վերադարաձնում մինչև [1, n] բոլոր պարզ թվերը:
def plain_number(number):
    myArray = []
    if number < 1:
        return 1
    i = 2
    while i == number/2:
        if number % i == 0:
            myArray.append(number)
        i += 1
    return myArray
print(plain_number(10))

# 4) Գրել ֆունկցիա, որը կստանա թիվ և կվերադարձնի թվի երկուական տեսքը տողի տեսքով։
def binary_number(number):
    while number > 0:
        pass
    
# 5) Գրել ֆունկցիա, որը կստանա նախադասություն և կվերադարձնի նրա ամենաերկար բառը։
def longest_word(word):
    if isinstance(word, str):
        splited_word = word.split()
        splited_word.sort()
    else:
        return ("Not a string")
    return splited_word[0]

sentence = "Thiss is a long word"
print(longest_word(sentence))

# 6) Գրել ֆունկցիա, որը ստանում է ամբողջ թվային պարամետր: 
# Ֆունկցիան վերադարդձնում է True՝ եթե այն կատարյալ թիվ է և False հակառակ դեպքում:
def perfect_number(number):
    total = 0
    for n in range(1, number):
        if n % 2 == 0:
            total += n
    return total
numb = 6
if numb == perfect_number(numb):
    print(True) 
else:
    print(False)

# 7) Գրել ֆունկցիա, որը ունի հետևյալ նախատիպը (prototype)  int sqrt (int num); 
# Ֆունկցիան վերադարձնում է num ամբողջ թվի քառակուսային արմատի արժեքը։
def prototype(number):
    square_number = number ** 2
    # root_number = sqrt(square_number)

# 8) Իրականացնել join ֆունկցիան:
def join_string(my_str):
    concat_str = []
    myString = my_str.split()
    for i in myString:
        concat_str += i
    print(myString)
    print(concat_str)
join_string("This is a long string")

# 9) 
def f(total=0):
    def inner(n=None):
        if n is None:  
            return total
        return f(total + n)  
    return inner
print(f()(3)(6)(7)(6)(7)())

# 10 chunck generator

def chunk_generator(iter, numb):
    for i in range(0, len(iter), numb):
        yield iter[i:i + numb]
    
nums = [1,2,3,4,5,6]
chunk = chunk_generator(nums, 4)
print(next(chunk))
print(next(chunk))

# 12 prime generator with yeald
def prime_generator(nums):
    for num in nums:
        for x in range(2, num):
            if num % x == 0:
                break
        else:
            yield num

pm = prime_generator([2,3,4,5,6])
print(next(pm))
print(next(pm))
print(next(pm))
# print(next(pm))

# 13 
numss = [[23, 13,2], [34,45,56,45]]
myLen = [min((len(x)) for x in numss)]
print(myLen)

# 14 Transpose rows 