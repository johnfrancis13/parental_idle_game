import random
# Function to determine what the child's ambition is
def develop_ambition(age:str="Preschooler",
                     child_attributes:dict=dict()):
    
    # Get the attribute with the highest value 
    primary_attribute = max(child_attributes, key=child_attributes.get)
    if primary_attribute=="Motor Skills":
        possible_ambitions = [ "astronaut", "doctor", "firefighter", "police officer", "chef", 
                             "artist", "pilot", "superhero", "dancer", "engineer",  "musician", "builder"]
    elif primary_attribute=="Social Skills":
        possible_ambitions = ["astronaut", "teacher", "doctor",  "police officer", "veterinarian",
                             "artist", "superhero", "dancer", "musician", "builder"]
    elif primary_attribute=="Emotional Skills":
        possible_ambitions = ["teacher", "doctor", "police officer", "veterinarian", "chef",
                             "artist",  "dancer",  "musician"]
    elif primary_attribute=="Communication Skills":
        possible_ambitions = [ "astronaut", "teacher", "doctor", "veterinarian","pilot", "superhero", "musician"]
    elif primary_attribute=="Cognitive Skills":
        possible_ambitions = [ "astronaut", "teacher", "doctor", "police officer", "chef",
                              "engineer", "scientist", "musician", "builder"]
    elif primary_attribute=="Physical Development":
        possible_ambitions = [ "astronaut", "firefighter", "police officer", "chef", "pilot", "superhero", "dancer", "builder"]  
    child_ambition = random.choice(possible_ambitions,1)

    return child_ambition

# Function to determine what the child's ambition is based on their previous ambition and how they have developed
# Potentially do this in 3 or 4 waves
def update_ambition(age:str="",
                    child_attributes:dict=dict(),
                    previous_ambition:str=""):
    
    if age=="Adolescent":
        # check if child wants to keep their ambition?
        new_child_ambition = develop_ambition(child_attributes=child_attributes)

    else:
        ambition_mapping = {"astronaut": ["aerospace engineer", "astrophysicist", "space exploration scientist"], 
                            "teacher": ["author", "educational consultant", "researcher","teacher","principal"],
                            "doctor": ["biologist", "surgeon", "pediatrician","doctor","dentist"], 
                            "firefighter": ["paramedic", "emergency response coordinator", "wildlife firefighter","firefighter"],
                            "police officer": ["detective", "forensic scientist", "private investigator","police officer","lawyer","judge"], 
                            "chef": ["pastry chef", "culinary instructor", "restaurant manager","chef","restranteur"], 
                            "veterinarian": ["zoologist", "wildlife conservationist", "animal behaviorist","veterinarian"], 
                            "artist": ["graphic designer", "illustrator", "art director","painter"], 
                            "pilot": ["commercial airline pilot", "flight instructor", "aeronautical engineer"], 
                            "superhero": ["environmentalist", "social activist", "human rights lawyer","special forces member"], 
                            "dancer": ["choreographer", "dance teacher", "performing artist","professional dancer"], 
                            "engineer": ["robotics engineer", "civil engineer", "software developer"], 
                            "scientist": ["astronomer", "marine biologist", "chemist","physicist"], 
                            "musician": ["composer", "music producer", "orchestra conductor","pop star","professional musician"], 
                            "builder": ["architect", "construction manager", "interior designer","construction worker"]}
        
        new_child_ambition = random.choice(ambition_mapping[previous_ambition])

    return new_child_ambition

# Function for the end of the game to determine if the child successfully achieved their ambition
def check_ambition_successful(child_attributes:dict=dict(),
                              child_ambition:str=""):
    
    ambition_requirements = {'aerospace engineer':{},
                             'astrophysicist':{},
                             'space exploration scientist':{},
                             'author':{},
                             'educational consultant':{},
                             'researcher':{},
                             'teacher':{},
                             'principal':{},
                             'biologist':{},
                             'surgeon':{},
                             'pediatrician':{},
                             'doctor':{},
                             'dentist':{},
                             'paramedic':{},
                             'emergency response coordinator':{},
                             'wildlife firefighter':{},
                             'firefighter':{},
                             'detective':{},
                             'forensic scientist':{},
                             'private investigator':{},
                             'police officer':{},
                             'lawyer':{},
                             'judge':{},
                             'pastry chef':{},
                             'culinary instructor':{},
                             'restaurant manager':{},
                             'chef':{},
                             'restranteur':{},
                             'zoologist':{},
                             'wildlife conservationist':{},
                             'animal behaviorist':{},
                             'veterinarian':{},
                             'graphic designer':{},
                             'illustrator':{},
                             'art director':{},
                             'painter':{},
                             'commercial airline pilot':{},
                             'flight instructor':{},
                             'aeronautical engineer':{},
                             'environmentalist':{},
                             'social activist':{},
                             'human rights lawyer':{},
                             'special forces member':{},
                             'choreographer':{},
                             'dance teacher':{},
                             'performing artist':{},
                             'professional dancer':{},
                             'robotics engineer':{},
                             'civil engineer':{},
                             'software developer':{},
                             'astronomer':{},
                             'marine biologist':{},
                             'chemist':{},
                             'physicist':{},
                             'composer':{},
                             'music producer':{},
                             'orchestra conductor':{},
                             'pop star':{},
                             'professional musician':{},
                             'architect':{},
                             'construction manager':{},
                             'interior designer':{},
                             'construction worker':{}}
    childs_ambition_requirements = ambition_requirements[child_ambition]
    
    # Check the 4 thresholds for each skill to see if they have been met 
    failed = 0 
    for key in childs_ambition_requirements:
        if childs_ambition_requirements[key]<2000:
            failed += 1

    if failed==0:
        ambition_rating = "Ultimate ambition success!"
    elif failed==1:
        ambition_rating = "Ambition success!"
    elif failed==2:
        ambition_rating = "Partial ambition success"
    else:
        ambition_rating = "Ambition failure"

    return ambition_rating