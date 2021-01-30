# Exercise 2
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
number = int(input("Enter a number: "))
if number%2 == 0: print("the entered " + str(number) + " is even number")
else: print("the entered " + str(number) + " is odd number")
if number%4 == 0: print("the entered " + str(number) + " is divided by number 4")
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
num = int(input("Enter a check number:"))
check = int(input("Enter a divde by number:"))
if num%check == 0: print(str(check) +" divides evenly into "+ str(num))
else: print(str(check) +" does not divides evenly into "+ str(num))