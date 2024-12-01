import random
import textwrap
import skill_thresholds

# Definte the Parental Unit class which will hold all of the information about the player (attributes, skills, abilities, relationships, etc.)
class parental_unit():
    def __init__(self,
                 name,
                 level=0,
                 num_of_children=1,
                 profession = "Stay at home parent",
                 attribute_bonuses = {},
                 helpers = {},
                 skills= {},
                 history = {}):
        self.name = name
        self.history = history # things from previous runs that may give bonuses or negatives
        self.level = level
        self.num_of_children = num_of_children
        self.profession = profession

        if level ==0: # at the beginning of the game you don't start with any bonuses - or point buy for the first round? maybe point buy AFTER the first round
            self.attributes = self.setup_attributes(base=True)
            self.helpers = self.setup_helpers(base =True)
            self.skills = self.setup_skills(base =True)
        else:
            self.attributes = self.setup_attributes(base=False,
                                                  bonuses=attribute_bonuses)
            self.helpers = self.setup_helpers(base =False,
                                              helpers=helpers)
            self.skills = self.setup_skills(base =False,
                                            skills=skills)
    
    def examine_self(self):
        print(f"My name is {self.name}. I have {self.num_of_children} {'child' if self.num_of_children==1 else 'children'}.")
        print(f"My current attributes are: {self.attributes}.")
        print(f"To help me raise my offspring I currently have a {' and a'.join([key for key in self.helpers if self.helpers[key] is not None])}.")
        print(f"The skills I have developed are: {' '.join([self.skills[key] for key in self.skills if self.skills[key] is not None])}.")
        print(f"My current profession is: {self.profession}.")

    def examine_self_return(self):
        return(f"""
               My name is {self.name}. I have {self.num_of_children} {'child' if self.num_of_children==1 else 'children'}.
               My current attributes are: 
               {self.attributes}.
               To help me raise my offspring I currently have a {' and a'.join([key for key in self.helpers if self.helpers[key] is not None])}.
               The skills I have developed are: 
               {' '.join([self.skills[key] for key in self.skills if self.skills[key] is not None])}
               My current profession is: 
               {self.profession}.
               """)


    def setup_attributes(self,
                       base,
                       bonuses={}):
        # Initialize attributes
        attribute_dict = {"Intelligence":1,
                              "Creativity":1,
                              "Socialization":1,
                              "Empathy":1,
                              "Fitness":1,
                              "Willpower":1,
                              "Endurance":1,
                              "Perception":1,
                              "Knowledge":1,
                              "Prosperity":1}
        # If base==False add bonuses to the attribute dict
        if base==False:
            attribute_dict = {key: bonuses[key] + attribute_dict[key] for key in attribute_dict}
        return(attribute_dict)
    
    
    def setup_helpers(self,
                      base,
                      helpers={}):
        # Initialize helpers
        max_helpers = 10
        tutor_dict = dict.fromkeys(f"{'tutor'}_{i}" for i in range(1, max_helpers + 1))
        babysitter_dict = dict.fromkeys(f"{'babysitter'}_{i}" for i in range(1, max_helpers + 1))
        family_dict = dict.fromkeys(f"{'family_member'}_{i}" for i in range(1, max_helpers + 1))
        base_dict = {"spouse": {"Intelligence":1,
                              "Creativity":1,
                              "Socialization":1,
                              "Empathy":1,
                              "Fitness":1,
                              "Willpower":1,
                              "Endurance":1,
                              "Perception":1,
                              "Knowledge":1,
                              "Prosperity":1},
                       "chef":None,
                       "cleaner":None}
        
        helper_dict = base_dict | tutor_dict | babysitter_dict | family_dict

        if base==False:
            helper_dict = {key1: {key2: helpers[key1][key2] + helper_dict[key1][key2] for key2 in helper_dict[key1]} for key1 in helper_dict}
    
        return(helper_dict)
    
    def setup_skills(self,
                     base,
                     skills={}):
    
        skills_dict = {"Intelligence":None,
                       "Creativity":None,
                       "Socialization":None,
                       "Empathy":None,
                       "Fitness":None,
                       "Willpower":None,
                       "Endurance":None,
                       "Perception":None,
                       "Knowledge":None,
                       "Prosperity":None}
        
        if base==False:
            skills_dict = {key: skills[key] for key in skills_dict}

        return(skills_dict)

