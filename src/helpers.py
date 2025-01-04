import random

### Here are how the skills effect child effects
# "Intelligence" - cognitive skills
# "Creativity" - social skills and emotional skills and  cognitive skills
# "Socialization" - social skills and communication skills
# "Empathy" - emotional skills and communication skills
# "Fitness" - physical skills and motor skills
# "Willpower" - Hygiene and motor skills
# "Endurance"- Energy and physical skills
# "Perception"-  Hunger
# "Knowledge" - cognitive skills
# "Prosperity" - daily income

# Questions to think about?
# Should helpers provide a flat additive value, or a multiplier?
# Should helpers have the chance to be actively bad?
# Should helpers be permanent upgrades, or time limited?
# Should their be limits on the number of each type of helpers?

# Here we define a set of functions to manage helpers
class helper:
    def __init__(self,
                 quality: str="bronze"):
        # Initialzie a baseline for each helper before getting into the type specific things
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
        skills_list = ["Intelligence","Creativity", "Socialization","Empathy","Fitness","Willpower",
                        "Endurance","Perception","Knowledge","Prosperity"]
        
        # need to add in the quality factor still
        helper_base_stats = {skills_list[a]:0 for a in range(10)}

        return helper_base_stats
   
    # Allow the created helper to help in developing the child's skills
    def help_develop_skills(self):
        skill_help = {"Motor Skills":self.helper_stats["Willpower"]+self.helper_stats["Fitness"],
                      "Social Skills":self.helper_stats["Creativity"]+self.helper_stats["Socialization"],
                      "Emotional Skills":self.helper_stats["Creativity"]+self.helper_stats["Empathy"],
                      "Communication Skills":self.helper_stats["Empathy"]+self.helper_stats["Socialization"],
                      "Cognitive Skills":self.helper_stats["Creativity"]+self.helper_stats["Intelligence"]+self.helper_stats["Knowledge"],
                      "Physical Development":self.helper_stats["Endurance"]+self.helper_stats["Fitness"]}
        return skill_help

    # Allow the created helper to help in managing the child's needs multiplier for helping Hunger/Hygiene/Energy
    def help_child_maintenance(self):
        needs_help  ={"Hunger":self.helper_stats["Perception"], 
                      "Hygiene":self.helper_stats["Willpower"],
                      "Energy":self.helper_stats["Endurance"]}
        return needs_help

    # Allow the created helper to help with household income, multipler for daily income
    def help_household_income(self):
        return self.helper_stats["Prosperity"]

class partner(helper):
    def __init__(self,quality):
        super().__init__(quality)
        self.type="partner"
        self.helper_stats = self.adjust_skills()
   
    # Assign the base skill points
    def adjust_skills(self):

        skills_dict = {
                        "Intelligence":random.randint(0,2),
                        "Creativity":random.randint(0,2),
                        "Socialization":random.randint(0,2),
                        "Empathy":random.randint(0,2),
                        "Fitness":random.randint(0,2),
                        "Willpower":random.randint(0,4),
                        "Endurance":random.randint(0,2),
                        "Perception":random.randint(0,4),
                        "Knowledge":random.randint(0,2),
                        "Prosperity":random.randint(0,3),
        }
        # Create a new dictionary to store the summed values 
        result_dict = {} 
        # Add the values together 
        for key in skills_dict: 
            result_dict[key] = skills_dict[key] + self.helper_base_stats[key]
        return result_dict

# Assign the base skill points
class babysitter(helper):
    def __init__(self,quality):
        super().__init__(quality)
        self.type="babysitter"
        self.helper_stats = self.adjust_skills()

    def adjust_skills(self):
        skills_dict = {
                        "Intelligence":0,
                        "Creativity":random.randint(0,1),
                        "Socialization":random.randint(0,1),
                        "Empathy":random.randint(0,1),
                        "Fitness":0,
                        "Willpower":random.randint(0,3),
                        "Endurance":random.randint(0,3),
                        "Perception":random.randint(0,3),
                        "Knowledge":0,
                        "Prosperity":0
        }
        # Create a new dictionary to store the summed values 
        result_dict = {} 
        # Add the values together 
        for key in skills_dict: 
            result_dict[key] = skills_dict[key] + self.helper_base_stats[key]
        return result_dict
   
# Assign the base skill points
class relative(helper):
    def __init__(self,quality):
        super().__init__(quality)
        self.relative_type = random.choice(["grandparent","older sibling","younger sibling","fun uncle",
                                           "quirky uncle","fun aunt","quirky aunt","cousin"])
        self.type=self.relative_type
        self.helper_stats = self.adjust_skills()
        
   
    def adjust_skills(self):
        prosperity = random.randint(1,2) if self.relative_type == "grandparent" or "aunt" in self.relative_type or "uncle" in self.relative_type else random.randint(0,1) 
        skills_dict = {
                        "Intelligence":random.randint(0,1),
                        "Creativity":random.randint(0,1),
                        "Socialization":random.randint(0,1),
                        "Empathy":random.randint(0,1),
                        "Fitness":random.randint(0,1),
                        "Willpower":random.randint(0,2),
                        "Endurance":random.randint(0,1),
                        "Perception":random.randint(0,2),
                        "Knowledge":random.randint(0,1),
                        "Prosperity":prosperity,
        }
        # Create a new dictionary to store the summed values 
        result_dict = {} 
        # Add the values together 
        for key in skills_dict: 
            result_dict[key] = skills_dict[key] + self.helper_base_stats[key]
        return result_dict

# Assign the base skill points
class tutor(helper):
    def __init__(self,quality):
        super().__init__(quality)
        self.tutor_type = random.choice(["academic","social","fitness"])
        self.type= str(self.tutor_type+" tutor")
        self.helper_stats = self.adjust_skills()
        
    def adjust_skills(self):
        intelligence = random.randint(1,3) if self.tutor_type == "academic" else random.randint(0,1) 
        socialization = random.randint(1,3) if self.tutor_type == "social" else random.randint(0,1) 
        fitness = random.randint(1,3) if self.tutor_type == "fitness" else random.randint(0,1) 
        skills_dict = {
                        "Intelligence":intelligence,
                        "Creativity":random.randint(0,2),
                        "Socialization":socialization,
                        "Empathy":0,
                        "Fitness":fitness,
                        "Willpower":0,
                        "Endurance":0,
                        "Perception":0,
                        "Knowledge":random.randint(0,2),
                        "Prosperity":0,
        }
        # Create a new dictionary to store the summed values 
        result_dict = {} 
        # Add the values together 
        for key in skills_dict: 
            result_dict[key] = skills_dict[key] + self.helper_base_stats[key]
        return result_dict

# Potentially add other helpers (chef, cleaner, )

# Function to create a helper of a particular type and quality
def create_helper(type="partner",
                  quality="bronze"):
   
    if type=="partner":
        return(partner(quality=quality))
    elif type=="babysitter":
        return(babysitter(quality=quality))
    elif type=="relative":
        return(relative(quality=quality))
    elif type=="tutor":
        return(tutor(quality=quality))
    else:
        raise ValueError(f"Helper type must be one of partner, babysitter, relative, tutor, not {type}")