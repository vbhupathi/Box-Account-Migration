# Exercise 10

# List Overlap Comprehensions Solutions
# This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.

# Take two lists, say for example these two:

# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes. Write this using at least one list comprehension. 
# (Hint: Remember list comprehensions from Exercise 7).

# Extra:

# Randomly generate two lists to test this


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print([item for item in set(a) if item in b])
# NOT COMMON
print(set([item for item in b if item not in a]).union([item for item in a if item not in b]))


import random

a = [random.randint(1,20) for x in range(2, random.randint(4,40))]
b = [random.randint(1,20) for x in range(2, random.randint(4,40))]
print([num for i, num in enumerate(a) if num in b and num not in a[i+1:]])
         

