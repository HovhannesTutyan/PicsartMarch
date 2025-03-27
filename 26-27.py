from fractions import Fraction
from decimal import Decimal
import math

# 1) Write a program that prompts the user to create an empty list. 
# Then, the user should be able to add elements to the list using three different methods: append(), extend(), and insert().

# myList = []
# number = int(input('Enter a number to append to list '))
# myList.append(number)
# print(f"The appendid list is {myList}")
# multipleNumbers = input('Enter multiple numbers to extend the list ').split()
# myList.extend(multipleNumbers)
# print(f"The Extended list is {myList} ")
# specificNumber = int(input('Enter a specific number '))
# specificIndex = int(input (f'Enter an index in range {len(myList)} '))
# myList.insert(specificIndex, specificNumber)
# print(myList)
# removeByValue = input(f"Select a number from the list to remove {myList} ")
# myList.remove(int(removeByValue))
# print(myList)
# removeByIndex = int(input(f"Enter the index of number to be removed in range {len(myList)} "))
# myList.pop(removeByIndex)
# print(myList)

# --------------------------------------------------------------------------------------------------------------------#
# 2) Write a program that prompts the user to create a list containing different types of elements 
# (integers, strings, floating-point numbers, etc.). Allow the user to add elements of different types to the list using append(), extend(), and insert().

# myList2 = input("Create a list of different types of objects").split()
# intNumber = int(input("Enter integer number to append to list"))
# myListStr = str(input('Enter string to append to the list'))
# floatNumber = float(input("Enter float number to append to the list"))
# myList2.append(myListStr)
# myList2.append(intNumber)
# myList2.append(floatNumber)
# print(myList2)
# extendedList = input("Add multiple elements to extend List 2").split()
# myList2.append(extendedList)
# print(myList2)
# insertListNumber = int(input("Enter a value to insert in the list"))
# insertListIndex = int(input("Enter an index to be inserted"))
# myList2.insert(insertListIndex, insertListNumber)

# --------------------------------------------------------------------------------------------------------------------#
# 3) Write a program to count the occurrences of a specific element in a list and tuple.

# myList3 = [65, 41, 27, 52, 34, "hello", 45.67, 67.89, "James", "hello"]
# myListInt = [65, 41, 27, 52, 34, 45.67, 67.89]
# print("The occurance of element is ", myList3.count("hello"))

# --------------------------------------------------------------------------------------------------------------------#
# 4) Write a program to find and print the maximum and minimum values in a list and a tuple.

# print("The max number of int is ", max(myListInt))
# print("The min number of Int list is ", min(myListInt))

# --------------------------------------------------------------------------------------------------------------------# 
# 5) Write a program to access elements from a nested list and a nested tuple.
# 6) Write a program to find the sum of all elements in a list and a tuple.
# 7) Write a program to reverse a list and a tuple

# nestedList = [65,41,27,77, [13,51,24], 51, ["hello", "James", 45]]
# nestedTuple = (65,41,27,77, (13,51,24),51, ("hello", "James", 45))
# print("Access an element in a List ", nestedList[1])
# print("Access an element in a Tuple ", nestedTuple[1])
# print("Access nested element in a List ", nestedList[6][1])
# print("Access nested element in a tuple ", nestedList[6][1])
# print("Sum of all elements in a List is ", sum(nestedList[:4]))
# print("Sum of all elements in a tuple is ", sum(nestedTuple[:4]))
# reversedList = nestedList[::-1]
# reversedTuple = nestedTuple[::-1]
# print("The reversed list will be ", reversedList)
# print("The reversed tuple will be ", reversedTuple)

# --------------------------------------------------------------------------------------------------------------------# 
# 8) Create a program that adds, subtracts, multiplies, and divides two integers, two floats, and a combination of both.

ntInt1 = 65
ntInt2 = 41
ntFloat1 = 45.58
ntFloat2 = 88.77
print('add two int ', ntInt1 + ntInt2)
print('multiply two int', ntInt1 * ntInt2)
print('devide two int', ntInt1 / ntInt2)
print('subtract two int', ntInt1 - ntInt2)

print('add two float ', ntFloat1 + ntFloat2)
print('multiply two float', ntFloat1 * ntFloat2)
print('devide two float', ntFloat1 / ntFloat2)
print('subtract two float', ntFloat1 - ntFloat2)

print('add int to float ', ntInt1 + ntFloat2)
print('multiply int to float', ntInt1 * ntFloat2)
print('devide int to float', ntInt1 / ntFloat2)
print('subtract int to float', ntInt1 - ntFloat2)

# --------------------------------------------------------------------------------------------------------------------#
# 9) Write a program to calculate the product of two complex numbers.

