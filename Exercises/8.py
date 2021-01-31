# Exercise 8
# Rock Paper Scissors   
# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, a
# nd ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

game = 1 == 1
wincount = 0
losecount = 0
while game:    
       
    Player = input('''Please pick one:
            rock            
            paper
            scissors \n''').lower()
    import random
    computer = random.randint(1,3) # 1 = Rock, 2 = Paper, 3 = Scissors
    # Play game
    if Player == "rock" and computer == 1 :
        print("Computer selects Rock it's a DRAW!!.")
    elif Player == "rock" and computer == 2 :
        print("Computer selects Paper and WINS.")
        losecount += 1
    elif Player == "rock" and computer == 3 :
        print("Computer selects Scissors and LOSES.")
        wincount += 1

    elif Player == "paper" and computer == 1 :
        print("Computer selects Rock and LOSES.")
        wincount += 1
    elif Player == "paper" and computer == 2 :
        print("Computer selects Paper it's a DRAW!!.")
    elif Player == "paper" and computer == 3 :
        print("Computer selects Scissors and WINS.")
        losecount += 1

    elif Player == "scissors" and computer == 1 :
        print("Computer selects Rock and WINS.")
        losecount += 1
    elif Player == "scissors" and computer == 2 :
        print("Computer selects Paper and LOSES.")
        wincount += 1
    elif Player == "scissors" and computer == 3 :
        print("Computer selects Scissors it's a DRAW!!.")

    else :
        print("Unknown result.")
    game = input("Do you want to play again? y/n ") == "y"
print("You won " + str(wincount) + " and lose " + str(losecount))


# short version

Selections = list(['rock', 'paper', 'scissors'])

playerOne = input("What is your selection?\n").lower()
playerTwo = input("What is your selection?\n").lower()

if playerOne == playerTwo:
    print("it is a DRAW!!!!")

if Selections.index(playerTwo) == (Selections.index(playerOne) + 1)%3:
    print("PlayerOne WINS!!")

if Selections.index(playerOne) == (Selections.index(playerTwo) + 1)%3:
    print("PlayerTwo WINS!!")
