# Exercise 6
# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

string = input(" Enter a Palindrome string: ")
string=str(string)
backwordString=string[::-1]
print(backwordString)

if string == backwordString :
    print(string + " is a palindrome")
else :
    print(string + " is not a palindrome")