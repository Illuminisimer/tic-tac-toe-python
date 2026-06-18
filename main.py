#a GUI based tic tac toe game in puthon

from tkinter import *
import random

def next_turn(row, column):
    global player
    
    if buttons[row][column]['text']=="" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if check_winner is False:
                player = players[1]
                label.config(text = (players[1] + " turn"))
def check_winner():
    pass

def empty_spaces():
    pass

def new_game():
    pass

def center_and_resize(window, width, height):
    # Update tasks so window width/height are accurately recognized before mapping
    window.update_idletasks()
    # Get total screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # Calculate starting x and y coordinates to center the window
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    
    # Set the geometry: "widthxheight+x+y"
    window.geometry(f"{width}x{height}+{x}+{y}")

window = Tk()
window.title("TIC TAC TOE")
height = 800
width = 450
center_and_resize(window, width, height)
window.resizable(True, True)

players = ["X", "0"]
player = random.choice(players)
buttons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

label = Label(text = player + ' turn', font=("Calibri", 30))
label.pack(side="top")

reset = Button(text = "Restart", font=("calibri", 40), command=new_game)
reset.pack(side="top")
frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text = "", font=("calibri", 40), width=5, height=2,
                                      command = lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row, column=column)
window.mainloop()