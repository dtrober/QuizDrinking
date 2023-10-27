import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import os

questions_data = {
    "Wildlife Managment": [
        {"text": "Big Drink!", "statement": "Name one tool used in wildlife management for tracking animals.", "correct" : "Tracking Collars", "drinks": 1},
        {"text": "Chug it!", "statement": "What is the term for the minimum viable population size below which a species is likely to go extinct?", "choices": ["MVP", "FPT", "LQA", "APM"], "correct": "MVP (Minimum Viable Population)", "drinks": 1},
        {"text": "Shot with a chaser!", "statement": "What is the practice of deliberately moving a species to a new location called?", "choices": ["Translocation", "Transposition", "Transference", "Transmutation"], "correct": "Translocation", "drinks": 2},
        {"text": "Shot no chaser!", "statement": "What is the primary objective of the 'Rewilding' approach in conservation?", "correct": "To restore and protect natural processes and core wilderness areas.","drinks": 2},
        {"text": "Two Shots!", "statement": "Name the phenomenon where fragmented habitats can lead to species being trapped in small areas, leading to reduced gene flow and increased vulnerability.", "correct": "Island Biogeography Theory", "drinks": 3},
    ],
    "Aviation!": [
        {"text": "Big Drink!", "statement": "In which part of the airplane would you find the empennage?", "choices": ["The tail section.", "The wingtip.", "The fuselage.", "The nose cone."], "correct": "The tail section.", "drinks": 1},
        {"text": "Chug it!", "statement": "In aviation management, what is the primary role of an FBO?", "correct": "Fixed-Base Operator; they offer services such as fueling, hangaring, tie-down and parking, aircraft rental, and maintenance.", "drinks": 2},
         {"text": "Shot with a chaser!", "statement": "What does IFR stand for in aviation?", "choices": ["Intuitive Flight Regulations.", "Interior Flight Routines.", "Integral Flight Radios.", "Instrument Flight Rules."], "correct": " Instrument Flight Rules.", "drinks": 2},
        {"text": "Shot no chaser!", "statement": "For instrument rating, what is the significance of 'Decision Altitude' or 'Decision Height'?", "correct": " It's the altitude or height at which a decision must be made during an instrument approach to either continue the landing or execute a missed approach.", "drinks": 2},
        {"text": "Two Shots!", "statement": " In aviation management, which principle is essential for ensuring efficient runway operations at busy airports?","choices": ["Queue scheduling or time queue distribution.", "Slot management or time slot allocation.", "Time block organization.", "Interval coordination or time period assignment."], "correct": "Slot management or time slot allocation.", "drinks": 3},
    ],
    "Micro Biology!": [
        {"text": "Big Drink!", "statement": "What is the shape of a bacillus bacterium?", "choices": ["Rod-shaped.", "Cone-shaped.", "Spiral-shaped.", "Disk-shaped."], "correct": "Rod-shaped.", "drinks": 1},
        {"text": "Chug it!", "statement": "Which process allows bacteria to exchange genetic material through a pilus?", "choices": ["Configuration.", "Conjunction.", "Conflation.","Conjugation."], "correct": "Conjugation.", "drinks": 1},
        {"text": "Shot with a chaser!", "statement": "Which domain of microorganisms is known for thriving in extreme environments like hot springs or acidic lakes?", "choices": ["Bacteria.", "Eukarya.", "Archaea.", "Protozoa."], "correct": "Archaea.", "drinks": 2},
        {"text": "Shot no chaser!", "statement": "Which molecule, found in the cell walls of bacteria, can induce a strong immune response in animals?", "choices": ["Lipopolysaccharide (LPS).", "Lipoglycoprotein (LGP).", "Lipoproteinase (LPA).", "Glycolipoprotein (GLP)."], "correct": "Lipopolysaccharide (LPS).", "drinks": 2.5},
        {"text": "Two Shots!", "statement": " What is the significance of the 'RNA world' hypothesis in the context of the origin of life?", "correct": "It proposes that self-replicating ribonucleic acid (RNA) molecules were precursors to current life (which is based on deoxyribonucleic acid, DNA).", "drinks": 3},
    ],
    "3D Modeling!": [
        {"text": "Big Drink!", "statement": "Which software is commonly used for graphic design and photo editing?", "correct": "Adobe Photoshop." , "drinks": 1},
        {"text": "Chug it!", "statement": "In the context of website design, what does 'UX' stand for?", "correct": "User Experience" , "drinks": 1},
        {"text": "Shot with a chaser!", "statement": "In digital marketing, what is the primary purpose of SEO?", "correct": "Search Engine Optimization; to improve the visibility of a website or web page on search engine results." , "drinks": 2},
        {"text": "Shot no chaser!", "statement": "In digital storytelling, what is the concept of 'transmedia storytelling'?", "correct": "Telling a story across multiple platforms and formats using digital technologies." , "drinks": 2},
        {"text": "Two Shots!", "statement": "What is the significance of 'vector graphics' in digital design?", "correct": " Vector graphics are based on mathematical paths and can be scaled without losing quality." , "drinks": 3},
    ],
    "Communications (Very special Digital Arts)!": [
        {"text": "Big Drink!", "statement": "Which tool in 3D modeling software allows you to stretch, compress, or twist a model?", "correct": "The 'scale' tool.", "drinks": 1},
        {"text": "Chug it!", "statement": "What is the primary purpose of 'rigging' in 3D modeling?", "correct": "To create a skeletal structure that can be used to animate and pose a model.", "drinks": 1},
        {"text": "Shot with a chaser!", "statement": "What technique involves creating a high-resolution model, then deriving a lower-resolution version to use in real-time applications?",  "choices": ["Mesh retopology.", "Mesh deformation.", "Mesh subdivision.", "Mesh refactoring."], "correct": "Mesh retopology.", "drinks": 2},
        {"text": "Shot no chaser!", "statement": "How do 'NURBS' differ from polygon-based modeling?", "correct": "NURBS (Non-Uniform Rational B-Splines) are mathematical representations that produce smooth surfaces, while polygons are flat surfaces defined by vertices.", "drinks": 2},
        {"text": "Two Shots!", "statement": "What does the 'Subdivision Surface' technique achieve in 3D modeling?", "correct": "It refines and smoothens the surface of a model by subdividing each polygonal face into smaller faces, resulting in a smoother appearance.", "drinks": 3},
    ]
}

