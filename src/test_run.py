import tkinter as tk
from character_classes import parental_unit, baby
import random
from tkinter import messagebox
from tkinter import ttk

class TurnTrackerApp:
    def __init__(self, root):
        self.root = root
        self.turn_count = 0
        self.name = ""  # Initialize an empty name
        self.child_gender=random.choice(["boy","girl"]) 

        # Create widgets
        self.turn_label = tk.Label(self.root, text="Day: 0")
        self.start_game_button = tk.Button(self.root, text="Start Game", command=self.increment_turn)
        self.next_turn_button = tk.Button(self.root, text="Next Day", command=self.increment_turn)
        self.next_5turn_button = tk.Button(self.root, text="Advance 5 Days", command=lambda: self.multi_increment_turn(5))
        self.next_10turn_button = tk.Button(self.root, text="Advance 10 Days", command=lambda: self.multi_increment_turn(10))
        self.name_label = tk.Label(self.root, text="Enter your name:")
        self.child_label = tk.Label(self.root, text=f"You and your partner have just had your first child, it's a {self.child_gender}! Please give them a name:")
        self.name_entry = tk.Entry(self.root)  # Add an entry widget for the name
        self.child_entry = tk.Entry(self.root)  # Add an entry widget for the name
        self.name_entry.insert(0, "John")
        self.child_entry.insert(0, "GB")
        self.parent_info = tk.Label(self.root, text="Result will appear here")
        self.child_info = tk.Label(self.root, text="")

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
        frame = tk.Frame(self.root)
        frame.grid(pady=5)
        # Create the score boxes with labels
        for i, (category, score) in enumerate(starting_needs_dict.items()): 
            # Create a frame for each score box
            needs_frame = tk.Frame(frame, bd=2, relief="groove")
            needs_frame.grid(row=i//9, column=i%9, padx=2, pady=5)
            self.needs_frames[category] = needs_frame
            # Create a label for the score value
            needs_label = tk.Label(needs_frame, text=score, font=("Helvetica", 12)) 
            needs_label.grid(row=0, column=0, pady=5) 
            self.needs_labels[category] = needs_label 
            # Create a label for the category 
            needs_category_label = tk.Label(needs_frame, text=category, font=("Helvetica", 10)) 
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
        frame2 = tk.Frame(self.root)
        frame2.grid(pady=5)
        # Create the score boxes with labels
        for i, (category, score) in enumerate(starting_attributes_dict.items()): 
            # Create a frame for each score box
            attributes_frame = tk.Frame(frame2, bd=2, relief="groove")
            attributes_frame.grid(row=i//6, column=i%6, padx=2, pady=5)
            # Create a label for the score value
            attributes_label = tk.Label(attributes_frame, text=score, font=("Helvetica", 12)) 
            attributes_label.grid(row=0, column=0, pady=5) 
            self.attributes_labels[category] = attributes_label 
            # Create a label for the category 
            attributes_category_label = tk.Label(attributes_frame, text=category, font=("Helvetica", 10)) 
            attributes_category_label.grid(row=1, column=0)

        starting_physical_dict = {
                "Name":0,
                "Age (category)":0,
                "Age (days)":0,
                "Weight (lbs)":0,
                "Height (in)":0}
        # Create a dictionary to hold the labels for dynamic updates 
        self.physical_labels = {} 
        frame3 = tk.Frame(self.root)
        frame3.grid(pady=5)
        # Create the score boxes with labels
        for i, (category, score) in enumerate(starting_physical_dict.items()): 
            # Create a frame for each score box
            physical_frame = tk.Frame(frame3, bd=2, relief="groove")
            physical_frame.grid(row=i//6, column=i%6, padx=2, pady=5)
            # Create a label for the score value
            physical_label = tk.Label(physical_frame, text=score, font=("Helvetica", 12)) 
            physical_label.grid(row=0, column=0, pady=5) 
            self.physical_labels[category] = physical_label 
            # Create a label for the category 
            physical_category_label = tk.Label(physical_frame, text=category, font=("Helvetica", 10)) 
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
        self.restart_button = tk.Button(self.root, text="Restart", command=restart)
        
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
        frame4 = tk.Frame(self.root)
        frame4.grid(pady=5)
        self.actions = ["Sleep","Feed","Play", "Teach","Clean","Do Nothing","Bonding Time"]
        for i in range(len(self.actions)):
            spinbox_value_i = tk.StringVar()
            spinbox = tk.Spinbox(frame4, from_=0, to=48, command=lambda i=i: on_spinbox_change(i),
                                 state="readonly", textvariable=spinbox_value_i)
            label = tk.Label(frame4, text=f"{self.actions[i]}")
            self.spinbox_list.append(spinbox)
            self.spinbox_values.append(spinbox_value_i)
            self.spin_labels.append(label)

        self.remaining_label = tk.Label(self.root, text="Remaining 30 min time chunks: 0")
        
        # grid widgets
        self.child_info.grid(row=4, column=0,pady=3)
        self.turn_label.grid(row=5, column=0,pady=3)
        self.name_label.grid(row=6, column=0)
        self.name_entry.grid(row=7, column=0)
        self.child_label.grid(row=8, column=0)
        self.child_entry.grid(row=9, column=0)

        self.start_game_button.grid(row=10, column=0)
        self.restart_button.grid(row=11, column=0)
        
    def end_game(self): 
        messagebox.showinfo("Game Over", f"Your child {self.child.name} died after {self.child.age_days} days. Better luck next time!") 
        self.root.quit() # Close the game window

    def end_game_victory(self): 
        messagebox.showinfo("Game Over", f"Your child {self.child.name} turned 18 and is ready to leave the house. Better luck next time!") 
        self.root.quit() # Close the game window
    
    def increment_turn(self):

        # Turn 0 is setup, add an introduction of your child (randomly you and your spouse have just had a boy/girl, what would you like to name it?)
        if self.turn_count==0:
            self.name = self.name_entry.get()
            self.child_name = self.child_entry.get()
            self.name_label.grid_forget()
            self.turn_label.grid_forget()
            self.name_entry.grid_forget()
            self.child_label.grid_forget()
            self.child_entry.grid_forget()
            self.start_game_button.grid_forget()
            self.restart_button.grid_forget()
            self.remaining_label.grid(row=7, column=0,pady=3)

            for i in range(len(self.spinbox_list)):
                #self.spin_labels[i].grid(pady=5,row=i+8, column=0, sticky="n")  
                #self.spinbox_list[i].grid(pady=5,row=i+8, column=0, sticky="s")
                self.spin_labels[i].grid(padx=3,row=8, column=i%7, sticky="n")  
                self.spinbox_list[i].grid(padx=3,row=9, column=i%7, sticky="s")

            self.next_turn_button.grid()
            self.next_5turn_button.grid()
            self.next_10turn_button.grid()
            self.parent_info.grid()
            self.restart_button.grid()
            
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
            #self.child_info.config(text=str(self.child.examine_child()))
            turn_attrib, turn_needs, turn_physical,turn_skills, turn_text  =self.child.examine_child2()
            print(turn_attrib)
            print(turn_needs)
            
            # Update the labels with the new attribs
            for key, value in self.needs_labels.items():
                self.needs_labels[key].config(text=turn_needs[key])

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
            

        if self.spinbox_values[0].get():
            self.turn_count += 1
            
    def multi_increment_turn(self,number):
        for _ in range(number):
            self.increment_turn()

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
        # Populate frames with skill labels using grid 
        for tree, skill_list in skills.items():
            if len(skill_list)>0:
                for i, skill in enumerate(reversed(skill_list)):
                    label = tk.Label(self.skill_frames[tree], text=skill)
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
        self.child.update_turn(self.child.age)

    # Not actually sure i want to do this, maybe have better default values or just keep the last days values - otherwise you are constantly putting in the same info
    def reset_spinbox_values(self):
        # Reset all spinbox values to 0
        default_vals = ["32","4","2", "2","5","2","1"]
        for val in range(len(self.spinbox_values)):
            self.spinbox_values[val].set(default_vals[val])

    def run(self):
        self.root.mainloop()

def main():
    root = tk.Tk()
    root.title("Parental Idle Game") 
    root.geometry("1000x850")
    app = TurnTrackerApp(root)
    app.run()

if __name__ == "__main__":
    main()
