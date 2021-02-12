# Exercise 16

# Password Generator    
# Write a password generator in Python. Be creative with how you generate passwords 
# - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
# The passwords should be random, generating a new password every time the user asks for a new password. 
# Include your run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.


# Method 1
import random

passChars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?.,'"
passLength = 8
print ("".join(random.sample(passChars, passLength)))

# Method 2

import string
import random

def PassWordGen(size = 15, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

print(PassWordGen(int(input('Desired length of the password: \n'))))

# Method 3

def password():
       import random
       import string
       uppercase = (string.ascii_uppercase)
       lowercase = (string.ascii_lowercase)
       number = (string.digits)
       symbols = (string.punctuation)
       Light=  lowercase + number
       Medium= uppercase + lowercase + number
       Strong= uppercase + lowercase + number + symbols
       desiredPasswordType = input('How Secure must have light/Medium/strong ?: ')
       x= int(input('How many characters would you like in your password?:\n'))
       if desiredPasswordType  == 'light':
            print( "".join(random.sample(Light, x)))
       elif desiredPasswordType  == 'Medium':
            print("".join(random.sample(Medium, x)))
       elif desiredPasswordType  == 'strong':
            print("".join(random.sample(Strong, x)))
       else:
            print(' Characters length must be an number, try again!')
            password()

if __name__ == "__main__":
 password()