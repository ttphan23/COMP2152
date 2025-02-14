import random
import functions_lab06

# Load previous game result from save.txt
previous_result = None
try:
    with open("save.txt", "r") as file:
        lines = file.readlines()
        if lines:
            previous_result = lines[-1].strip()
            print("Previous game result:", previous_result)
except FileNotFoundError:
    print("No previous game result found.")

# Define Dice, Weapons, Loot, Monster Powers
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []
monster_powers = {"Fire Magic": 2, "Freeze Time": 4, "Super Hearing": 6}
num_stars = 0

i = 0
input_invalid = True
while input_invalid and i in range(5):
    print("------------------------------------------------")
    combat_strength = input("Enter your combat Strength (1-6): ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    if not (combat_strength.isnumeric() and m_combat_strength.isnumeric()):
        print("Invalid input. Enter integer numbers between 1 and 6.")
        i += 1
        continue
    elif int(combat_strength) not in range(1, 7) or int(m_combat_strength) not in range(1, 7):
        print("Enter a valid integer between 1 and 6 only.")
        i += 1
        continue
    else:
        input_invalid = False
        combat_strength = int(combat_strength)
        m_combat_strength = int(m_combat_strength)

# Adjust combat strength based on previous game result
if previous_result:
    if "Hero" in previous_result and "gained" in previous_result:
        stars = int(previous_result.split(" ")[-2])
        if stars > 3:
            m_combat_strength += 1
    elif "Monster has killed" in previous_result:
        combat_strength += 1

# Roll for weapon
input("Roll the dice for your weapon (Press enter)")
weapon_roll = random.choice(small_dice_options)
combat_strength = min(6, combat_strength + weapon_roll)
print(f"The hero's weapon is {weapons[weapon_roll - 1]}")

# Roll for player health points
input("Roll the dice for your health points (Press enter)")
health_points = random.choice(big_dice_options)
print(f"Player rolled {health_points} health points")

# Roll for monster health points
input("Roll the dice for the monster's health points (Press enter)")
m_health_points = random.choice(big_dice_options)
print(f"Monster rolled {m_health_points} health points")

# Loop for valid Dream Levels input
while True:
    num_dream_lvls = input("How many dream levels do you want to go down? (Enter a number 0-3): ")
    if num_dream_lvls.isdigit() and int(num_dream_lvls) in range(0, 4):
        num_dream_lvls = int(num_dream_lvls)
        break
    print("Invalid input. Enter a number between 0 and 3.")

if num_dream_lvls > 0:
    health_points -= 1
    crazy_level = functions_lab06.inception_dream(num_dream_lvls)
    combat_strength += crazy_level
    print("combat strength:", combat_strength)
    print("health points:", health_points)

# Fight Sequence
while m_health_points > 0 and health_points > 0:
    input("Roll to see who strikes first (Press Enter)")
    attack_roll = random.choice(small_dice_options)
    if attack_roll % 2 != 0:
        input("You strike (Press enter)")
        m_health_points = functions_lab06.hero_attacks(combat_strength, m_health_points)
        if m_health_points == 0:
            num_stars = 3
            break
        input("The monster strikes (Press enter)")
        health_points = functions_lab06.monster_attacks(m_combat_strength, health_points)
        if health_points == 0:
            num_stars = 1
            break
    else:
        input("The Monster strikes (Press enter)")
        health_points = functions_lab06.monster_attacks(m_combat_strength, health_points)
        if health_points == 0:
            num_stars = 1
            break
        input("The hero strikes!! (Press enter)")
        m_health_points = functions_lab06.hero_attacks(combat_strength, m_health_points)
        if m_health_points == 0:
            num_stars = 3
            break

# Final Score Display
if health_points > 0:
    hero_name = ""
    while True:
        hero_name = input("Enter your Hero's name (in two words): ")
        name = hero_name.split()
        if len(name) == 2 and name[0].isalpha() and name[1].isalpha():
            short_name = name[0][:2] + name[1][0]
            print(f"I'm going to call you {short_name} for short")
            break
        print("Please enter a valid name with two words.")

    stars_display = "*" * num_stars
    print(f"Hero {short_name} gets <{stars_display}> stars")
    with open("save.txt", "a") as file:
        file.write(f"Hero {short_name} has killed a monster and gained {num_stars} stars.\n")
else:
    print("Monster has killed the hero previously")
    with open("save.txt", "a") as file:
        file.write("Monster has killed the hero previously\n")
