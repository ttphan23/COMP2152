# comment
import random

# Put all the functions into another file and import them
import functions_lab05_starter

# Game Flow
# Define two Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
good_loot_options = ["Health Potion", "Leather Boots"]
bad_loot_options = ["Poison Potion"]
belt = []

# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Define the number of stars to award the player
num_stars = 0

# Loop to get valid input for Hero and Monster's Combat Strength
i = 0
input_invalid = True

while input_invalid and i in range(5):
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    combat_strength = input("Enter your combat Strength (1-6): ")
    print("    |", end="    ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    # Validate input: Check if the string inputted is numeric
    if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
        # If one of the inputs are invalid, print error message and halt
        print("    |    One or more invalid inputs. Player needs to enter integer numbers for Combat Strength    |")
        i = i + 1
        continue

    # Note: Now safe to cast combat_strength to integer
    # Validate input: Check if the string inputted
    elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength)) not in range(1, 7):
        print("    |    Enter a valid integer between 1 and 6 only")
        i = i + 1
        continue

    else:
        input_invalid = False
        break

if not input_invalid:
    input_invalid = False
    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

    # Roll for weapon
    print("    |", end="    ")
    input("Roll the dice for your weapon (Press enter)")
    ascii_image5 = """
              , %               .           
   *      @./  #         @  &.(         
  @        /@   (      ,    @       # @ 
  @        ..@#% @     @&*#@(         % 
   &   (  @    (   / /   *    @  .   /  
     @ % #         /   .       @ ( @    
                 %   .@*                
               #         .              
             /     # @   *              
                 ,     %                
            @&@           @&@
            """
    print(ascii_image5)
    weapon_roll = random.choice(small_dice_options)

    # Limit the combat strength to 6
    combat_strength = min(6, (combat_strength + weapon_roll))
    print("    |    The hero's weapon is " + str(weapons[weapon_roll - 1]))

    # Weapon Roll Analysis
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the Weapon roll (Press enter)")
    print("    |", end="    ")
    if weapon_roll <= 2:
        print("--- You rolled a weak weapon, friend")
    elif weapon_roll <= 4:
        print("--- Your weapon is meh")
    else:
        print("--- Nice weapon, friend!")

    # If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
    if weapons[weapon_roll - 1] != "Fist":
        print("    |    --- Thank goodness you didn't roll the Fist...")

    # Roll for player health points
    print("    |", end="    ")
    input("Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(health_points) + " health points")

    # Roll for monster health points
    print("    |", end="    ")
    input("Roll the dice for the monster's health points (Press enter)")
    m_health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(m_health_points) + " health points for the monster")

    # Collect Loot
    belt, loot_options = functions_lab05_starter.collect_loot(loot_options, belt)

    # Use Loot
    belt, health_points = functions_lab05_starter.use_loot(belt, health_points, good_loot_options, bad_loot_options)

    # Roll to see who strikes first
    attack_roll = random.choice(small_dice_options)
    if attack_roll in [1, 3, 5]:
        hero_first = True
    else:
        hero_first = False

    # Fight Sequence
    # Loop while the monster and the player are alive. Call fight sequence functions
    print("You meet the monster. FIGHT!!")
    while m_health_points > 0 and health_points > 0:
        if hero_first:
            input("You strike first (Press Enter)")
            m_health_points = functions_lab05_starter.hero_attacks(combat_strength, m_health_points)
            if m_health_points == 0:
                num_stars = 3
            else:
                input("The monster strikes (Press Enter)")
                health_points = functions_lab05_starter.monster_attacks(m_combat_strength, health_points)
                if health_points == 0:
                    num_stars = 1
                else:
                    num_stars = 2
        else:
            input("The monster strikes first (Press Enter)")
            health_points = functions_lab05_starter.monster_attacks(m_combat_strength, health_points)
            if health_points == 0:
                num_stars = 1
            else:
                input("You strike (Press Enter)")
                m_health_points = functions_lab05_starter.hero_attacks(combat_strength, m_health_points)
                if m_health_points == 0:
                    num_stars = 3
                else:
                    num_stars = 2

    stars = "*" * num_stars

    # Ask for Hero's name
    hero_name = ""
    while True:
        hero_name = input("Enter your Hero's name (in two words): ")
        hero_name_parts = hero_name.split()
        if len(hero_name_parts) == 2 and all(part.isalpha() for part in hero_name_parts):
            break
        else:
            print("Invalid input. Please enter two words with alphabetical characters only.")

    short_name = hero_name_parts[0][:2] + hero_name_parts[1][:1]

    print(f"Hero {short_name} gets <{stars}> stars")

    # Inception Dream Function
    def inception_dream(crazy_level):
        decision = input("Would you like to go deeper into the dream layer? (yes/no): ")
        if decision.lower() == "yes":
            return inception_dream(crazy_level + 1)
        else:
            return crazy_level + 2

    crazy_level = inception_dream(0)
    health_points -= 1
    combat_strength += crazy_level
