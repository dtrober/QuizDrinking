import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import os



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
        if self.drink_count > 5:
            self.avatar_image = self.load_image(self.avatar_paths[2])
        elif self.drink_count > 3:
            self.avatar_image = self.load_image(self.avatar_paths[1])
        self.label.configure(image=self.avatar_image)
root = tk.Tk()
root.title("Drinking Game")

# Each player's avatars
tex_avatars = [os.path.join("Avatars", f"Tex{i}.png") for i in range(1, 5)]
nova_avatars = [os.path.join("Avatars", f"Nova{i}.png") for i in range(1, 5)]
sneeze_avatars = [os.path.join("Avatars", f"Sneeze{i}.png") for i in range(1, 5)]

avatars_paths_for_player = [
    [os.path.join("Avatars", "tex1.png"), os.path.join("Avatars", "tex2.png"), os.path.join("Avatars", "tex3.png")],
    # ... add more lists for other players if they have different avatars
]

# Load your players (You can add more players and their respective avatar images)
players = [
    Player("Tex", tex_avatars),
    Player("Nova", nova_avatars),
    Player("Sneeze", sneeze_avatars)
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

questions_data = {
    "Wildlife Managment": [
        {"text": "Water!", "statement": "Is this a banana?", "drinks": 2},
        {"text": "A drink!", "statement": "Is this an apple?", "drinks": 2},
        {"text": "Chug it!", "statement": "Is this a banana?", "drinks": 2},
        {"text": "A shot!", "statement": "Is this a banana?", "drinks": 2},
        {"text": "Mysterious!", "statement": "Is this a banana?", "drinks": 2}
    ],
    "Aviation!": [
        {"text": "Water!", "statement": "Is this a banana?", "drinks": 2},
        {"text": "A drink!", "statement": "Is this an apple?", "drinks": 2},
        {"text": "Chug it!", "statement": "Is this a banana?", "drinks": 2},
        {"text": "A shot!", "statement": "Is this a banana?", "drinks": 2},
        {"text": "Mysterious!", "statement": "Is this a banana?", "drinks": 2}
    ],
    "Micro Biology!": [
        {"text": "Water!", "statement": "Is this a banana?", "drinks": 2},
        {"text": "A drink!", "statement": "Is this an apple?", "drinks": 2},
        {"text": "Chug it!", "statement": "Is this a banana?", "drinks": 2},
        {"text": "A shot!", "statement": "Is this a banana?", "drinks": 2},
        {"text": "Mysterious!", "statement": "Is this a banana?", "drinks": 2}
    ],
    "3D Modeling!": [
        {"text": "Water!", "statement": "Is this a banana?", "drinks": 2},
        {"text": "A drink!", "statement": "Is this an apple?", "drinks": 2},
        {"text": "Chug it!", "statement": "Is this a banana?", "drinks": 2},
        {"text": "A shot!", "statement": "Is this a banana?", "drinks": 2},
        {"text": "Mysterious!", "statement": "Is this a banana?", "drinks": 2}
    ],
    "Communications (Very special Digital Arts)!": [
        {"text": "Water!", "statement": "Is this a banana?", "drinks": 2},
        {"text": "A drink!", "statement": "Is this an apple?", "drinks": 2},
        {"text": "Chug it!", "statement": "Is this a banana?", "drinks": 2},
        {"text": "A shot!", "statement": "Is this a banana?", "drinks": 2},
        {"text": "Mysterious!", "statement": "Is this a banana?", "drinks": 2}
    ]
}

def show_question(question_text, statement, drinks):
    def assign_drinks_to_player():
        player_name = player_var.get()
        for player in players:
            if player.name == player_name:
                for _ in range(drinks):  # Call the drink method based on the number of drinks
                    player.drink()
                popup.destroy()

    def accept_challenge():
        popup.destroy()
        drink_assignment_popup = tk.Toplevel(root)
        drink_assignment_popup.title("Assign Drinks")

        lbl = tk.Label(drink_assignment_popup, text=f"Assign {drinks} drinks to:", font=("Arial", 16))
        lbl.pack(pady=20)

        player_var = tk.StringVar(drink_assignment_popup)
        player_dropdown = tk.OptionMenu(drink_assignment_popup, player_var, *[player.name for player in players])
        player_dropdown.pack(pady=20)

        assign_btn = tk.Button(drink_assignment_popup, text="Assign", command=assign_drinks_to_player)
        assign_btn.pack(pady=20)

    
    popup = tk.Toplevel(root)
    popup.attributes('-fullscreen', True)
    lbl_question = tk.Label(popup, text=statement, font=("Arial", 24))
    lbl_question.pack(pady=200)
    
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
        btn = tk.Button(root, text=question_text, command=lambda q=question_text, s=statement, d=drinks: show_question(q, s, d), padx=10, pady=10)
        btn.grid(row=row, column=col, sticky="nsew")
root.mainloop()
