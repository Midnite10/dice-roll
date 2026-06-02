import tkinter as tk
import random

# constants
DICE_LOWER_LIMIT = 1
DICE_HIGHER_LIMIT = 6
MAIN_BG = "white"
SPECIAL_BG = "green"
PRIMARY_FONT = "Arial 24"
SECONDARY_FONT = "Arial 16"
FONT_COLOUR = "black"

# Class for the dice rolling system
class DiceRoll:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roll")
        self.root.config(MAIN_BG)

        # styles
        self.style = PRIMARY_FONT
        self.background = MAIN_BG
        self.counter = 0 

        self.root.rowconfigure([0, 1, 2], minsize=64)
        self.root.columnconfigure([0, 1], minsize=192)

        self.create_widgets()

    # Creates the widgets on the window for the user to interact with
    def create_widgets(self):
        self.quit_btn = tk.Button(self.root, text="Quit", command=self.quit)
        self.quit_btn.grid(row=0, column=0, sticky="nwe")

        self.roll_btn = tk.Button(self.root, text="Roll", command=self.roll_dice)
        self.roll_btn.grid(row=0, column=1, sticky="nwe")

        self.dice1_display = tk.Label(self.root, text="", font=self.style, bg=self.background)
        self.dice1_display.grid(row=1, column=0, sticky="we")
        
        self.dice2_display = tk.Label(self.root, text="", font=self.style, bg=self.background)
        self.dice2_display.grid(row=1, column=1, sticky="we")

        self.roll_count_label = tk.Label(self.root, text="Roll count: 0", font=SECONDARY_FONT, fg=FONT_COLOUR, bg=self.background)
        self.roll_count_label.grid(row=2, column=0, sticky="we")

    # Quits program when quit button is pressed
    def quit(self):
        self.root.destroy()
    
    # Changes background to green when double sixes are rolled
    def change_bg(self):
        self.root.config(bg=SPECIAL_BG)

    # Rolls dice each time roll button is pressed
    def roll_dice(self):
        self.root.config(bg=MAIN_BG)
        dice_1 = random.randint(DICE_LOWER_LIMIT, DICE_HIGHER_LIMIT)
        dice_2 = random.randint(DICE_LOWER_LIMIT, DICE_HIGHER_LIMIT)

        self.dice1_display.config(text=dice_1)
        self.dice2_display.config(text=dice_2)

        self.counter += 1
        self.roll_count_label.config(text=f"Roll count: {self.counter}")

        if dice_1 == 6 and dice_2 == 6:
            self.change_bg()

# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRoll(root)
    root.mainloop()