class Player:
    def load_image(self, path):
        """Load and resize the image."""
        base_size = (200, 200)  # Adjust this value as per your requirement
        img = Image.open(path)
        img = img.resize(base_size, Image.LANCZOS)  # Use antialiasing for smoother resize
        return ImageTk.PhotoImage(img)

    def __init__(self, name, avatar_paths):
        self.name = name
        self.avatar_paths = avatar_paths
        self.drink_count = 0
        self.avatar_image = self.load_image(self.avatar_paths[0])
        self.label = None  # Placeholder for the player's label on the GUI

    def drink(self):
        self.drink_count += 1
        if self.drink_count >= 10:
            self.avatar_image = self.load_image(self.avatar_paths[3])
        elif self.drink_count >= 7:
            self.avatar_image = self.load_image(self.avatar_paths[2])
        elif self.drink_count > 2:
            self.avatar_image = self.load_image(self.avatar_paths[1])
        else:  
            self.avatar_image = self.load_image(self.avatar_paths[0])
        # Moved this line out of the nested condition
        self.label.configure(image=self.avatar_image)
        root.update()  # Force GUI to update
        print(self.drink_count)
root = tk.Tk()
root.title("Drinking Game")

# Each player's avatars
tex_avatars = [os.path.join("Avatars", f"Tex{i}.png") for i in range(1, 5)]
nova_avatars = [os.path.join("Avatars", f"Nova{i}.png") for i in range(1, 5)]
sneeze_avatars = [os.path.join("Avatars", f"Sneeze{i}.png") for i in range(1, 5)]
lup_avatars = [os.path.join("Avatars", f"Lup{i}.png") for i in range(1, 5)]
toes_avatars = [os.path.join("Avatars", f"Toes{i}.png") for i in range(1, 5)]
avatars_paths_for_player = [
    [os.path.join("Avatars", "tex1.png"), os.path.join("Avatars", "tex2.png"), os.path.join("Avatars", "tex3.png")],
    # ... add more lists for other players if they have different avatars
]

