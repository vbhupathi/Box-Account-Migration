# Exercise 11
# Check Primality Functions   
# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors.). 
# You can (and should!) use your answer to Exercise 4 to help you. Take the opportunity to practice using functions.

def number():
     return int(input("Enter a number!\n"))
num = number()
a = [i for i in range(2, num) if num % i == 0]

def prime_num(n):
	if num > 1:
		if len(a) == 0:
			print("PRIME NUMBER")
		else:
			print("NOT a PRIME NUMBER")
	else:
		print("NOT A PRIME NUMBER")
	
prime_num(num) 
