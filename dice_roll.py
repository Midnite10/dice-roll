import tkinter as t
import random as r

# styles
style = "Arial 24"
background = "white"

roll_count = 0

def quit():
    root.destroy()


def change_bg():
    root.config(bg = "green")



def roll_dice():
    dice_1 = r.randint(1, 6)
    dice_2 = r.randint(1, 6)

    dice1_display.config(text = dice_1)
    dice2_display.config(text = dice_2)

    if dice_1 == 6 and dice_2 == 6:
        change_bg()

root = t.Tk()
root.title("Dice Roll")
root.config(bg = "white")

root.rowconfigure([0,1,2], minsize=64)
root.columnconfigure([0,1], minsize=192)

quit_btn = t.Button(root, text="Quit", command=quit)
quit_btn.grid(row = 0, column = 0, sticky = "nwe")

roll_btn = t.Button(root, text="Roll", command=roll_dice)
roll_btn.grid(row = 0, column = 1, sticky = "nwe")

dice1_display = t.Label(root, text="", font = style, bg = background)
dice1_display.grid(row = 1, column = 0, sticky = "we")
dice2_display = t.Label(root, text="", font = style, bg = background)
dice2_display.grid(row = 1, column = 1, sticky = "we")

roll_count = t.Label(root, text="roll count", font= "Arial 12", fg="black", bg = background)
roll_count.grid(row = 2, column = 0, sticky = "we")


root.mainloop()