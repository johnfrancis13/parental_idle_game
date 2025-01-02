import random
# Here we define a set of functions to manage helpers

# Still need some sort of way to determine when a helper

class helper:
    def __init__(self,
                 type: str,
                 quality: str):
        self.type = type
        self.quality = quality
        self.helper_base_stats = self.setup_helper()

    # Create a random helper of a certain quality
    def setup_helper(self):
        if self.quality=="bronze":
            quality_factor = 1
        elif self.quality=="silver":
            quality_factor = 2
        elif self.quality=="gold":
            quality_factor = 3
        elif self.quality=="platinum":
            quality_factor = 5
        elif self.quality=="diamond":
            quality_factor = 10
        elif self.quality=="master":
            quality_factor = 20
        else:
            raise ValueError(f"Helper quality {self.quality} is not a valid quality. Must be one of 'bronze','silver','gold','platinum','diamond','master'")

        # Choose a set of random
        helper_base_stats = [random.randint(1,3*quality_factor) for a in range(10)]
        return(helper_base_stats)
   
    # Allow the created helper to help in raising the children
    def help(self):
        return 

class partner(helper):
    def __init__(self):
        self.helper_stats = self.setup_skills()
   
    # Assign the base skill points
    def setup_skills(self):

        skills_dict = {
            "Intelligence":1,
                              "Creativity":1,
                              "Socialization":1,
                              "Empathy":1,
                              "Fitness":1,
                              "Willpower":1,
                              "Endurance":1,
                              "Perception":1,
                              "Knowledge":1,
                              "Prosperity":1
        }
        return {skills_dict}

# Assign the base skill points
class babysitter(helper):
    def __init__(self):
        self.helper_stats = self.setup_skills()

    def setup_skills(self):
        skills_dict = {
           
        }
        return {skills_dict}
   
# Assign the base skill points
class relative(helper):
    def __init__(self):
        self.helper_stats = self.setup_skills()
        self.relative_type = random.choice("grandparent","older sibling","younger sibling","fun uncle","quirk uncle","fun aunt","quirky aunt","cousin")
   
    def setup_skills(self):
        skills_dict = {
           
        }
        return {skills_dict}

# Assign the base skill points
class tutor(helper):
    def __init__(self):
        self.helper_stats = self.setup_skills()

    def setup_skills(self):
        skills_dict = {
           
        }
        return {skills_dict}


# Function to create a helper of a particular type and quality
def create_helper(type="partner",
                  quality="bronze"):
   
    if type=="partner":
        return(partner(quality==quality))
    elif type=="babysitter":
        return(babysitter(quality==quality))
    elif type=="relative":
        return(relative(quality==quality))
    elif type=="tutor":
        return(tutor(quality==quality))
    else:
        raise ValueError(f"Helper type must be one of partner, babysitter, relative, tutor, not {type}")