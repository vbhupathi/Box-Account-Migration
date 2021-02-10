# Exercise 15

#  Reverse Word Order   
# strings
# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

#   My name is Michele
# Then I would see the string:

#   Michele is name My
# shown back to me.

# Method 1
def reverseString_M1(s):
  return ' '.join(s.split()[::-1])

userString = input("Enter a string!\n")

print(reverseString_M1(userString))
# Method 2
def reverseString_M2(s):
    w = s.split()
    return " ".join(reversed(w))
  

# method 3
def reverseString_M3(s):
  w = s.split()
  result = []
  for sord in w:
    result.insert(0,sord)
  return " ".join(result)

# method 4
def reverseString_M4(s):
  w = s.split()
  w.reverse()
  return " ".join(w)

# test code
UserSentence = input("Enter a sentence:\n ")
print (reverseString_M2(UserSentence))
print (reverseString_M3(UserSentence))
print (reverseString_M4(UserSentence))