# Load your players (You can add more players and their respective avatar images)
players = [
    Player("Tex", tex_avatars),
    Player("Nova", nova_avatars),
    Player("Sneeze", sneeze_avatars),
    Player("Lup", lup_avatars),
    Player("Toes", toes_avatars)
    # ... Add more players as needed
]

# Display players' avatars at the bottom of the screen
for index, player in enumerate(players):
    player.label = tk.Label(root, image=player.avatar_image, text=player.name, compound="top")
    player.label.grid(row=6, column=index, sticky="nsew")
    root.grid_columnconfigure(index, weight=1)

# Configure weights for rows and columns
for i in range(6):  # 5 rows of questions + 1 row for categories
    root.grid_rowconfigure(i, weight=1)

for i in range(5):  # 5 columns
    root.grid_columnconfigure(i, weight=1)

def show_question(question_text, statement, drinks, choices=None, btn=None, correct_ans=None):
    player_var = tk.StringVar()
    
    drink_assignment_popup = None  # Declare the variable here at the outer function level
    popup = tk.Toplevel(root)     # Declare the popup here so it's accessible in inner functions

    def assign_drinks_to_player():
        nonlocal drink_assignment_popup  # Use the nonlocal keyword to refer to the outer variable
        player_name = player_var.get()
        for player in players:
            if player.name == player_name:
                for _ in range(drinks):  # Call the drink method based on the number of drinks
                    player.drink()
                if drink_assignment_popup:  # Check if the popup is initialized
                    drink_assignment_popup.destroy()  # Close the drink assignment popup window
                popup.destroy()  # Close the original question popup window
                if btn:  # If a button is provided, disable it
                    btn.config(state=tk.DISABLED)
                break
        

    def accept_challenge():
        nonlocal drink_assignment_popup  # Use the nonlocal keyword to refer to the outer variable
        popup.withdraw()  # Hide the popup but don't destroy it
        drink_assignment_popup = tk.Toplevel(root)
        drink_assignment_popup.title("Assign Drinks")
        
        lbl_answer = tk.Label(drink_assignment_popup, text=f"Correct Answer: {correct_ans}", font=("Arial", 16))  # Use the correct_ans variable  # Display correct answer
        lbl_answer.pack(pady=20)

        lbl = tk.Label(drink_assignment_popup, text=f"Assign {drinks} drinks to:", font=("Arial", 16))
        lbl.pack(pady=20)

        player_dropdown = tk.OptionMenu(drink_assignment_popup, player_var, *[player.name for player in players])
        player_dropdown.pack(pady=20)

        assign_btn = tk.Button(drink_assignment_popup, text="Assign", command=assign_drinks_to_player)
        assign_btn.pack(pady=20)

    popup.attributes('-fullscreen', True)
    lbl_question = tk.Label(popup, text=statement, font=("Arial", 24))
    lbl_question.pack(pady=200)
    
    # Display choices if they exist
    if choices:
        for choice in choices:
            choice_label = tk.Label(popup, text=choice, font=("Arial", 18))
            choice_label.pack(pady=10)
    
    # Button to confirm the answer and assign drinks
    btn_accept = tk.Button(popup, text="Accept Challenge", command=accept_challenge, padx=20, pady=20)
    btn_accept.pack(pady=50)

    # Close question popup button (if you want one)
    btn_close = tk.Button(popup, text="Close", command=popup.destroy, padx=20, pady=20)
    btn_close.pack(pady=50)


for col, category in enumerate(questions_data):
    label = tk.Label(root, text=category, bg="blue", fg="white", padx=10, pady=10)
    label.grid(row=0, column=col, sticky="nsew")

    for row, question in enumerate(questions_data[category], start=1):
        question_text = question['text']
        statement = question['statement']
        drinks = question['drinks']
        choices = question.get('choices')
        btn = tk.Button(root, text=question_text, padx=10, pady=10)
        btn["command"] = lambda q=question_text, s=statement, d=drinks, c=choices, b=btn, correct_ans=question['correct']: show_question(q, s, d, c, b, correct_ans)  # Set command after btn is defined
        btn.grid(row=row, column=col, sticky="nsew")
root.mainloop()