# Exercise 14

# List Remove Duplicates  
# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

def remove_duplicates_loops(a):
  b = []
  for i in a:
    if i not in b:
      b.append(i)
  return b

def remove_duplicates_sets(a):
    return list(set(a))

c = [1,1,2,3,4,4,5,7,3,8,8,2,9]
print (c)
print (remove_duplicates_loops(c))
print (remove_duplicates_sets(c))

# Excercise 5 using set 
import random

a = range(1, random.randint(1,50))
b = range(1, random.randint(5,30))
print(list(set([item for item in a if  item in b])))