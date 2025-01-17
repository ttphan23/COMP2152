import random

def random_game():
    targetNumber = random.randint(1, 100)
    play = input("Would you like to play a number guessing game? (yes/no): ").strip().lower()

    if play != "yes":
        print("Maybe next time!")
        return

    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            userGuess = int(input("Please select a number between 1 and 100: "))
            attempts += 1

            if userGuess < targetNumber:
                if abs(userGuess - targetNumber) <= 5:
                    print("Very close, but still too low! Try again.")
                else:
                    print("Too low! Try again.")
            elif userGuess > targetNumber:
                if abs(userGuess - targetNumber) <= 5:
                    print("Very close, but still too high! Try again.")
                else:
                    print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed it in {attempts} attempts.")
                return
        except ValueError:
            print("Invalid input! Please enter a valid number between 1 and 100.")

    print(f"Game over! The target number was {targetNumber}.")

random_game()
