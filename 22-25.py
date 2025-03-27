# Write a Python programm that asks the user for two numbers and prints their sum

a = int(input('Input first value '))
b = int(input('Input second value '))
print(f"The sum of {a} + {b} is ", a + b) 

# Create two integer variables, and perform addition, subtraction, multiplication and division. Same for floating point and complex numbers


int1 = 25
int2 = 57
float1 = 25.72
float2 = 57.89
complex1 = complex(97, 125)
complex2 = complex(234, 567)
print(int1 + int2, '\t  Sum of two integers')
print(float1 + float2, '\t Sum of two float numbers')
print(complex1 + complex2, '\t Sum of two complex numbers')
print(int1 * int2, '\t Multiplication of two integres')
print(float1 * float2, '\t multiplication of two floats')
print(complex1 * complex2, '\t multiplication of two complex numbers')
print(int2 - int1, '\t subtraction of two int numbers')
print(float2 - float1, '\t subtratcion of floats')
print(complex1 - complex2, '\t subtraction of compl numb')
print(int2 / int1, '\t division of int')
print(float2 / float1, '\t division of floats')
print(complex1 / complex2, '\t division of complexes')


# Write a program that takes a string and extracts the first and last character using subscripts (indexing).

myString1 = str(input('enter a string here '))
print(f"First character {myString1[0]}, Last Character {myString1[-1]}")

# Write a program that slices the first 3 characters and the last 2 characters from a string

myString2 = str(input('enter a string here '))
print(f" '{myString2[:3]}'  and  ' {myString2[-2:]}' ")

# Write a program that takes two strings as input and concatenates them with a space in between.

myString3 = "Good"
myString4 = "Morning"
print(myString3 + " " + myString4)

# Write a program that takes a string and converts it to both uppercase and lowercase.
print(f"{myString3.upper()} and {myString4.lower()} " )

# Write a program that checks whether a string starts with the letter "A" and ends with the letter "Z".
print(f"Starts with A: {myString1.startswith('A')}; Ends with Z: {myString1.endswith('Z')}")

# Write a program that counts how many times the letter "a" appears in a given string.

print(f" 'a' appears {myString1.count('a')} times")

# Write a program that takes a sentence and splits it into words, then joins the words back into a sentence with hyphens (-) between them.

splitedString = myString1.split()
print("-".join(splitedString))

# Write a program that takes a user’s name as input and creates a greeting message like "Hello, [Name]!".

print(f"Hello, {myString1}!")