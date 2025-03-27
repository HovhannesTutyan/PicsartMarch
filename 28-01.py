from decimal import Decimal

# --------------------------------------------------------------------------------------------------------------------#
# 1) Create a program to format and print a float with 2 decimal places.

# floatDec = 20.5523452345
# print(round(floatDec, 2))

# --------------------------------------------------------------------------------------------------------------------#
# 2) Write a program to convert all characters in a string to uppercase and then to lowercase.

# upperLowerStr = "Write A Program To Convert All Characters In A String To Uppercase And Then To Lowercase."
# print(upperLowerStr.upper())
# print(upperLowerStr.lower())

# --------------------------------------------------------------------------------------------------------------------#
# 3) Create a program to count the number of occurrences of a specific character in a string.

# countOccur = "Create a program to count the number of occurrences of a specific character in a string."
# print(f"The occurance of letter 't' in the sentence is {countOccur.count('t')}")

# --------------------------------------------------------------------------------------------------------------------#
# 4) Write a program to concatenate two strings with a space in between.

# concatStr1 = "Write a program to concatenate two strings with a space in between."
# concatStr2 = "Write a program to concatenate two strings with a space in between."
# print(concatStr1 + " " + concatStr2)

# --------------------------------------------------------------------------------------------------------------------#
# 5) Create a program to find the sum of the first and last digit of a given number.

# sumFirstLast = int(input("Enter a number that has many digits "))
# firstDigit = sumFirstLast / 10 ** (len(str(sumFirstLast))-1)
# lastDigit = (sumFirstLast / 10)
# lastDigitStr = str(lastDigit).split(".")[1]
# print(f"The result of first digit {int(firstDigit)} and last digit {lastDigitStr} sum is {int(lastDigitStr)+int(firstDigit)} ")

# --------------------------------------------------------------------------------------------------------------------#
# 6) Write a program to calculate the average of 3 float numbers and format the result to 3 decimal places.

# avgFloat1 = 65.899345345
# avgFloat2 = 41.2524352453
# avgFloat3 = 27.23452435
# avgFloatSum = (avgFloat1 + avgFloat2 + avgFloat3) / 3
# print(f"The average of three float numbers will be {avgFloatSum:.3f}")

# --------------------------------------------------------------------------------------------------------------------#
# 7) Create a program that takes a string input and an integer input and repeats the string that many times.

# strInputRepeat = 4
# strInputRow = "Create a program that takes a string input and an integer input and repeats the string that many times."
# for x in range(strInputRepeat):
#     print(strInputRow)

# --------------------------------------------------------------------------------------------------------------------#
# 8) Ask the user to enter a string, and then print the string in reverse order.

# reverseStr = str(input("Enter a string to reverse it "))
# print(reverseStr[::-1])

# --------------------------------------------------------------------------------------------------------------------#
# 9) Count how many vowels are in the string and print the count.

# vowelString = "Count how many vowels are in the string and print the count."
# vowels = ["a", "o", "u", "e", "i", "y"]
# vowelSum = 0
# for s in vowelString:
#     if s in vowels:
#         vowelSum += 1
# print(vowelSum)

# --------------------------------------------------------------------------------------------------------------------#
# 10) Write a program that takes a string as input and outputs the longest substring without repeating characters. For example, the string "abcabcbb" should return "abc".

# repeatStr = "abcabcbb"
# repeatNew = set()
# for x in (repeatStr):
#     if x in repeatNew:
#         break
#     repeatNew.add(x)
# print(repeatNew)

# --------------------------------------------------------------------------------------------------------------------#
# 11) Write a program using a while loop that repeatedly asks the user to input a number until they input 0, then print the sum of all entered numbers.

# whileInpRep = int(input("Enter numbers for sum."))
# whileInputSum = whileInpRep
# while whileInpRep != 0:
#     whileInpRep = int(input("Enter numbers for sum."))
#     whileInputSum += whileInpRep
#     print(whileInpRep)
# print(whileInputSum)

# --------------------------------------------------------------------------------------------------------------------#
# 12) Create a list of 10 numbers (hardcoded) and calculate the sum of all numbers in the list.

# hardList = [65,41,27,77,52,3,19,-20,8,22.8]
# print(sum(hardList))
# hardListSum = 0
# for x in hardList:
#     hardListSum += x
# print(f"The sum of all elements in the list is {hardListSum}")

# --------------------------------------------------------------------------------------------------------------------#
# 13) Հայտարարել list, և տպել list-ի էլեմենտներից առավելագույնի արժեքը: List-ը պետք է պարունակի միայն int տիպի արժեքներ: Չօգտագործել max ֆունկցիան:

# maxList = [65,41,27,77,52,3,19,-20,8,22]
# maxValue = maxList[0]
# for x in maxList:
#     if x > maxValue:
#         maxValue = x
# print(f"The max value of the list is {maxValue}")
# maxList.sort()
# print(f"The max number of the sorted list is {maxList[-1]}")

# --------------------------------------------------------------------------------------------------------------------#
# 14) Հայտարարել list և տպել նվազագույն արժեքով էլեմենտի ինդեքսը։

# minList = [65,41,27,77,-48,52,3,19,-20,8,22]
# minNumber = minList[0]
# minNumberIndex = 0
# for i in range(len(minList)):
#     if minList[i] < minNumber:
#         minNumber = minList[i]
#         minNumberIndex = i
# print(f"The min number from the list is {minNumber} and its index is {minNumberIndex}")

# --------------------------------------------------------------------------------------------------------------------#
# 15) Հայտարարել երկու ամբողջ թվային արժեքներով list- եր  և տպել համապատասխանող ինդեքսներով էլեմնետների արտադրյալը էկրանին:

# indexList1 = [2,4,6,8,10,12,14,16,18,20]
# indexList2 = [3,5,7,9,11,13,15,17,19,21]
# for i in range(len(indexList1)):
#     print(indexList1[i] * indexList2[i])

# --------------------------------------------------------------------------------------------------------------------#
# 16) Գրել ծրագիր, որը ստանում է ամբողջ թիվ։ Հայտարարել list: Եթե list-ում առկա է տրված թիվը տպել YES, հակառակ դեպքում տպել NO։ 

# wholeNumberList = [2,4,6,8,10,12,14,16,18,20]
# wholeNumberInput = int(input("Enter a whole number "))
# if wholeNumberInput in wholeNumberList:
#     print("Yes")
# else:
#     print("No")

# --------------------------------------------------------------------------------------------------------------------#
# 17) Հայտարարել list,  որը բաղկացած է string-ներից: Տպել թե քանի անգամ է յուրաքանչյուրը հանդիպում list-ում: 

repeatList = ["hello", "I", "love", "programming", "in", "python", "and", "in", "hello", "world"]
for x in repeatList:
    print(f'The count of word "{x}" is {repeatList.count(x)}')
