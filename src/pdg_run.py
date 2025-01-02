import tkinter as tk
from character_classes import parental_unit, baby
import random
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage
import pickle
from tkinter import simpledialog

class TurnTrackerApp:
    def __init__(self, root):
        self.root = root      
        self.turn_count = 0
        self.name = ""  # Initialize an empty name
        self.child_gender=random.choice(["boy","girl"])

        # Configure the style for the ttk.Notebook 
        style = ttk.Style() 
        style.theme_use('default') 
        # Set the background color for the ttk.Notebook 
        style.configure('TNotebook', background='lightblue1') 
        style.configure('TNotebook.Tab', background='lightblue1')
        style.configure('TFrame', background='lightblue1')
        # Set the background color for the selected tab
        style.map('TNotebook.Tab', background=[('selected','lightblue')])
        style.map('TNotebook', background=[('selected','lightblue')])
        style.map('TFrame', background=[('selected','lightblue')])

        # Create widgets
        self.turn_label = tk.Label(self.root, text="Day: 0",bg="white")
        self.start_game_button = tk.Button(self.root, text="Start Game", command=self.increment_turn,bg="lightgreen")
        self.name_label = tk.Label(self.root, text="Enter your name:",bg="white")
        self.child_label = tk.Label(self.root, text=f"You and your partner have just had your first child, it's a {self.child_gender}! Please give them a name:",bg="white")
        self.name_entry = tk.Entry(self.root,bg="white")  # Add an entry widget for the name
        self.child_entry = tk.Entry(self.root,bg="white")  # Add an entry widget for the name

        self.save_button = tk.Button(root, text="Save Game", command=self.save_game,bg="plum1") 
        self.load_button = tk.Button(root, text="Load Game", command=self.load_game,bg="plum2") 

        # Create a StringVar to hold the selected choice 
        self.parent_income_label = tk.Label(self.root, text=f"Your income determines how challenging it will be to raise your child! Please choose your income:",bg="white")
        # Define the choices
        choices = ["Low paying job (Hard)", "Average paying job (Regular)", "High paying job (Easy)"] 
        # Create the OptionMenu
        self.option_menu = ttk.Combobox(self.root, values=choices,width = 30)
        self.option_menu.set("Average paying job (Regular)")
        
        self.name_entry.insert(0, "John")
        self.child_entry.insert(0, "GB")
        self.parent_info = tk.Label(self.root, text="Result will appear here",bg="white")
        self.child_info = tk.Label(self.root, text="",bg="white")

        self.image = PhotoImage(file="data/assets/newborn_image.png")
        
                                                                                             
        starting_needs_dict = {"Hunger":75, # need food to stay happy/healthy
                      "Hygiene":75, # cleanliness to stay happy/healthy
                      "Energy":75, # energy to do activities before collapsing
                      "Happiness":50, # higher happiness affects performance on tasks
                      "Health":50, # poor health prevents some activities
                      "Love for Parent":75, # affects how amenable child is to activities
                      "Fear of Parent":75, #  affects how amenable child is to activities
                      "Current Physical State":"healthy",
                      "Current Mental State":"content"}
        
        # Create a dictionary to hold the labels for dynamic updates 
        self.needs_labels = {} 
        self.needs_frames = {} 
        self.needs_category_labels = {} 
        frame = tk.Frame(self.root,bg="white")
        frame.grid(pady=5)
        # Create the score boxes with labels
        for i, (category, score) in enumerate(starting_needs_dict.items()): 
            # Create a frame for each score box
            needs_frame = tk.Frame(frame, bd=2, relief="groove",bg="white")
            needs_frame.grid(row=i//9, column=i%9, padx=2, pady=5)
            self.needs_frames[category] = needs_frame
            # Create a label for the score value
            needs_label = tk.Label(needs_frame, text=score, font=("Helvetica", 12),bg="white") 
            needs_label.grid(row=0, column=0, pady=5) 
            self.needs_labels[category] = needs_label 
            # Create a label for the category 
            needs_category_label = tk.Label(needs_frame, text=category, font=("Helvetica", 10),bg="white") 
            needs_category_label.grid(row=1, column=0)
            self.needs_category_labels[category] = needs_category_label 

        starting_attributes_dict = {
                "Motor Skills":0,
                "Social Skills":0,
                "Emotional Skills":0,
                "Communication Skills":0,
                "Cognitive Skills":0,
                "Physical Development":0}
        
        # Create a dictionary to hold the labels for dynamic updates 
        self.attributes_labels = {} 
        frame2 = tk.Frame(self.root,bg="white")
        frame2.grid(pady=5)
        # Create the score boxes with labels
        for i, (category, score) in enumerate(starting_attributes_dict.items()): 
            # Create a frame for each score box
            attributes_frame = tk.Frame(frame2, bd=2, relief="groove",bg="white")
            attributes_frame.grid(row=i//6, column=i%6, padx=2, pady=5)
            # Create a label for the score value
            attributes_label = tk.Label(attributes_frame, text=score, font=("Helvetica", 12),bg="white") 
            attributes_label.grid(row=0, column=0, pady=5) 
            self.attributes_labels[category] = attributes_label 
            # Create a label for the category 
            attributes_category_label = tk.Label(attributes_frame, text=category, font=("Helvetica", 10),bg="white") 
            attributes_category_label.grid(row=1, column=0)

        starting_physical_dict = {
                "Name":0,
                "Age (category)":0,
                "Age (days)":0,
                "Weight (lbs)":0,
                "Height (in)":0}
        # Create a dictionary to hold the labels for dynamic updates 
        self.physical_labels = {} 
        frame3 = tk.Frame(self.root,bg="white")
        frame3.grid(pady=5)
        # Create the score boxes with labels
        for i, (category, score) in enumerate(starting_physical_dict.items()): 
            # Create a frame for each score box
            physical_frame = tk.Frame(frame3, bd=2, relief="groove",bg="white")
            physical_frame.grid(row=i//6, column=i%6, padx=2, pady=5)
            # Create a label for the score value
            physical_label = tk.Label(physical_frame, text=score, font=("Helvetica", 12),bg="white") 
            physical_label.grid(row=0, column=0, pady=5) 
            self.physical_labels[category] = physical_label 
            # Create a label for the category 
            physical_category_label = tk.Label(physical_frame, text=category, font=("Helvetica", 10),bg="white") 
            physical_category_label.grid(row=1, column=0)

            
        # Create a notebook (tabbed interface)
        notebook = ttk.Notebook(root) 
        notebook.grid(pady=5) 
        # Create frames for each skill tree 
        self.skill_trees = ["Motor Skills","Social Skills","Emotional Skills","Communication Skills","Cognitive Skills","Physical Development"] 
        self.skill_frames = {} 
        for skill_tree in self.skill_trees: 
            frame = ttk.Frame(notebook) 
            notebook.add(frame, text=skill_tree) 
            self.skill_frames[skill_tree] = frame 

        # update the frame colors
        self.update_frame_colors()

        def restart(): 
            self.root.destroy() # Destroy the current root window
            main()
        self.restart_button = tk.Button(self.root, text="Restart", command=restart,bg="lightblue")
        
        def update_total_points():
            total_points = 48
            current_total = sum(int(self.spinbox_list[i].get()) for i in range(len(self.spinbox_list)))
            remaining_points = total_points - current_total
            self.remaining_label.config(text=f"Remaining 30 min time chunks: {remaining_points}")
            # You can add logic here to disable/enable buttons based on remaining points.
            if remaining_points < 0:
                remaining_points = 0

        def on_spinbox_change(index):
            update_total_points()
            remaining_points = int(self.remaining_label.cget("text").split()[-1])  # Get remaining points
            if remaining_points < 0:
                # Disable the Next turn button (optional)
                self.next_turn_button.config(state="disabled")
                self.next_5turn_button.config(state="disabled")
                self.next_10turn_button.config(state="disabled")

            else:
                # Enable the Next turn button
                self.next_turn_button.config(state="normal")
                self.next_5turn_button.config(state="normal")
                self.next_10turn_button.config(state="normal")

        self.spinbox_list = []
        self.spinbox_values = []
        self.spin_labels = [] 
        frame4 = tk.Frame(self.root,bg="white")
        frame4.grid(pady=5)
        self.actions = ["Sleep","Feed","Play", "Teach","Clean","Rest","Bonding Time"]
        for i in range(len(self.actions)):
            spinbox_value_i = tk.StringVar()
            spinbox = tk.Spinbox(frame4, from_=0, to=48, command=lambda i=i: on_spinbox_change(i),
                                 state="readonly", textvariable=spinbox_value_i,bg="white")
            label = tk.Label(frame4, text=f"{self.actions[i]}",bg="white")
            self.spinbox_list.append(spinbox)
            self.spinbox_values.append(spinbox_value_i)
            self.spin_labels.append(label)

        self.remaining_label = tk.Label(self.root, text="Remaining 30 min time chunks: 0",bg="white")
        
        # grid widgets
        self.child_info.grid(row=4, column=0,pady=3)
        self.turn_label.grid(row=5, column=0,pady=3)
        self.name_label.grid(row=6, column=0)
        self.name_entry.grid(row=7, column=0)
        self.child_label.grid(row=8, column=0)
        self.child_entry.grid(row=9, column=0)
        self.parent_income_label.grid(row=10, column=0)
        self.option_menu.grid(row=11, column=0)

        self.start_game_button.grid(row=12, column=0)
        self.restart_button.grid(row=13, column=0)
        self.load_button.grid(row=15, column=0)
        
    def end_game(self): 
        messagebox.showinfo("Game Over", f"Your child {self.child.name} died after {self.child.age_days} days. Better luck next time!") 
        self.root.quit() # Close the game window

    def end_game_victory(self): 
        messagebox.showinfo("Game Over", f"Your child {self.child.name} turned 18 and is ready to leave the house. Better luck next time!")
        # Need to add in some stats/ability to reset with some benefits
        self.root.quit() # Close the game window
    
    def buy_needs(self,need,amount):
        for ne in need:
            self.child.needs[ne] += amount
            self.needs_labels[ne].config(text=self.child.needs[ne])
        self.current_money += -50
        self.income_label.config(text=f"${self.current_money}")
        self.update_buy_button_states()

    def buy_skills(self,skill,amount):
        for sk in skill:
            self.child.attributes[sk] += amount
            self.attributes_labels[sk].config(text=self.child.attributes[sk])
        self.current_money += -50
        self.income_label.config(text=f"${self.current_money}") 
        self.update_buy_button_states()

    def increment_turn(self):

        # Turn 0 is setup, add an introduction of your child (randomly you and your spouse have just had a boy/girl, what would you like to name it?)
        if self.turn_count==0:
            self.name = self.name_entry.get()
            self.child_name = self.child_entry.get()
            self.parent_income = self.option_menu.get()
            self.name_label.grid_forget()
            self.turn_label.grid_forget()
            self.name_entry.grid_forget()
            self.child_label.grid_forget()
            self.child_info.grid_forget()
            self.child_entry.grid_forget()
            self.parent_income_label.grid_forget()
            self.option_menu.grid_forget()
            self.start_game_button.grid_forget()
            self.restart_button.grid_forget()
            self.load_button.grid_forget()
            self.remaining_label.grid(row=7, column=0,pady=3)

            for i in range(len(self.spinbox_list)):
                #self.spin_labels[i].grid(pady=5,row=i+8, column=0, sticky="n")  
                #self.spinbox_list[i].grid(pady=5,row=i+8, column=0, sticky="s")
                self.spin_labels[i].grid(padx=3,row=8, column=i%7, sticky="n")  
                self.spinbox_list[i].grid(padx=3,row=9, column=i%7, sticky="s")

            self.child_info.grid()

            frame_image = tk.Frame(self.root,bg="white")
            frame_image.grid(row=11,pady=5,padx=5)
            self.image_label = tk.Label(frame_image, image=self.image,bg="white")
            self.image_label.grid(row=11,column=0%4,rowspan=4,padx=5)
            self.next_turn_button = tk.Button(frame_image, text="Next Day", command=self.increment_turn,bg="lightgreen")
            self.next_5turn_button = tk.Button(frame_image, text="Advance 5 Days", command=lambda: self.multi_increment_turn(5),bg="lightgreen")
            self.next_10turn_button = tk.Button(frame_image, text="Advance 10 Days", command=lambda: self.multi_increment_turn(10),bg="lightgreen")
            self.next_turn_button.grid(row=11,column=1%4,rowspan=1)
            self.next_5turn_button.grid(row=12,column=1%4,rowspan=1)
            self.next_10turn_button.grid(row=13,column=1%4,rowspan=1)
            # Create a frame for income
            self.income_frame = tk.Frame(frame_image, bd=2, relief="groove",bg="white")
            self.income_frame.grid(row=14,column=1)
            # Create a label for the score value
            self.current_money = 0
            self.income_label = tk.Label(self.income_frame, text=f"${self.current_money}", font=("Helvetica", 12),bg="white")
            self.income_label.grid()
            self.income_category_label = tk.Label(self.income_frame, text="Current money from "+self.parent_income, font=("Helvetica", 10),bg="white") 
            self.income_category_label.grid()
            
            # Create buttons to spend money
            self.buy_nut_supp = tk.Button(frame_image, text="Buy nutrition supplements ($50)", command=lambda: self.buy_needs(["Energy"], 20),bg="lightyellow")
            self.buy_doc = tk.Button(frame_image, text="See a doctor ($50)", command=lambda: self.buy_needs(["Health"], 20),bg="lightyellow")
            self.buy_party = tk.Button(frame_image, text="Host a social event ($50)", command=lambda: self.buy_skills(["Social Skills","Communication Skills"], 20),bg="lightyellow")
            self.buy_toy = tk.Button(frame_image, text="Buy a new toy ($50)", command=lambda: self.buy_needs(["Love for Parent"], 20),bg="lightyellow")
            self.buy_meal = tk.Button(frame_image, text="Go out to eat ($50)", command=lambda: self.buy_needs(["Hunger"], 20),bg="lightyellow")
            # add in the buy buttons
            self.buy_nut_supp.grid(row=11,column=2%4,rowspan=1)
            self.buy_doc.grid(row=12,column=2%4,rowspan=1) 
            self.buy_party.grid(row=13,column=2%4,rowspan=1)
            self.buy_toy.grid(row=11,column=3%4,rowspan=1)
            self.buy_meal.grid(row=12,column=3%4,rowspan=1)
            self.update_buy_button_states()


            #self.parent_info.grid()
            self.restart_button.grid()
            self.save_button.grid()
                 
			# Create the parent
            self.parent=parental_unit(self.name)

            # Create the child
            self.child=baby(self.child_name,self.child_gender)
            self.turn_count += 1

        # From Turn 1 onwards you can pick an action that affects your baby (or maybe you have 48 actions to distribute across a day instead of going 1 by 1?)
        # How would you like to spend the day with your ___ newborn (allocation actions representing 30 minute increments to your child)
        # The child has certain need threshold that must be met each day (a certain number of actions allocated to sleep/eat)    
        if self.spinbox_values[0].get():
            self.update_attributes()
            if self.turn_count<=1:
                self.reset_spinbox_values()

            # Check to make sure the game shuoldn't end
            if self.child.needs["Health"]==0:
                self.end_game()
        
        if self.turn_count>0:
            self.parent_info.config(text=str(self.parent.examine_self_return()))
            turn_attrib, turn_needs, turn_physical,turn_skills, turn_text  =self.child.examine_child()
            print(turn_attrib)
            print(turn_needs)
            # Update the labels with the new attribs
            for key, value in self.needs_labels.items():
                self.needs_labels[key].config(text=turn_needs[key])

            # Add Income Money
            if self.parent_income=="Low paying job (Hard)":
                self.current_money+=1
            elif self.parent_income=="Average paying job (Regular)":
                self.current_money+=2
            elif self.parent_income=="High paying job (Easy)":
                self.current_money+=5
            self.income_label.config(text=f"${self.current_money}")

            self.update_buy_button_states()

            # update the frame colors
            self.update_frame_colors()

            # update skills
            self.update_skill_trees(turn_skills)

            # Update the labels with the new needs
            for key, value in self.attributes_labels.items():
                self.attributes_labels[key].config(text=turn_attrib[key])

            # Update the labels with the new needs
            for key, value in self.physical_labels.items():
                self.physical_labels[key].config(text=turn_physical[key])

            self.child_info.config(text=str(turn_text))
            #self.turn_label.config(text=f"Day: {self.turn_count}")
            if self.turn_count==90:
                # Update the image 
                self.image = PhotoImage(file="data/assets/infant_image.png")
                self.image_label.configure(image=self.image)
                self.image_label.image = self.image # Keep a reference to avoid garbage collection
            elif self.turn_count==365:
                # Update the image 
                self.image = PhotoImage(file="data/assets/toddler_image.png")
                self.image_label.configure(image=self.image)
                self.image_label.image = self.image # Keep a reference to avoid garbage collection
            elif self.turn_count==1095:
                # Update the image 
                self.image = PhotoImage(file="data/assets/preschooler_image.png")
                self.image_label.configure(image=self.image)
                self.image_label.image = self.image # Keep a reference to avoid garbage collection
            elif self.turn_count==2190:
                # Update the image 
                self.image = PhotoImage(file="data/assets/adolescent_image.png")
                self.image_label.configure(image=self.image)
                self.image_label.image = self.image # Keep a reference to avoid garbage collection
            elif self.turn_count==4015:
                # Update the image 
                self.image = PhotoImage(file="data/assets/preteen_image.png")
                self.image_label.configure(image=self.image)
                self.image_label.image = self.image # Keep a reference to avoid garbage collection
            elif self.turn_count==4745:
                # Update the image 
                self.image = PhotoImage(file="data/assets/teen_image.png")
                self.image_label.configure(image=self.image)
                self.image_label.image = self.image # Keep a reference to avoid garbage collection

            if self.turn_count==6570:
                self.end_game_victory()


        if self.spinbox_values[0].get():
            self.turn_count += 1
            
    def multi_increment_turn(self,number):
        for _ in range(number):
            self.increment_turn()
    
    def update_buy_button_states(self):
        if self.current_money < 50: 
            self.buy_nut_supp.config(state="disabled")
            self.buy_doc.config(state="disabled") 
            self.buy_party.config(state="disabled")
            self.buy_toy.config(state="disabled")
            self.buy_meal.config(state="disabled")
            
        else: 
            self.buy_nut_supp.config(state="normal")
            self.buy_doc.config(state="normal") 
            self.buy_party.config(state="normal")
            self.buy_toy.config(state="normal")
            self.buy_meal.config(state="normal")

    def update_frame_colors(self):
        for category, label in self.needs_labels.items():
            value = label.cget("text")
            try: 
                value = int(value)
                if value < 25: 
                    self.needs_frames[category].config(bg="firebrick1")
                    self.needs_labels[category].config(bg="firebrick1")
                    self.needs_category_labels[category].config(bg="firebrick1")
                elif value < 50:
                    self.needs_frames[category].config(bg="yellow")
                    self.needs_labels[category].config(bg="yellow")
                    self.needs_category_labels[category].config(bg="yellow")
                else:
                    self.needs_frames[category].config(bg="lightgreen")
                    self.needs_labels[category].config(bg="lightgreen") 
                    self.needs_category_labels[category].config(bg="lightgreen") 
            except ValueError:
                self.needs_frames[category].config(bg="white")
                self.needs_labels[category].config(bg="white")
                self.needs_category_labels[category].config(bg="white")
            
    def update_skill_trees(self,skills):
        # Clear existing labels in the frames
        for frame in self.skill_frames.values(): 
            for widget in frame.winfo_children(): 
                widget.destroy()

        # Populate frames with skill labels using grid 
        for tree, skill_list in skills.items():
            if len(skill_list)>0:
                for i, skill in enumerate(reversed(skill_list)):
                    label = tk.Label(self.skill_frames[tree], text=skill,bg="lightblue")
                    label.grid(row=i, column=0, pady=2, sticky="w")


    def update_attributes(self):
        # Get all of the actions from the day
        action_dict = {}
        for i in range(len(self.spinbox_list)):
            action_dict[self.actions[i]] = self.spinbox_values[i].get()

        print(action_dict)
        # iterate over each key and calculate new child values
        for key in action_dict:
            action_amount = int(action_dict[key])
            while action_amount>0:
                self.child.process_action(key)
                action_amount= action_amount-1

        # Also do the baby's normal daily update
        self.child.update_turn()

    # Not actually sure i want to do this, maybe have better default values or just keep the last days values - otherwise you are constantly putting in the same info
    def reset_spinbox_values(self):
        # Reset all spinbox values to 0
        default_vals = ["32","4","2", "2","5","2","1"]
        for val in range(len(self.spinbox_values)):
            self.spinbox_values[val].set(default_vals[val])

    def save_game(self):
        save_slot = simpledialog.askstring("Save Game", "Enter save slot name:")
        if save_slot: 
            with open(f"data\game_saves\{save_slot}.pkl", "wb") as f: 
                game_state = {"turn":self.turn_count,
                                  "parent":self.parent,
                                  "child":self.child,
                                  "difficulty":self.parent_income,
                                  "current_money":self.current_money}
                pickle.dump(game_state, f)
            messagebox.showinfo("Game Saved", f"Game saved in slot: {save_slot}") 
            print(f"Game saved in slot: {save_slot}") 
            
    def load_game(self): 
        load_slot = simpledialog.askstring("Load Game", "Enter save slot name:")
        if load_slot:
            try: 
                with open(f"data\game_saves\{load_slot}.pkl", "rb") as f:
                    game_state = pickle.load(f)
                if self.turn_count==0:
                    self.parent_income = game_state["difficulty"]
                    self.name_label.grid_forget()
                    self.turn_label.grid_forget()
                    self.name_entry.grid_forget()
                    self.child_label.grid_forget()
                    self.child_info.grid_forget()
                    self.child_entry.grid_forget()
                    self.parent_income_label.grid_forget()
                    self.option_menu.grid_forget()
                    self.start_game_button.grid_forget()
                    self.restart_button.grid_forget()
                    self.load_button.grid_forget()
                    self.remaining_label.grid(row=7, column=0,pady=3)

                    for i in range(len(self.spinbox_list)):
                        #self.spin_labels[i].grid(pady=5,row=i+8, column=0, sticky="n")  
                        #self.spinbox_list[i].grid(pady=5,row=i+8, column=0, sticky="s")
                        self.spin_labels[i].grid(padx=3,row=8, column=i%7, sticky="n")  
                        self.spinbox_list[i].grid(padx=3,row=9, column=i%7, sticky="s")

                    self.child_info.grid()

                    frame_image = tk.Frame(self.root,bg="white")
                    frame_image.grid(row=11,pady=5,padx=5)
                    self.image_label = tk.Label(frame_image, image=self.image,bg="white")
                    self.image_label.grid(row=11,column=0%4,rowspan=4,padx=5)
                    self.next_turn_button = tk.Button(frame_image, text="Next Day", command=self.increment_turn,bg="lightgreen")
                    self.next_5turn_button = tk.Button(frame_image, text="Advance 5 Days", command=lambda: self.multi_increment_turn(5),bg="lightgreen")
                    self.next_10turn_button = tk.Button(frame_image, text="Advance 10 Days", command=lambda: self.multi_increment_turn(10),bg="lightgreen")
                    self.next_turn_button.grid(row=11,column=1%4,rowspan=1)
                    self.next_5turn_button.grid(row=12,column=1%4,rowspan=1)
                    self.next_10turn_button.grid(row=13,column=1%4,rowspan=1)
                    # Create a frame for income
                    self.income_frame = tk.Frame(frame_image, bd=2, relief="groove",bg="white")
                    self.income_frame.grid(row=14,column=1)
                    # Create a label for the score value
                    self.current_money = game_state["current_money"]
                    self.income_label = tk.Label(self.income_frame, text=f"${self.current_money}", font=("Helvetica", 12),bg="white")
                    self.income_label.grid()
                    self.income_category_label = tk.Label(self.income_frame, text="Current money from "+self.parent_income, font=("Helvetica", 10),bg="white") 
                    self.income_category_label.grid()

                    # Create buttons to spend money
                    self.buy_nut_supp = tk.Button(frame_image, text="Buy nutrition supplements ($50)", command=lambda: self.buy_needs(["Energy"], 20),bg="lightyellow")
                    self.buy_doc = tk.Button(frame_image, text="See a doctor ($50)", command=lambda: self.buy_needs(["Health"], 20),bg="lightyellow")
                    self.buy_party = tk.Button(frame_image, text="Host a social event ($50)", command=lambda: self.buy_skills(["Social Skills","Communication Skills"], 20),bg="lightyellow")
                    self.buy_toy = tk.Button(frame_image, text="Buy a new toy ($50)", command=lambda: self.buy_needs(["Love for Parent"], 20),bg="lightyellow")
                    self.buy_meal = tk.Button(frame_image, text="Go out to eat ($50)", command=lambda: self.buy_needs(["Hunger"], 20),bg="lightyellow")
                    # add in the buy buttons
                    self.buy_nut_supp.grid(row=11,column=2%4,rowspan=1)
                    self.buy_doc.grid(row=12,column=2%4,rowspan=1) 
                    self.buy_party.grid(row=13,column=2%4,rowspan=1)
                    self.buy_toy.grid(row=11,column=3%4,rowspan=1)
                    self.buy_meal.grid(row=12,column=3%4,rowspan=1)
                    self.update_buy_button_states()

                    #self.parent_info.grid()
                    self.restart_button.grid()
                    self.save_button.grid()

			        # Create the parent
                    self.parent=game_state["parent"]

                    # Create the child
                    self.child=game_state["child"]
                    self.turn_count = game_state["turn"]

                # Increment turn (but without adding stuff)
                self.parent_info.config(text=str(self.parent.examine_self_return()))
                turn_attrib, turn_needs, turn_physical,turn_skills, turn_text  =self.child.examine_child()
                print(turn_attrib)
                print(turn_needs)
                self.reset_spinbox_values()
                # Update the labels with the new attribs
                for key, value in self.needs_labels.items():
                    self.needs_labels[key].config(text=turn_needs[key])

                self.income_label.config(text=f"${self.current_money}")

                self.update_buy_button_states()

                # update the frame colors
                self.update_frame_colors()

                # update skills
                self.update_skill_trees(turn_skills)

                # Update the labels with the new needs
                for key, value in self.attributes_labels.items():
                    self.attributes_labels[key].config(text=turn_attrib[key])

                # Update the labels with the new needs
                for key, value in self.physical_labels.items():
                    self.physical_labels[key].config(text=turn_physical[key])

                self.child_info.config(text=str(turn_text))

                messagebox.showinfo("Game Loaded", f"Game loaded from slot: {load_slot}") 
                print(f"Game loaded from slot: {load_slot}")
            except FileNotFoundError: 
                print(f"No saved game found in slot: {load_slot}") 

    def run(self):
        self.root.mainloop()

def main():
    root = tk.Tk()
    root.configure(bg="white")
    root.title("Parental Idle Game") 
    root.geometry("1000x850")
    root.resizable(True, True)
    app = TurnTrackerApp(root)
    app.run()

if __name__ == "__main__":
    main()