class baby():
    def __init__(self,
                 name,
                 gender):
        self.name=name
        self.gender=gender
        self.age_days=0
        self.age="Newborn"
        if gender == "boy":
            self.weight = round(random.uniform(6.5, 9.5),2)
            self.height = round(random.uniform(17.5, 23),2)
        if gender == "girl":
            self.weight = round(random.uniform(6, 9),2)
            self.height = round(random.uniform(17, 22.5),2)

        self.daily_needed_sleep = 17
        self.daily_hunger = 7

        if self.age=="Newborn":
            self.attributes=self.setup_attributes(age=self.age)
            self.skills = self.setup_skills(base =True)
            self.needs = self.setup_needs(base=True) 
            self.natural_inclinations = self.setup_natural_inclinations(base=True)   


    def examine_child(self):
        return(self.attributes, self.needs, {
                "Name":self.name,
                "Age (category)":self.age,
                "Age (days)":self.age_days,
                "Weight (lbs)":round(self.weight,3),
                "Height (in)":round(self.height,3)},
                self.skills,
                f"""{self.name}'s current inclinations are: {self.natural_inclinations}""")
#                    {wrapped_summary}""")
    
    def setup_attributes(self,
                         age,
                         bonuses={}):
        if age=="Newborn":
            attributes = {
                "Motor Skills":0,
                "Social Skills":0,
                "Emotional Skills":0,
                "Communication Skills":0,
                "Cognitive Skills":0,
                "Physical Development":0}
        if age=="Infant":
            attributes = attributes+bonuses
        if age=="Toddler":
            attributes = attributes+bonuses
        if age=="Preschooler":
            attributes = attributes+bonuses        
        if age=="Adolescent":
            attributes = attributes+bonuses
        if age=="Pre-teen":
            attributes = attributes+bonuses
        if age=="Teen":
            attributes = attributes+bonuses        
        return(attributes)
    
    def grow_up(self,
                new_age, 
                current_attributes):
        self.attributes = self.setup_attributes(new_age,
                                                current_attributes)
        
        if new_age=="Adolescent":
            self.childs_goal = self.select_random_goal()

        print(f"Your child has now grown to: {new_age}")
        
    def select_random_goal(self):
        possible_goal_list = ["Become an athlete","Become a lawyer","Become a doctor","Get married young","Travel the world",
                              "Get into politics","Become an influencer","Get rich quick"]
        return(random.choice(possible_goal_list))
    
    def setup_skills(self,
                     base,
                     skills={}):
    
        skills_dict = {"Motor Skills":[],
                       "Social Skills":[],
                       "Emotional Skills":[],
                       "Communication Skills":[],
                       "Cognitive Skills":[],
                       "Physical Development":[]}
        
        if base==False:
            skills_dict = {key: skills[key] for key in skills_dict}

        return(skills_dict)
    
    def setup_needs(self,
                     base,
                     needs={}):
    
        needs_dict = {"Hunger":75, # need food to stay happy/healthy
                      "Hygiene":75, # cleanliness to stay happy/healthy
                      "Energy":75, # energy to do activities before collapsing
                      "Happiness":50, # higher happiness affects performance on tasks
                      "Health":50, # poor health prevents some activities
                      "Love for Parent":75, # affects how amenable child is to activities
                      "Fear of Parent":75, #  affects how amenable child is to activities
                      "Current Physical State":"healthy",
                      "Current Mental State":"content"}
        
        if base==False:
            needs_dict = {key: needs[key] for key in needs_dict}

        return(needs_dict)
    
    def setup_natural_inclinations(self,
                                   base,
                                   inclinations={}):
        possible_inclinations = ["Hungry","Sleepy","Sickly","Emotive","Active","Curious","Calm","Sociable","Playful"]
        
        num_of_inclinations = random.randint(1, 4)
        natural_inclinations_dict = random.sample(possible_inclinations, num_of_inclinations)
        
        # Gain/Lose Inclinations when you grow up
        if base==False:
            natural_inclinations_dict = [inclination for inclination in natural_inclinations_dict]

        return(natural_inclinations_dict)

    # check attributes and inclinations
    def update_inclinations(self):
        # check Happiness
        if self.needs["Happiness"]>50:
            self.natural_inclinations.append(random.choices(["Emotive","Active","Curious","Calm","Sociable","Playful","Joyful","Alert","Giggly"], k=1)[0])
            self.natural_inclinations = [item for item in self.natural_inclinations if item not in  ["Detached","Passive","Uninterested","Anxious","Unsociable","Serious","Fussy","Irritable","Distressed"]]
            self.natural_inclinations = list(set(self.natural_inclinations))
            if self.needs["Happiness"]>90:
                self.natural_inclinations = list(set(self.natural_inclinations))[:4]
            elif self.needs["Happiness"]>80:
                self.natural_inclinations = list(set(self.natural_inclinations))[:3]
            elif self.needs["Happiness"]>70:
                self.natural_inclinations = list(set(self.natural_inclinations))[:2]
            elif self.needs["Happiness"]>50:
                self.natural_inclinations = list(set(self.natural_inclinations))[:1]
        else:
            self.natural_inclinations = [item for item in self.natural_inclinations if item not in  ["Emotive","Active","Curious","Calm","Sociable","Playful","Joyful","Alert","Giggly"]]
            self.natural_inclinations.append(random.choices(["Detached","Passive","Uninterested","Anxious","Unsociable","Serious","Fussy","Irritable","Distressed"], k=1)[0])
            self.natural_inclinations = list(set(self.natural_inclinations))
            if self.needs["Happiness"]<10:
                self.natural_inclinations = list(set(self.natural_inclinations))[:4]
            elif self.needs["Happiness"]<20:
                self.natural_inclinations = list(set(self.natural_inclinations))[:3]
            elif self.needs["Happiness"]<30:
                self.natural_inclinations = list(set(self.natural_inclinations))[:2]
            elif self.needs["Happiness"]<=50:
                self.natural_inclinations = list(set(self.natural_inclinations))[:1]

        # check Hunger
        if self.needs["Hunger"]<25:
            self.natural_inclinations.append("Hungry")
            self.natural_inclinations = list(set(self.natural_inclinations))
        else:
            self.natural_inclinations = [item for item in self.natural_inclinations if item != "Hungry"]
        
        # check Energy
        if self.needs["Energy"]<25:
            self.natural_inclinations.append("Sleepy")
            self.natural_inclinations = list(set(self.natural_inclinations))
        else:
            self.natural_inclinations = [item for item in self.natural_inclinations if item != "Sleepy"]

        # check Hygiene
        if self.needs["Hygiene"]<25:
            self.natural_inclinations.append("Dirty")
            self.natural_inclinations = list(set(self.natural_inclinations))
        else:
            self.natural_inclinations = [item for item in self.natural_inclinations if item != "Dirty"]
        
        # check Health
        if 0 < self.needs["Health"] < 20:
            self.needs["Current Physical State"] = "Critically ill" 
        elif 20 <= self.needs["Health"] < 40:
            self.needs["Current Physical State"] = "Sickly"
        elif 40 <= self.needs["Health"] < 60:
            self.needs["Current Physical State"] = "Mediocre"
        elif 60 <= self.needs["Health"] < 80:
            self.needs["Current Physical State"] = "Mostly Healthy"
        elif 80 <= self.needs["Health"] < 100:
            self.needs["Current Physical State"] = "Very Healthy"
        elif self.needs["Health"] == 100:
            self.needs["Current Physical State"] = "Optimally Fit"              

        # check mental
        if self.needs["Love for Parent"] == 0:
            self.needs["Current Mental State"] = "Unhinged" 
        if 0 < self.needs["Love for Parent"] < 20:
            self.needs["Current Mental State"] = "Distressed" 
        elif 20 <= self.needs["Love for Parent"] < 40:
            self.needs["Current Mental State"] = "Struggling"
        elif 40 <= self.needs["Love for Parent"] < 60:
            self.needs["Current Mental State"] = "Indifferent"
        elif 60 <= self.needs["Love for Parent"] < 80:
            self.needs["Current Mental State"] = "Content"
        elif 80 <= self.needs["Love for Parent"] < 100:
            self.needs["Current Mental State"] = "Thriving"
        elif self.needs["Love for Parent"] == 100:
            self.needs["Current Mental State"] = "Joyous" 

        if self.needs["Health"]<50:
            self.natural_inclinations.append("Sickly")
            self.natural_inclinations = list(set(self.natural_inclinations))
        else:
            self.natural_inclinations = [item for item in self.natural_inclinations if item != "Sickly"]

        if self.needs["Love for Parent"]<50:
            self.natural_inclinations.append("Struggling")
            self.natural_inclinations = list(set(self.natural_inclinations))
        else:
            self.natural_inclinations = [item for item in self.natural_inclinations if item != "Struggling"]

        

    # check attributes for skills breakpoints
    def update_skills(self):
        # Get the right skill thresholds based on age
        skill_threshold_dict = {"Newborn":skill_thresholds.skill_thresholds_young,
                                "Infant":skill_thresholds.skill_thresholds_young,
                                "Toddler":skill_thresholds.skill_thresholds_young,
                                "Preschooler":skill_thresholds.skill_thresholds_school,
                                "Adolescent":skill_thresholds.skill_thresholds_school,
                                "Pre-teen":skill_thresholds.skill_thresholds_school,
                                "Teen":skill_thresholds.skill_thresholds_high_school}
        
        # Check for added skills
        for attribute, points in self.attributes.items():
            if attribute in skill_threshold_dict[self.age]:
                for threshold, skill in sorted(skill_threshold_dict[self.age][attribute].items()):
                    if points >= threshold and skill not in self.skills[attribute]: 
                        self.skills[attribute].append(skill)


    # Baseline updates to all features that happens every day
    def update_turn(self, age):
        if age=="Newborn":
            # Needs
            self.needs["Hunger"] = self.needs["Hunger"] - self.daily_hunger*2 # require food
            self.needs["Hygiene"] = self.needs["Hygiene"] - 8 # require cleaning
            self.needs["Energy"] = self.needs["Energy"] - self.daily_needed_sleep*2 # require sleep
            self.needs["Love for Parent"] = self.needs["Love for Parent"] - 4 # require bonding time
            self.age_days +=1

            # Every 5 days randomize
            if self.age_days>1 and self.age_days%5==0:
                self.daily_needed_sleep = random.choice([14,15,16,17])
                self.daily_hunger = random.choice([5,6,7,8,9])

        if age=="Infant":
            # Needs
            self.needs["Hunger"] = self.needs["Hunger"] - self.daily_hunger*2 # require food
            self.needs["Hygiene"] = self.needs["Hygiene"] - 12
            self.needs["Energy"] = self.needs["Energy"]  - self.daily_needed_sleep*2 # require sleep
            self.needs["Love for Parent"] = self.needs["Love for Parent"] - 4 # require bonding time
            self.age_days +=1

            # Every 5 days randomize
            if self.age_days>1 and self.age_days%5==0:
                self.daily_needed_sleep = random.choice([12,13,14,15,16])
                self.daily_hunger = random.choice([5,6,7,8,9])

        if age=="Toddler":
            # Needs
            self.needs["Hunger"] = self.needs["Hunger"] - self.daily_hunger*2 # require food
            self.needs["Hygiene"] = self.needs["Hygiene"] - 8
            self.needs["Energy"] = self.needs["Energy"]  - self.daily_needed_sleep*2 # require sleep
            self.needs["Love for Parent"] = self.needs["Love for Parent"] - 3 # require bonding time
            self.age_days +=1

            # Every 5 days randomize
            if self.age_days>1 and self.age_days%5==0:
                self.daily_needed_sleep = random.choice([11,12,13,14])
                self.daily_hunger = random.choice([5,6,7,8,9])

        if age=="Preschooler":
            # Needs
            self.needs["Hunger"] = self.needs["Hunger"] - self.daily_hunger*2 # require food
            self.needs["Hygiene"] = self.needs["Hygiene"] - 6
            self.needs["Energy"] = self.needs["Energy"]  - self.daily_needed_sleep*2 # require sleep
            self.needs["Love for Parent"] = self.needs["Love for Parent"] - 2 # require bonding time
            self.age_days +=1
            # Every 10 days randomize
            if self.age_days>1 and self.age_days%30==0:
                self.daily_needed_sleep = random.choice([10,11,12,13])
                self.daily_hunger = random.choice([5,6,7,8,9])
        
        if age=="Adolescent":
            # Needs
            self.needs["Hunger"] = self.needs["Hunger"] - self.daily_hunger*2 # require food
            self.needs["Hygiene"] = self.needs["Hygiene"] - 4
            self.needs["Energy"] = self.needs["Energy"]  - self.daily_needed_sleep*2 # require sleep
            self.needs["Love for Parent"] = self.needs["Love for Parent"] - 1 # require bonding time
            self.age_days +=1
            # Every 10 days randomize
            if self.age_days>1 and self.age_days%90==0:
                self.daily_needed_sleep = random.choice([9,10,11,12])
                self.daily_hunger = random.choice([5,6,7,8,9])

        if age=="Pre-teen":
            # Needs
            self.needs["Hunger"] = self.needs["Hunger"] - self.daily_hunger*2 # require food
            self.needs["Hygiene"] = self.needs["Hygiene"] - 4
            self.needs["Energy"] = self.needs["Energy"]  - self.daily_needed_sleep*2 # require sleep
            self.needs["Love for Parent"] = self.needs["Love for Parent"] - .5 # require bonding time
            self.age_days +=1
            # Every 10 days randomize
            if self.age_days>1 and self.age_days%180==0:
                self.daily_needed_sleep = random.choice([8,9,10,11])
                self.daily_hunger = random.choice([5,6,7,8,9])

        if age=="Teen":
            # Needs
            self.needs["Hunger"] = self.needs["Hunger"] - self.daily_hunger*2 # require food
            self.needs["Hygiene"] = self.needs["Hygiene"] - 6 # POTENTIALLY adjust this based on their preference for how much they care about appearances
            self.needs["Energy"] = self.needs["Energy"]  - self.daily_needed_sleep*2 # require sleep
            self.needs["Love for Parent"] = self.needs["Love for Parent"] - .25 # require bonding time
            self.age_days +=1
            # Every 10 days randomize
            if self.age_days>1 and self.age_days%300==0:
                self.daily_needed_sleep = random.choice([7,8,9,10,11])
                self.daily_hunger = random.choice([5,6,7,8,9])
        
        # Check Health/Happiness
        for turn_need in ["Hygiene","Hunger","Energy"]:
            if self.needs[turn_need]<25:
                self.needs["Health"] = self.needs["Health"] - 1
                self.needs["Happiness"] = self.needs["Happiness"] - 1
                if self.needs[turn_need]<10:
                    self.needs["Health"] = self.needs["Health"] - 3
                    self.needs["Happiness"] = self.needs["Happiness"] - 3
        
        # Add condition to improve Health/Happiness
        if self.needs["Hygiene"] > 50 and self.needs["Hunger"] > 50 and self.needs["Energy"] > 50:
            self.needs["Health"] = self.needs["Health"] + 1
            self.needs["Happiness"] = self.needs["Happiness"] + 1
        if self.needs["Hygiene"] > 75 and self.needs["Hunger"] > 75 and self.needs["Energy"] > 75:
            self.needs["Health"] = self.needs["Health"] + 3
            self.needs["Happiness"] = self.needs["Happiness"] + 3

        # Note: Happiness should be tied to 

        # Update inclinations
        self.update_inclinations()

        # Update Skills
        self.update_skills()
        
        # Ensure values stay within (0,100)
        for category, label in self.needs.items():
            try: 
                value = int(label)
                if value < 0: 
                    self.needs[category] = 0
                elif value > 100:
                    self.needs[category] = 100
            except ValueError:
                continue

        # Age up at each breakpoint
        if self.age_days>=90:
            self.age="Infant"
        if self.age_days>=365:
            self.age="Toddler"
        if self.age_days>=1095:
            self.age="Preschooler"
        if self.age_days>=2190:
            self.age="Adolescent"
        if self.age_days>=4015:
            self.age="Pre-teen"
        if self.age_days>=4745:
            self.age="Teen"
        if self.age_days>=6570:
            self.age="Grown"

    def current_inclination_factor(self):

        negative_factors = len([a for a in self.natural_inclinations if a in ["Detached","Passive","Uninterested","Anxious","Unsociable","Serious","Hungry","Sleepy","Sickly","Dirty","Struggling"]])
        positive_factors = len([a for a in self.natural_inclinations if a in ["Emotive","Active","Curious","Calm","Sociable","Playful"]])
        happiness = 1 if self.needs["Happiness"]>=50 else -1
        i_f = positive_factors - negative_factors + happiness

        return(i_f)
        

    # Function to determine skill development dependent on action type
    def develop_skill(self,action):
        if action=="Play":
            # choose a skill
            selected_skill = random.choices(["Social Skills", "Emotional Skills","Communication Skills","Physical Development"],
                                            weights=[2,1,1,2], k=1)[0]
            # choose a development amount
            development_level = random.choices([-2,-1,0,1,2,3,4,5],
                                                weights=[1,2,5,70,15,4,2,1], k=1)[0]
            
            # adjust development_level based on current inclinations
            development_level = development_level + self.current_inclination_factor()

            # don't less this number get out of hand
            if development_level<0:
                development_level=0
            if development_level>5:
                development_level=5

            return {selected_skill:development_level}
        
        if action=="Teach":
            # choose a skill
            selected_skill = random.choices(["Motor Skills","Communication Skills","Cognitive Skills"],
                                            weights=[2,1,4], k=1)[0]
            # choose a development amount
            development_level = random.choices([-2,-1,0,1,2,3,4,5],
                                                weights=[1,2,5,70,15,4,2,1], k=1)[0]
            
            # adjust development_level based on current inclinations
            development_level = development_level + self.current_inclination_factor()

            # don't less this number get out of hand
            if development_level<0:
                development_level=0
            if development_level>5:
                development_level=5

            return {selected_skill:development_level}
        
        if action=="Bonding Time":
            # choose a skill
            selected_skill = random.choices(["Motor Skills","Emotional Skills","Communication Skills"],
                                            weights=[1,3,1], k=1)[0]
            # choose a development amount
            development_level = random.choices([-2,-1,0,1,2,3,4,5],
                                                weights=[1,2,5,70,15,4,2,1], k=1)[0]
            
            # adjust development_level based on current inclinations
            development_level = development_level + self.current_inclination_factor()

            # don't less this number get out of hand
            if development_level<0:
                development_level=0
            if development_level>5:
                development_level=5

            return {selected_skill:development_level}
        
    def determine_weight_gain_by_age(self):
        if self.age=="Newborn":
            if self.gender=="boy":
                return(round(random.uniform(0.04425, 0.0670),3))
            else:
                return(round(random.uniform(0.04175, 0.0610),3))

        if self.age=="Infant":
            if self.gender=="boy":
                return(round(random.uniform(0.025, 0.0485),3))
            else:
                return(round(random.uniform(0.0225, 0.04585),3))

        if self.age=="Toddler":
            if self.gender=="boy":
                return(round(random.uniform(0.015625, 0.01925),3))
            else:
                return(round(random.uniform(0.015425, 0.01895),3))

        if self.age=="Preschooler":
            if self.gender=="boy":
                return(round(random.uniform(0.010825, 0.013425),3))
            else:
                return(round(random.uniform(0.010525, 0.013225),3))
            
        if self.age=="Adolescent":
            if self.gender=="boy":
                return(round(random.uniform(0.013225, 0.021),3))
            else:
                return(round(random.uniform(0.013025, 0.020),3))

        if self.age=="Pre-teen":
            if self.gender=="boy":
                return(round(random.uniform(0.01675, 0.0325),3))
            else:
                return(round(random.uniform(0.01875, 0.0375),3)) # girls outpace boys

        if self.age=="Teen":
            if self.gender=="boy":
                return(round(random.uniform(0.027, 0.0395),3)) # boys outpace girls
            else:
                return(round(random.uniform(0.023, 0.0355),3))

    def determine_height_gain_by_age(self): # NOTE: STILL NEED TO ADJUST THIS
        if self.age=="Newborn":
            if self.gender=="boy":
                return(round(random.uniform(0.04425, 0.0670),3))
            else:
                return(round(random.uniform(0.04175, 0.0610),3))

        if self.age=="Infant":
            if self.gender=="boy":
                return(round(random.uniform(0.025, 0.0485),3))
            else:
                return(round(random.uniform(0.0225, 0.04585),3))

        if self.age=="Toddler":
            if self.gender=="boy":
                return(round(random.uniform(0.015625, 0.01925),3))
            else:
                return(round(random.uniform(0.015425, 0.01895),3))

        if self.age=="Preschooler":
            if self.gender=="boy":
                return(round(random.uniform(0.010825, 0.013425),3))
            else:
                return(round(random.uniform(0.010525, 0.013225),3))
            
        if self.age=="Adolescent":
            if self.gender=="boy":
                return(round(random.uniform(0.013225, 0.021),3))
            else:
                return(round(random.uniform(0.013025, 0.020),3))

        if self.age=="Pre-teen":
            if self.gender=="boy":
                return(round(random.uniform(0.01675, 0.0325),3))
            else:
                return(round(random.uniform(0.01875, 0.0375),3)) # girls outpace boys

        if self.age=="Teen":
            if self.gender=="boy":
                return(round(random.uniform(0.027, 0.0395),3)) # boys outpace girls
            else:
                return(round(random.uniform(0.023, 0.0355),3))

    # Function to update attributes, skills, needs, and Height/Weight based on the action of the turn
    def process_action(self, action):
        action_dict = {"Sleep":{"Needs":{"Energy":2},
                        "Attributes":None,
                        "Size":{"Height":round(random.uniform(0.005, .015),3)}},
               "Feed":{"Needs":{"Hunger":2},
                        "Attributes":None,
                        "Size":{"Weight":round(random.uniform(0.015, .025),3)}},
               "Play":{"Needs":{"Energy":-4,
                                "Hygiene":-2},
                        "Attributes": self.develop_skill("Play"),
                        "Size":{"Weight":-.01}},
               "Teach":{"Needs":{"Energy":-6},
                        "Attributes":self.develop_skill("Teach"),
                        "Size":None},
               "Clean":{"Needs":{"Hygiene":2,
                                            "Energy":-2},
                        "Attributes":None,
                        "Size":None},
               "Do Nothing":{"Needs":None,
                        "Attributes":None,
                        "Size":None},
               "Bonding Time":{"Needs":{"Energy":-2,
                                        "Love for Parent":2},
                        "Attributes":self.develop_skill("Bonding Time"),
                        "Size":None},
               }
        # get the effects of the given action
        effects = action_dict[action]

        # process each of the keys
        if effects["Needs"] is not None:
            for k1 in self.needs:
                if k1 in effects["Needs"]:
                    self.needs[k1] = effects["Needs"][k1] + self.needs[k1]

        if effects["Attributes"] is not None:
            for k1 in self.attributes:
                if k1 in effects["Attributes"]:
                    self.attributes[k1] = effects["Attributes"][k1] + self.attributes[k1]

        if effects["Size"] is not None:
            for k1 in ["Weight","Height"]:
                if k1 in effects["Size"]:
                    if k1=="Weight":
                        self.weight += effects["Size"][k1]
                    if k1=="Height":
                        self.height += effects["Size"][k1]
