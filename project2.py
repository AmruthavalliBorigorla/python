import random

def number_guessing_game():
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100

    # Generate a random number within the range
    random_number = random.randint(lower_bound, upper_bound)

    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}. Can you guess it?")

    # Initialize number of attempts
    attempts = 0

    while True:
        try:
            # Get the user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the user's guess
            if guess < lower_bound or guess > upper_bound:
                print(f"Please enter a number between {lower_bound} and {upper_bound}.")
            elif guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the correct number {random_number} in {attempts} attempts.")
                break  # Exit the loop if the correct number is guessed

        except ValueError:
            print("Invalid input. Please enter an integer.")

# To start the game, you need to call the function
number_guessing_game()
