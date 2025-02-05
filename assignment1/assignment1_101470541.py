# Author: Thinh Phan
# Assignment: #1

# Data type: String
gym_member = "Alex Alliton"

# Data type: Float
preferred_weight_kg = 20.5

# Data type: Integer
highest_reps = 25

# Data type: Boolean
membership_active = True

# Dictionary
# Key: Friend's name (string)
# Value: Tuple of workout minutes (int: yoga, running, weightlifting)
workout_stats = {
    "Alvin": (45, 40, 35),
    "Simon": (35, 30, 25),
    "Theodore": (25, 20, 25)
}

# Calculate total workout minutes for each friend and store in separate dictionary
total_workout = {}
for friend, minutes in workout_stats.items():
    total_minutes = sum(minutes)
    total_workout[f"{friend}_Total"] = total_minutes

# Update: workout_stats with total workout minutes
workout_stats.update(total_workout)

# 2D list: Extract workout minutes from dictionary
# Data type: 2-dimensional (nested) list
workout_list = [list(minutes) for friend, minutes in workout_stats.items() if not friend.endswith("_Total")]

# Slicing workout_list
print("Yoga and Running Minutes:")
for row in workout_list:
    print(row[:2])

print("Weightlifting Minutes for Last Two Friends:")
for row in workout_list[-2:]:
    print(row[2])

# Checking for friends who worked out >= 120 minutes
for friend, total in total_workout.items():
    if total >= 120:
        print(f"Great job staying active, {friend.replace('_Total', '')}!")

# User input to check workout stats
friend_name = input("Enter a friend's name: ")
if friend_name in workout_stats:
    print(f"{friend_name}'s workout stats: {workout_stats[friend_name]}")
    print(f"Total workout minutes: {workout_stats[friend_name + '_Total']}")
else:
    print(f"Friend {friend_name} not found in the records.")

# Finding highest and lowest total workout minutes
max_friend = max(total_workout, key=total_workout.get).replace("_Total", "")
min_friend = min(total_workout, key=total_workout.get).replace("_Total", "")
print(f"Friend with highest workout minutes: {max_friend}")
print(f"Friend with lowest workout minutes: {min_friend}")
