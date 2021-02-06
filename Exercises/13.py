# Exercise 13 
# Fibonacci  
# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
# Take this opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


def fibo():
    num = int(input("Enter a number?\n"))
    i = 1
    if num == 0:
        sequence = []
    elif num == 1:
        sequence = [1]
    elif num == 2:
        sequence = [1,1]
    elif num > 2:
        sequence = [1,1]
        while i < (num - 1):
            sequence.append(sequence[i] + sequence[i-1])
            i += 1
    return sequence

print(fibo())

