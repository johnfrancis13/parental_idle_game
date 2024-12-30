import random

# This is a class to hold alln the methods for the random events
class event_class():

    def increase_skill(self,skill,increase_amount):
        self.attributes[skill] += increase_amount
    
    def increase_need(self,need,increase_amount):
        self.needs[need] += increase_amount
    
    def growth_adjustment(self,height_adjustment,weight_adjustment):
        self.height += height_adjustment
        self.weight += weight_adjustment
        

    # check and choose random event
    def random_event(self):
        print("Checking for a random event...")
        if random.random() >=.4:
            print("Random event chosen.")
            # Each of these should have a name, and then a list of functions that have an effect
            random_event_options_good = {"Newborn": [
                                            {"event_name": "made a skill breakthrough",
                                            "event_effects":[(self.increase_skill,(
                                                random.choice(["Motor Skills","Social Skills","Emotional Skills",
                                                              "Communication Skills","Cognitive Skills","Physical Development"]),
                                                              20
                                            ))]},
                                            {"event_name": "slept through the night",
                                            "event_effects":[(self.increase_need,("Energy",25))]},
                                            {"event_name": "meeting new relatives",
                                            "event_effects":[(self.increase_need,("Energy",-20)),
                                                             (self.increase_skill,("Social Skills",15)),
                                                             (self.increase_skill,("Communication Skills",15))]},
                                            {"event_name": "first park trip",
                                            "event_effects":[(self.increase_need,("Energy",-20)),
                                                             (self.increase_skill,("Motor Skills",15)),
                                                             (self.increase_skill,("Cognitive Skills",15))]},
                                            {"event_name": "growth spurt",
                                            "event_effects":[(self.increase_need,("Energy",-20)),
                                                             (self.increase_need,("Hunger",-20)),
                                                             (self.growth_adjustment,(round(random.uniform(0.00325*5, .00525*5),3),
                                                                                      round(random.uniform(0.04425*5, .0670*5),3)))]},
                                        ],
                                        "Infant": [
                                            {"event_name": "made a skill breakthrough",
                                            "event_effects":[(self.increase_skill,(
                                                random.choice(["Motor Skills","Social Skills","Emotional Skills",
                                                              "Communication Skills","Cognitive Skills","Physical Development"]),
                                                              20
                                            ))]},
                                            {"event_name": "growth spurt",
                                            "event_effects":[(self.increase_need,("Energy",-20)),
                                                             (self.increase_need,("Hunger",-20)),
                                                             (self.growth_adjustment,(round(random.uniform(0.00325*5, .00525*5),3),
                                                                                      round(random.uniform(0.04425*5, .0670*5),3)))]},
                                            {"event_name": "says a new word",
                                            "event_effects":[(self.increase_skill,("Communication Skills",20))]},
                                            {"event_name": "moves in a new way",
                                            "event_effects":[(self.increase_skill,("Motor Skills",15)),
                                                             (self.increase_skill,("Physical Development",15))]},
                                            {"event_name": "laughs heartily for the first time",
                                            "event_effects":[(self.increase_skill,("Emotional Skills",15)),
                                                             (self.increase_skill,("Social Skills",15))]},
                                            {"event_name": "responds to name",
                                            "event_effects":[(self.increase_skill,("Communication Skills",20))]},
                                            {"event_name": "shows interest in toys",
                                            "event_effects":[(self.increase_skill,("Cognitive Skills",20))]}
                                        ],
                                        "Toddler": [
                                            {"event_name": "made a skill breakthrough",
                                            "event_effects":[(self.increase_skill,(
                                                random.choice(["Motor Skills","Social Skills","Emotional Skills",
                                                              "Communication Skills","Cognitive Skills","Physical Development"]),
                                                              20
                                            ))]},
                                            {"event_name": "growth spurt",
                                            "event_effects":[(self.increase_need,("Energy",-20)),
                                                             (self.increase_need,("Hunger",-20)),
                                                             (self.growth_adjustment,(round(random.uniform(0.00325*5, .00525*5),3),
                                                                                      round(random.uniform(0.04425*5, .0670*5),3)))]},
                                            {"event_name": "learns to use the potty",
                                            "event_effects":[]},
                                            {"event_name": "draws a picture",
                                            "event_effects":[]},
                                            {"event_name": "makes a new friend",
                                            "event_effects":[]},
                                            {"event_name": "learns to count",
                                            "event_effects":[]},
                                            {"event_name": "helps with chores",
                                            "event_effects":[]}
                                        ],
                                        "Preschooler": [
                                            {"event_name": "made a skill breakthrough",
                                            "event_effects":[(self.increase_skill,(
                                                random.choice(["Motor Skills","Social Skills","Emotional Skills",
                                                              "Communication Skills","Cognitive Skills","Physical Development"]),
                                                              20
                                            ))]},
                                            {"event_name": "growth spurt",
                                            "event_effects":[(self.increase_need,("Energy",-20)),
                                                             (self.increase_need,("Hunger",-20)),
                                                             (self.growth_adjustment,(round(random.uniform(0.00325*5, .00525*5),3),
                                                                                      round(random.uniform(0.04425*5, .0670*5),3)))]},
                                            {"event_name": "learns to ride a bike",
                                            "event_effects":[]},
                                            {"event_name": "wins a small award",
                                            "event_effects":[]},
                                            {"event_name": "reads a book independently",
                                            "event_effects":[]},
                                            {"event_name": "builds a complex structure with blocks",
                                            "event_effects":[]},
                                            {"event_name": "helps a friend in need",
                                            "event_effects":[]}
                                        ],
                                        "Adolescent": [
                                            {"event_name": "made a skill breakthrough",
                                            "event_effects":[(self.increase_skill,(
                                                random.choice(["Motor Skills","Social Skills","Emotional Skills",
                                                              "Communication Skills","Cognitive Skills","Physical Development"]),
                                                              20
                                            ))]},
                                            {"event_name": "growth spurt",
                                            "event_effects":[(self.increase_need,("Energy",-20)),
                                                             (self.increase_need,("Hunger",-20)),
                                                             (self.growth_adjustment,(round(random.uniform(0.00325*5, .00525*5),3),
                                                                                      round(random.uniform(0.04425*5, .0670*5),3)))]},
                                            {"event_name": "joins a sports team",
                                            "event_effects":[]},
                                            {"event_name": "gets a high grade on a test",
                                            "event_effects":[]},
                                            {"event_name": "discovers a new hobby",
                                            "event_effects":[]},
                                            {"event_name": "makes a new friend",
                                            "event_effects":[]},
                                            {"event_name": "volunteers for a community event",
                                            "event_effects":[]}
                                        ],
                                        "Pre-teen": [
                                            {"event_name": "made a skill breakthrough",
                                            "event_effects":[(self.increase_skill,(
                                                random.choice(["Motor Skills","Social Skills","Emotional Skills",
                                                              "Communication Skills","Cognitive Skills","Physical Development"]),
                                                              20
                                            ))]},
                                            {"event_name": "growth spurt",
                                            "event_effects":[(self.increase_need,("Energy",-20)),
                                                             (self.increase_need,("Hunger",-20)),
                                                             (self.growth_adjustment,(round(random.uniform(0.00325*5, .00525*5),3),
                                                                                      round(random.uniform(0.04425*5, .0670*5),3)))]},
                                            {"event_name": "gets a part in a school play",
                                            "event_effects":[]},
                                            {"event_name": "wins a science fair",
                                            "event_effects":[]},
                                            {"event_name": "learns to play an instrument",
                                            "event_effects":[]},
                                            {"event_name": "starts a small business",
                                            "event_effects":[]},
                                            {"event_name": "helps a neighbor",
                                            "event_effects":[]}
                                        ],
                                        "Teen": [
                                            {"event_name": "made a skill breakthrough",
                                            "event_effects":[(self.increase_skill,(
                                                random.choice(["Motor Skills","Social Skills","Emotional Skills",
                                                              "Communication Skills","Cognitive Skills","Physical Development"]),
                                                              20
                                            ))]},
                                            {"event_name": "growth spurt",
                                            "event_effects":[(self.increase_need,("Energy",-20)),
                                                             (self.increase_need,("Hunger",-20)),
                                                             (self.growth_adjustment,(round(random.uniform(0.00325*5, .00525*5),3),
                                                                                      round(random.uniform(0.04425*5, .0670*5),3)))]},
                                            {"event_name": "gets accepted into a dream college",
                                            "event_effects":[]},
                                            {"event_name": "scores the winning point in a game",
                                            "event_effects":[]},
                                            {"event_name": "lands a part-time job",
                                            "event_effects":[]},
                                            {"event_name": "starts a new club at school",
                                            "event_effects":[]},
                                            {"event_name": "receives a scholarship",
                                            "event_effects":[]}
                                        ]
                                        }                                       

            random_event_options_bad = {"Newborn": [
                                            {"event_name": "refuses to eat",
                                            "event_effects":[(self.increase_need,("Energy",-25)),
                                                             (self.increase_need,("Hunger",-25)),
                                                             ]},
                                            {"event_name": "has colic",
                                            "event_effects":[(self.increase_need,("Health",-25))]},
                                            {"event_name": "won't stop crying",
                                            "event_effects":[(self.increase_need,("Love for Parent",-25))]},
                                            {"event_name": "has an ear infection",
                                            "event_effects":[(self.increase_need,("Health",-25))]},
                                            {"event_name": "has bad diarrhea",
                                            "event_effects":[(self.increase_need,("Health",-25))]},
                                        ],
                                        "Infant": [
                                            {"event_name": "catches a cold",
                                            "event_effects":[(self.increase_need,("Health",-25))]},
                                            {"event_name": "wakes up crying at night",
                                            "event_effects":[(self.increase_need,("Energy",-25))]},
                                            {"event_name": "falls while learning to walk",
                                            "event_effects":[(self.increase_need,("Health",-15)),
                                                             (self.increase_skill,("Motor Skills",-15))]},
                                            {"event_name": "has a fever",
                                            "event_effects":[(self.increase_need,("Health",-25))]},
                                            {"event_name": "is teething and irritable",
                                            "event_effects":[(self.increase_need,("Energy",-25)),
                                                             (self.increase_need,("Hunger",-25)),]}
                                        ],
                                        "Toddler": [
                                            {"event_name": "refuses to eat",
                                            "event_effects":[(self.increase_need,("Energy",-25)),
                                                             (self.increase_need,("Hunger",-25)),
                                                             ]},
                                            {"event_name": "catches a cold",
                                            "event_effects":[(self.increase_need,("Health",-25))]},
                                            {"event_name": "gets hurt while playing",
                                            "event_effects":[(self.increase_need,("Health",-15)),
                                                             (self.increase_skill,("Motor Skills",-15))]},
                                            {"event_name": "throws a tantrum in public",
                                            "event_effects":[]},
                                            {"event_name": "loses a favorite toy",
                                            "event_effects":[]},
                                            {"event_name": "refuses to share with others",
                                            "event_effects":[]},
                                            {"event_name": "falls and gets a bruise",
                                            "event_effects":[]},
                                            {"event_name": "has separation anxiety",
                                            "event_effects":[]}
                                        ],
                                        "Preschooler": [
                                            {"event_name": "refuses to eat",
                                            "event_effects":[(self.increase_need,("Energy",-25)),
                                                             (self.increase_need,("Hunger",-25)),
                                                             ]},
                                            {"event_name": "catches a cold",
                                            "event_effects":[(self.increase_need,("Health",-25))]},
                                            {"event_name": "gets hurt while playing",
                                            "event_effects":[(self.increase_need,("Health",-15)),
                                                             (self.increase_skill,("Motor Skills",-15))]},
                                            {"event_name": "has a nightmare",
                                            "event_effects":[]},
                                            {"event_name": "gets a minor injury",
                                            "event_effects":[]},
                                            {"event_name": "feels left out by friends",
                                            "event_effects":[]},
                                            {"event_name": "refuses to eat vegetables",
                                            "event_effects":[]},
                                            {"event_name": "loses at a game and gets upset",
                                            "event_effects":[]}
                                        ],
                                        "Adolescent": [
                                            {"event_name": "refuses to eat",
                                            "event_effects":[(self.increase_need,("Energy",-25)),
                                                             (self.increase_need,("Hunger",-25)),
                                                             ]},
                                            {"event_name": "catches a cold",
                                            "event_effects":[(self.increase_need,("Health",-25))]},
                                            {"event_name": "gets hurt while playing",
                                            "event_effects":[(self.increase_need,("Health",-15)),
                                                             (self.increase_skill,("Motor Skills",-15))]},
                                            {"event_name": "struggles with schoolwork",
                                            "event_effects":[]},
                                            {"event_name": "has an argument with a friend",
                                            "event_effects":[]},
                                            {"event_name": "feels self-conscious about changes",
                                            "event_effects":[]},
                                            {"event_name": "experiences peer pressure",
                                            "event_effects":[]},
                                            {"event_name": "misses an important event",
                                            "event_effects":[]}
                                        ],
                                        "Pre-teen": [
                                            {"event_name": "refuses to eat",
                                            "event_effects":[(self.increase_need,("Energy",-25)),
                                                             (self.increase_need,("Hunger",-25)),
                                                             ]},
                                            {"event_name": "catches a cold",
                                            "event_effects":[(self.increase_need,("Health",-25))]},
                                            {"event_name": "gets hurt while playing",
                                            "event_effects":[(self.increase_need,("Health",-15)),
                                                             (self.increase_skill,("Motor Skills",-15))]},
                                            {"event_name": "fails a test",
                                            "event_effects":[]},
                                            {"event_name": "experiences bullying",
                                            "event_effects":[]},
                                            {"event_name": "gets grounded for misbehavior",
                                            "event_effects":[]},
                                            {"event_name": "loses a valuable possession",
                                            "event_effects":[]},
                                            {"event_name": "has a disagreement with parents",
                                            "event_effects":[]}
                                        ],
                                        "Teen": [
                                            {"event_name": "refuses to eat",
                                            "event_effects":[(self.increase_need,("Energy",-25)),
                                                             (self.increase_need,("Hunger",-25)),
                                                             ]},
                                            {"event_name": "catches a cold",
                                            "event_effects":[(self.increase_need,("Health",-25))]},
                                            {"event_name": "gets hurt while playing",
                                            "event_effects":[(self.increase_need,("Health",-15)),
                                                             (self.increase_skill,("Motor Skills",-15))]},
                                            {"event_name": "breaks up with a significant other",
                                            "event_effects":[]},
                                            {"event_name": "faces peer pressure",
                                            "event_effects":[]},
                                            {"event_name": "struggles with college applications",
                                            "event_effects":[]},
                                            {"event_name": "experiences a friendship breakup",
                                            "event_effects":[]},
                                            {"event_name": "fails a driver's test",
                                            "event_effects":[]}
                                        ]
                                    }

            # If child doing well, higher chance for good event, else higher chance for bad event 
            if self.needs["Hunger"]>50 and self.needs["Hygiene"]>50 and self.needs["Energy"]>50 and self.needs["Love for Parent"]>50:
                if random.random() >=.7:
                    random_event_list= random.choice(random_event_options_good[self.age])
                    random_positive = 1

                else:
                    random_event_list=random.choice(random_event_options_bad[self.age])
                    random_positive = 0

            else:
                if random.random() >=.7:
                    random_event_list= random.choice(random_event_options_bad[self.age])
                    random_positive = 0

                else:
                    random_event_list=random.choice(random_event_options_good[self.age])
                    random_positive = 1
            print(random_event_list["event_name"])
            return(1,random_event_list,random_positive)
        else:
            return(0, "no event",-1)