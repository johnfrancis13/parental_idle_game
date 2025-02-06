import random
# Traits that can be passed down
traits = {
    "physical_traits": {
        "positive": ["tall", "slim", "athletic", "strong", "healthy_skin", "beautiful_eyes", "good_posture", "fit", "energetic"],
        "negative": ["short", "lazy", "hairy", "balding", "frail", "uncoordinated", "prone_to_injury", "obese", "poor_vision"]
    },
    "personality_traits": {
        "positive": ["extroverted", "optimistic", "patient", "empathetic", "creative", "charismatic", "honest", "adaptable", "decisive"],
        "negative": ["pessimistic", "impatient", "stubborn", "indifferent", "irritable", "arrogant", "jealous", "moody", "selfish"]
    },
    "cognitive_abilities": {
        "positive": ["quick_learner", "logical_thinker", "creative", "good_memory", "analytical", "problem_solver", "innovative", "observant", "detail_oriented"],
        "negative": ["slow_learner", "forgetful", "average_memory", "disorganized", "struggles_with_math", "easily_distracted", "poor_concentration", "lack_of_focus", "poor_judgment"]
    },
    "talents_hobbies": {
        "positive": ["musically_inclined", "artistic", "athletic", "good_cook", "public_speaker", "quick_reader", "dancer", "mechanic", "engineer", "jogger", "gardening", "coding", "photography", "writing", "crafting"],
        "negative": ["tone_deaf", "poor_hand-eye_coordination", "gambling", "watching_tv", "collecting_stamps", "shopping", "doing_puzzles", "playing_video_games", "addiction", "overindulgence", "hoarding"]
    },
    "psychological_traits": {
        "positive": ["resilient", "confident", "sensitive", "curious", "self-aware", "emotional_intelligence", "brave", "optimistic", "compassionate"],
        "negative": ["anxious", "low_self-esteem", "fearful", "moody", "distrustful", "depressed", "paranoid", "insecure", "obsessive"]
    },
    "behavioral_patterns": {
        "positive": ["organized", "punctual", "tidy", "outgoing", "discipline", "reliable", "diligent", "responsible", "considerate"],
        "negative": ["procrastinator", "untidy", "late", "impulsive", "shy", "lazy", "neglectful", "disorganized", "reckless"]
    },
    "health_traits": {
        "positive": ["fast_metabolism", "strong_immune_system", "high_endurance", "robust", "active", "resistant_to_allergies", "flexible", "good_recovery", "fit"],
        "negative": ["allergies", "prone_to_injuries", "prone_to_illness", "low_energy", "weak_immune_system", "chronic_pain", "obesity", "sleep_disorders", "chronic_fatigue"]
    },
    "ethical_and_moral_values": {
        "positive": ["honesty", "kindness", "integrity", "generosity", "respectfulness", "fairness", "loyalty", "humility", "responsibility"],
        "negative": ["dishonest", "selfish", "inconsiderate", "rude", "irresponsible", "greedy", "deceptive", "manipulative", "vindictive"]
    }
}


def create_random_start_traits(level="regular",num_starting_traits=3):
    '''
    Function to create a random set of traits
    level = ["easy","regular","hard"] # difficulty
    num_starting_traits = int() # number of traits you start with, default 3
    '''
    if num_starting_traits<2 or num_starting_traits>=5:
        raise ValueError("The number of starting traits must be 2,3 or 4 in this version of the game")

    level = level.lower()
    if "easy" in level:
        if num_starting_traits==2:
            weights = [.05,.25,.7]
        elif num_starting_traits==3:
            weights = [0.05, 0.15, 0.2, 0.6]
        elif num_starting_traits==4:
            weights = [0.05,.1,.2,.3,.35]
    elif "regular" in level:
        if num_starting_traits==2:
            weights = [.15,.6,.25]
        elif num_starting_traits==3:
            weights = [0.1, 0.2, 0.5, 0.2]
        elif num_starting_traits==4:
            weights = [0.1,.15,.2,.35,.2]
    elif "hard" in level:
        if num_starting_traits==2:
            weights = [.65,.25,.1]
        elif num_starting_traits==3:
            weights = [0.5, 0.25, 0.15, 0.1]
        elif num_starting_traits==4:
            weights = [.35,.3,.2,.1,.05]
    else:
        raise ValueError("level must be one of easy,regular, or hard")

    choices = [a for a in range(num_starting_traits+1)]
    
    pos_list = random.choices(choices, weights=weights, k=8)
    print(pos_list)
    neg_list = [num_starting_traits-a for a in pos_list]
    
    starting_weights= {}

    i=0
    for key in traits:
        temp_pos = random.sample(traits[key]["positive"],pos_list[i])
        temp_neg = random.sample(traits[key]["negative"],neg_list[i])
        starting_weights[key]= temp_pos + temp_neg
        i+=1
    

    return starting_weights