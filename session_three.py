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


# Computer average

countPositive = 0
countNegative = 0
count = 0
total = 0

num = int(input(
    "Enter an integer, the input ends if it is 0: "))

while num != 0:
    if num > 0:
        countPositive += 1
    elif num < 0:
        countNegative += 1

    total += num
    count += 1

    # Read the next number
    num = int(input(
        "Enter an integer, the input ends if it is 0: "))

if count == 0:
    print("No numbers are entered except 0")
else:
    print("The number of positives is", countPositive)
    print("The number of negatives is", countNegative)
    print("The total is", total)