cn1 = complex(65, 41)
cn2 = complex(27, 53)
print("Product of two complex numbers will be ", cn1 * cn2)

# --------------------------------------------------------------------------------------------------------------------#
# 10) Create a fraction that represents 1/2 and another fraction representing 2/3. Add them and print the result.

fr1 = Fraction(1, 2)
fr2 = Fraction(2, 3)
print("The sum of fractions ", fr1+fr2)

# --------------------------------------------------------------------------------------------------------------------#
# 11) Using decimal, calculate the sum of 0.1 and 0.2 and compare it with float.

# fl1 = 0.1
# fl2 = 0.2

# flSum = (float(fl1 + fl2))
# dcSum = (Decimal(fl1) + Decimal(fl2))
# print(f"Float sum is {flSum} and Decimal sum is {dcSum}")
# print(f"Compare Float sum to Decimal sum - {flSum == dcSum}")

# --------------------------------------------------------------------------------------------------------------------#
# 12) Write a program to check if the sum of three numbers is equal to 100. Use boolean comparisons to print the result as True or False.

# boolNumb1 = int(input("Enter the first number "))
# boolNumb2 = int(input("Enter the second number "))
# boolNumb3 = int(input("Enter the third number "))
# print(f"{boolNumb1} + {boolNumb2} + {boolNumb3} is equal to 100 is {boolNumb1 + boolNumb2 + boolNumb3 == 100}" )

# --------------------------------------------------------------------------------------------------------------------#
# 13) Accept two fractions from the user and find their GCD using the math.gcd() function 
# along with the numerator and denominator attributes of each fraction.

# fr3 = Fraction(4, 9)
# fr4 = Fraction(8, 27)
# fr_num = math.gcd(fr3.numerator, fr4.numerator)
# fr_den = math.gcd(fr3.denominator, fr4.denominator)
# print(f"Greates common devisior of {fr3} and {fr4} nominator is {fr_num}, and for denominator is {fr_den} ")

# --------------------------------------------------------------------------------------------------------------------#
# 14) Write a program to check if a number is odd or even

# oddEven = int(input("Enter a number"))
# if (oddEven % 2 == 0):
#     print(f"{oddEven} number is Even")
# else:
#     print(f"{oddEven} number is Odd")

# --------------------------------------------------------------------------------------------------------------------#
# 15) Compare the values of a float and an int and print whether they are equal or not.

# floatInt1 = int(input("Enter an int number"))
# floatInt2 = float(input("Enter a float number"))
# print(f"Float and Int numbers are Equal -  {floatInt1 == floatInt2}")

# --------------------------------------------------------------------------------------------------------------------#
# 16) Calculate the square of an integer and a float using the exponentiation operator (**).

# sqInt = int(input("Enter an int number "))
# sqFloat = float(input("Enter a float number "))
# print(f"The square of an int number will be - {sqInt ** 2}.\n The square of an Float number will be - {sqFloat ** 2}.  ")

# --------------------------------------------------------------------------------------------------------------------#
# 17) Write a program to find the maximum of three numbers using nested conditional operators.

# maxNumbers = [22, 65, 41, 55, 99]
# max = maxNumbers[0]
# for x in maxNumbers:
#     if x > max:
#         max = x
# print(f"the max of given numbers is {max}")

# a = 15
# b = 20 
# c = 22
# if a > b and a > c:
#     print(f"{a} is the max number")
# elif b > a and b > c:
#     print(f"{b} is the max number")
# else:
#     print(f"{c} is the max number")

# --------------------------------------------------------------------------------------------------------------------#
# 18) Accept two integer inputs from the user and calculate the absolute difference between them using the abs() function. Print the result.

# absInt1 = int(input("Enter the first int for ABC calc (negative number)"))
# absInt2 = int(input("Enter the second int for ABC calc (positive number)"))
# print(f"The abs difference will be {abs(absInt1) - abs(absInt2)}")

# --------------------------------------------------------------------------------------------------------------------#
# 19) Accept an integer input from the user and use conditional statements to print whether the number is positive, negative, or zero.

# posNegNumb = int(input("Enter a positive, negative number or Zero "))
# if posNegNumb > 0:
#     print(f"The {posNegNumb} is Positive")
# elif posNegNumb == 0:
#     print(f"{posNegNumb} is 0")
# else: 
#     print(f"{posNegNumb} is negative")

# --------------------------------------------------------------------------------------------------------------------#
# 20) Accept two integer inputs from the user. Check if the first number is a multiple of the second and print True if it is, otherwise print False.

multNumb1 = int(input("Enter the furst number for multiple check"))
multNumb2 = int(input("Enter the second number for multiple check"))
print(f"{multNumb1} is the multiply of {multNumb2} - {multNumb1 % multNumb2 == 0}")

