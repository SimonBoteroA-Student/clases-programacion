import random


def play_game(max_number):
    # Generate a random number between 1 and max_number

    target_number = []
    for x in range(1, 10):
        target_number.append(random.randint(1, max_number))
    print(target_number[11])
    guess = None
    attempts = 0
    past_guesses = []

    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and " + str(max_number) + ".")

    for target in target_number:
        while guess != target:
            print("Past guesses: " + str(past_guesses))
            guess = int(input("Enter your guess: "))
            past_guesses.append(guess)
            attempts += 1

            if guess < target:
                print("Too low! Try again.")
            elif guess > target:
                print("Too high! Try again.")
            else:
                print("Congratulations! You found the number in " + str(attempts) + " attempts!")

# Start the game with maximum number 100
play_game(100)
