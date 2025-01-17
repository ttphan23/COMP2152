import random

def roll_the_dice():
    # Prompts user to play
    play = input("Would you like to roll the dice to choose a weapon? (yes/no): ").strip().lower()

    if play != "yes":
        print("Maybe next time!")
        return

    # Define the weapons array
    weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

    try:
        # Roll the dice (1-6)
        weaponRoll = random.randint(1, 6)  # Random number between 1 and 6
        print(f"You rolled: {weaponRoll}")

        # Add weaponRoll to hero's combat strength
        hero_combat_strength = 5 + weaponRoll

        # Index for weaponRoll
        weapon = weapons[weaponRoll - 1]
        print(f"Your weapon is: {weapon}")

        # Weapon quality
        if weaponRoll <= 2:
            print("You rolled a weak weapon, friend.")
        elif weaponRoll <= 4:
            print("Your weapon is meh.")
        else:
            print("Nice weapon, friend!")

        # Check if weapon is not a Fist
        if weapon != "Fist":
            print("Thank goodness you didn't roll the Fist...")

    except Exception as e:
        print(f"An error occurred: {e}")

roll_the_dice()
