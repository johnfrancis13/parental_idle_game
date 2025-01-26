# I want a high score tracker in the game

# Function to save high scores to a file
def save_high_score(score, player_name):
    with open("data\high_scores.txt", "a") as file:
        file.write(f"{player_name}: {score}\n")


# Function to retrieve high scores from a file
def get_high_scores():
    try:
        with open("data\high_scores.txt", "r") as file:
            scores = file.readlines()
        scores = [line.strip() for line in scores]
        # Convert scores to tuples of (score, player_name) and sort them
        scores = [(int(score.split(": ")[1]), score.split(": ")[0]) for score in scores]
        scores.sort(reverse=True, key=lambda x: x[0])
        # Convert back to string format for display
        sorted_scores = [f"{idx+1}. {name}: {score}" for idx, (score, name) in enumerate(scores[:10])]
    except FileNotFoundError:
        sorted_scores = []

    # Fill the remaining spots with "Empty" if fewer than 10 scores
    for i in range(len(sorted_scores), 10):
        sorted_scores.append(f"{i+1}. Empty")
        
    return sorted_scores  


# Function to calculate the high score when the game ends
def calculate_high_score(instance): # instance is the class...
    # for now just have it be the age plus all the attributes
    high_score = int(instance.child.age_days)
    for att,value in instance.child.attributes.items():
        print(att,value)
        high_score+=int(value)
    print(f"You scored {high_score}")
    return(high_score)