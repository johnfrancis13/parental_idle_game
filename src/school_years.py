# When the child reaches preschool the attributes change

# This will reformat the app for school age
def reformat_app_for_school(self):
    # Create a dictionary to hold the labels for dynamic updates 
    self.attributes_labels = {} 
    self.attributes_frames = {} 
    self.attributes_category_labels = {} 
    frame2 = tk.Frame(self.root,bg="white")
    frame2.grid(pady=5)
    # Create the score boxes with labels
    for i, (category, score) in enumerate(self.school_starting_attributes_dict.items()): 
        # Create a frame for each score box
        attributes_frame = tk.Frame(frame2, bd=2, relief="groove",bg="white")
        attributes_frame.grid(row=i//7, column=i%7, padx=2, pady=5)
        self.attributes_frames[category] = attributes_frame
        # Create a label for the score value
        attributes_label = tk.Label(attributes_frame, text=score, font=("Helvetica", 12),bg="white") 
        attributes_label.grid(row=0, column=0, pady=5) 
        self.attributes_labels[category] = attributes_label 
        # Create a label for the category 
        attributes_category_label = tk.Label(attributes_frame, text=category, font=("Helvetica", 10),bg="white") 
        attributes_category_label.grid(row=1, column=0)
        self.attributes_category_labels[category] = attributes_category_label


# THis function will determine the starting point for the school level attributes
def determine_school_starting_attributes(self):

    basic_attribute_school_mapping = {
                "Motor Skills":["Life skills","Physical Development"],
                "Social Skills":["Social Skills","Communication Skills"],
                "Emotional Skills":["Emotional Skills"],
                "Communication Skills":["Communication Skills","Emotional Skills","Life skills"],
                "Cognitive Skills":["Academic Skills","Life skills"],
                "Physical Development":["Physical Development"]}
    
    for key, value in self.attributes_labels.items():
                self.attributes_labels[key]


    starting_attributes_dict = {
                "Academic Skills":0,
                "Social Skills":0,
                "Emotional Skills":0,
                "Communication Skills":0,
                "Creativity":0,
                "Life skills":0,
                "Physical Development":0}
    
    return  starting_attributes_dict 

    
 
    
