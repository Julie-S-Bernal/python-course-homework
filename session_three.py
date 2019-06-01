# Guess the number
import random

# Generate a random number to be guessed
number = random.randint(1, 100)

print("Guess a magic number between 0 and 100")

# Write your code below:
# Try to find the condition that will stop the loop
# What statement should you put in the body of the loop?
userGuess = -1

while userGuess != number:
	userGuess = int(input('Your guess:'))
if userGuess == number:
	print('Your guess is correct')
elif guess > number: 
    print("Your guess is too high")
else:
    print("Your guess is too low")
