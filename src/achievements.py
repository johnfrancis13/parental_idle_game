# Want an achievement tracker in the game - this would need to be tied to an account, a machine, or something
import json
from tkinter import messagebox
 
# Sample achievement data
achievements_data = [
    {"name": "Start the game", "description": "You started for the first time!", "unlocked": False,"id": 1},
    {"name": "Reach Infancy", "description": "Your child has survived until infancy!", "unlocked": False,"id": 2},
    {"name": "Reach Toddler", "description": "Your child has survived long enough to become a toddler!", "unlocked": False,"id": 3},
    {"name": "Reach Preschooler", "description": "Your child has survived long enough to become a preschooler!", "unlocked": False,"id": 4},
    {"name": "Reach Adolescent", "description": "Your child has survived long enough to become a adolescent!", "unlocked": False,"id": 5},
    {"name": "Reach Pre-teen", "description": "Your child has survived long enough to become a pre-teen!", "unlocked": False,"id": 6},
    {"name": "Reach Teen", "description": "Your child has survived long enough to become a teen!", "unlocked": False,"id": 7},
    {"name": "Finish the game", "description": "For the first time, your child has survived until adulthood!", "unlocked": False,"id": 8},
]


# Define criteria functions separately
criteria_functions = {
    1: lambda turns: turns >= 1,
    2: lambda turns: turns >= 90,
    3: lambda turns: turns >= 365,
    4: lambda turns: turns >= 1095,
    5: lambda turns: turns >= 2190,
    6: lambda turns: turns >= 4015,
    7: lambda turns: turns >= 4745,
    8: lambda turns: turns >= 6570
}

# Save achievements to a JSON file
def save_achievements(achievements):
    with open("data/achievements.json", "w") as file:
        json.dump(achievements, file)

# Check and update achievements
def check_achievements(instance):
    achievements = load_achievements()
    updated = False
    
    for achievement in achievements:
        if not achievement["unlocked"] and criteria_functions[achievement["id"]](instance.turn_count):
            achievement["unlocked"] = True
            updated = True
            notify_achievement(achievement["name"],achievement["description"])
    
    if updated:
        save_achievements(achievements)

# Notify player of new achievement
def notify_achievement(name,description):
    messagebox.showinfo("Achievement Unlocked", f"Achievement Unlocked: {name}. {description}")

# Load achievements from a JSON file
def load_achievements():
    with open("data/achievements.json", "r") as file:
        return json.load(file)