from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic-Tac-Toe')

# X will start the game
clicked = True
count = 0

# End the game
def disable_all_buttons():
    b1.config(DISABLED)
    b2.config(DISABLED)
    b3.config(DISABLED)
    b4.config(DISABLED)
    b5.config(DISABLED)
    b6.config(DISABLED)
    b7.config(DISABLED)
    b8.config(DISABLED)
    b9.config(DISABLED)

# check winner
def checkWin():
    global winner
    winner = False

# checking if X Wins
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="blue")
        b2.config(bg="blue")
        b3.config(bg="blue")
        winner = True
        messagebox.showinfo("Winner!", "Player 1 Wins!\nCongratulations!!")
        disable_all_buttons()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="blue")
        b5.config(bg="blue")
        b6.config(bg="blue")
        winner = True
        messagebox.showinfo("Winner!", "Player 1 Wins!\nCongratulations!!")
        disable_all_buttons()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="blue")
        b8.config(bg="blue")
        b9.config(bg="blue")
        winner = True
        messagebox.showinfo("Winner!", "Player 1 Wins!\nCongratulations!!")
        disable_all_buttons()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="blue")
        b4.config(bg="blue")
        b7.config(bg="blue")
        winner = True
        messagebox.showinfo("Winner!", "Player 1 Wins!\nCongratulations!!")
        disable_all_buttons()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="blue")
        b5.config(bg="blue")
        b8.config(bg="blue")
        winner = True
        messagebox.showinfo("Winner!", "Player 1 Wins!\nCongratulations!!")
        disable_all_buttons()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="blue")
        b6.config(bg="blue")
        b9.config(bg="blue")
        winner = True
        messagebox.showinfo("Winner!", "Player 1 Wins!\nCongratulations!!")
        disable_all_buttons()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="blue")
        b5.config(bg="blue")
        b9.config(bg="blue")
        winner = True
        messagebox.showinfo("Winner!", "Player 1 Wins!\nCongratulations!!")
        disable_all_buttons()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b5.config(bg="blue")
        b7.config(bg="blue")
        b3.config(bg="blue")
        winner = True
        messagebox.showinfo("Winner!", "Player 1 Wins!\nCongratulations!!")
        disable_all_buttons()

# checking if O wins
    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Winner!", "Player 2 Wins!\nCongratulations!!")
        disable_all_buttons()

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Winner!", "Player 2 Wins!\nCongratulations!!")
        disable_all_buttons()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Winner!", "Player 2 Wins!\nCongratulations!!")
        disable_all_buttons()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Winner!", "Player 2 Wins!\nCongratulations!!")
        disable_all_buttons()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Winner!", "Player 2 Wins!\nCongratulations!!")
        disable_all_buttons()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Winner!", "Player 2 Wins!\nCongratulations!!")
        disable_all_buttons()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Winner!", "Player 2 Wins!\nCongratulations!!")
        disable_all_buttons()

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b5.config(bg="red")
        b7.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Winner!", "Player 2 Wins!\nCongratulations!!")
        disable_all_buttons()

    # check if it is a tie
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It is a Tie!\nNo one Wins")
        disable_all_buttons()

# button clicked function
def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkWin()

    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkWin()

    else:
        messagebox.showerror(
            "Error!", "That box has already been selected\nPick another box")


# Start the game
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0
    # buttons
    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b3))
    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b6))
    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3,
                width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

    # grid our buttons to the screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

reset()
root.mainloop()
