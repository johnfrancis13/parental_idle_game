import random
# Traits that can be passed down
traits = {
    "physical_traits": {
        "positive": ["tall", "slim", "athletic", "strong", "healthy skin", "beautiful eyes", "good posture", "fit", "energetic"],
        "negative": ["short", "lazy", "hairy", "balding", "frail", "uncoordinated", "prone to injury", "obese", "poor vision"]
    },
    "personality_traits": {
        "positive": ["extroverted", "optimistic", "patient", "empathetic", "creative", "charismatic", "honest", "adaptable", "decisive"],
        "negative": ["pessimistic", "impatient", "stubborn", "indifferent", "irritable", "arrogant", "jealous", "moody", "selfish"]
    },
    "cognitive_abilities": {
        "positive": ["quick learner", "logical thinker", "creative", "good memory", "analytical", "problem solver", "innovative", "observant", "detail oriented"],
        "negative": ["slow learner", "forgetful", "average memory", "disorganized", "struggles with math", "easily distracted", "poor concentration", "lack of focus", "poor judgment"]
    },
    "talents_hobbies": {
        "positive": ["musically inclined", "artistic", "athletic", "good cook", "public speaker", "quick reader", "dancer", "mechanic", "engineer", "jogger", "gardening", "coding", "photography", "writing", "crafting"],
        "negative": ["tone deaf", "poor hand-eye coordination", "gambling", "watching tv", "collecting stamps", "shopping", "doing puzzles", "playing video games", "addiction", "overindulgence", "hoarding"]
    },
    "psychological_traits": {
        "positive": ["resilient", "confident", "sensitive", "curious", "self-aware", "emotional intelligence", "brave", "optimistic", "compassionate"],
        "negative": ["anxious", "low self-esteem", "fearful", "moody", "distrustful", "depressed", "paranoid", "insecure", "obsessive"]
    },
    "behavioral_patterns": {
        "positive": ["organized", "punctual", "tidy", "outgoing", "discipline", "reliable", "diligent", "responsible", "considerate"],
        "negative": ["procrastinator", "untidy", "late", "impulsive", "shy", "lazy", "neglectful", "disorganized", "reckless"]
    },
    "health_traits": {
        "positive": ["fast metabolism", "strong immune system", "high endurance", "robust", "active", "resistant to allergies", "flexible", "good recovery", "fit"],
        "negative": ["allergies", "prone to injuries", "prone to illness", "low energy", "weak immune system", "chronic pain", "obesity", "sleep disorders", "chronic fatigue"]
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