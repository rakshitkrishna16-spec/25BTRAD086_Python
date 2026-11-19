import random

target = random.randint(1, 100)
guess = None

print("Guess a number between 1 and 100")

while guess != target:
    guess = int(input("Enter your guess: "))
    if guess < target:
        print("Too low! Try again.")
    elif guess > target:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it right.")