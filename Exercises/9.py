# Exercise 9

# Guessing Game One   
# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.


import random

guessnumber = 0
count = 0

num = random.randint(1,9)
while guessnumber != num and guessnumber != "exit":
    guessnumber= input("Guess a nummber!\n")
        
    if guessnumber == "exit":
        break
    guessnumber = int(guessnumber)
    count += 1
    if int(guessnumber) ==  num:
        print("your guess is correct")
        print("you took", count, "guesses!")

    elif int(guessnumber) > num:
        print("your guess is greater than the actual number ")
    elif int(guessnumber) < num:
        print("Your guess is less than the actual number")
    