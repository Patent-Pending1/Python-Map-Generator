import tkinter as tk
from Risk import board
# generates a board form the risk.py
board = board(65)

root = tk.Tk()
root.title("risk")

# this set the size of the square make it what ever
square_size = 10

# random tk stuff (did not steal from there webstie)
canvas = tk.Canvas(root, width=len(board[0])*square_size, height=len(board)*square_size)
canvas.pack()

# goes through the board
for y, row in enumerate(board):
    for x, value in enumerate(row):
        # i will work on this next to make it change colors base on the space
        color = 'blue' if value == ' ' else 'green'
        canvas.create_rectangle(x*square_size, y*square_size, (x+1)*square_size, (y+1)*square_size, fill=color)

root.mainloop()
