# 1) Write a program that takes a sentence and creates a dictionary where each word is a key, and the value is the number of times that word appears. 

# dictStr = "the cat and the hat"
# splitDictStr = dictStr.split()
# dictCount = []
# for x in splitDictStr:
#     dictCount.append(splitDictStr.count(x))
# listDict = dict(zip(splitDictStr, dictCount))
# print(listDict)

# --------------------------------------------------------------------------------------------------------------------#
# 2) Create a dictionary to store student names as keys and their scores as values. 
# Use a few sample names and scores to populate the dictionary. Print out each student’s name and score on a new line.

# studentGrades = {
#     "Alison Baker":         8, 
#     "Joe Gomez":            5,
#     "Ibrahima Konte":       7,
#     "Virgil van Dijk":      8,
#     "Alexis Max Allister":  9,
#     "Wataru Endo":          4,
#     "Luis Diaz":            8,
#     "Darwin Nunea":         6,
#     "Mohamed Salah":        8,
#     "Cody Gapko":           7
# }
# for key, value in studentGrades.items():
#     print(f"Student name: {key}, Grade: {value}")

# --------------------------------------------------------------------------------------------------------------------#
# 3)Create a dictionary that maps numbers from 1 to 5 to their word equivalents (e.g., {1: "one", 2: "two", ...}). 
# Use this dictionary to convert a list of numbers into words and print each word on a new line.

# mapDict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
# mapDictNumb = []
# for numb in mapDict.keys():
#     mapDictNumb.append(numb)
# for numb in mapDictNumb:
#     print(f"The number of each key is {mapDict.get(numb)}")

# --------------------------------------------------------------------------------------------------------------------#
# 4) Create a dictionary to represent a store’s inventory with items as keys and quantities as values. 
# Print the quantity of a specific item (e.g., "Apples"). Update the quantity of an item and print the dictionary to show the change.

# productsInStore = {
#     "Apples":               8, 
#     "Bananas":              5,
#     "Potatoes":             7,
#     "Tomatoes":             8,
#     "Carrots":              9,
#     "Chocolates":           4,
#     "Pancackes":            8
# }

# print(f"The quantity of Apples is {productsInStore["Apples"]}")
# productsInStore["Apples"] = 15
# print(f"After supplies, the quanitity of Apples is {productsInStore["Apples"]}")

# --------------------------------------------------------------------------------------------------------------------#
# 5) Write a program that takes a sentence and uses a set to find all unique words. Print each unique word on a new line.
# setStr = "the cat and the hat"
# splitSetStr = setStr.split()
# setUnique = set(splitSetStr)
# for x in setUnique:
#     print(x)

# --------------------------------------------------------------------------------------------------------------------#
# # 6) Given two lists of numbers, use sets to find and print the common elements between them.
numbList1 = [65,41,27,77,52,37,89]
numbList2 = [65,42,27,67,72,97,-89]
# commonElSet = set()
# for x in numbList1:
#     if x in numbList2:
#         commonElSet.add(x)
# print(commonElSet)
###### or ######
numbList1Set = set(numbList1)
numbList2Set = set(numbList2)
print(numbList1Set.intersection(numbList2Set))

# --------------------------------------------------------------------------------------------------------------------#
# 7) Given a list of numbers, use a set to find any duplicates in the list and print them. 
# You can add numbers to a set one by one and check if they are already present.

# setList = [1, 2, 2, 3, 4, 4, 5]
# duplSet = set()
# for x in setList:
#     if setList.count(x)>1:
#         duplSet.add(x)
# print(duplSet)

# --------------------------------------------------------------------------------------------------------------------#
# 8) Use a set to create a list of vocabulary words from a paragraph.
#  Break the paragraph into individual words, add each word to the set, and print the final set of unique words.

# vocabStr = "Python is fun. Python is powerful."
# splitVocabStr = vocabStr.split()
# vocabSet = set(splitVocabStr)
# print(vocabSet)