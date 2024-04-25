import tkinter as tk
from Risk import board
from Risk import neighbors
# generates a board form the risk.py
n = 60
board = board(n)

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
        if value == " ":
            if neighbors(board,"water",x,y,n) == 1:
                color = "#0ec7c1"
            elif neighbors(board,"water",x,y,n) == 2 or neighbors(board,"water",x,y,n) == 3:
                color = "#0e80c7"
            else:
                color = "blue"
        else:
            color = 'green'
        canvas.create_rectangle(x*square_size, y*square_size, (x+1)*square_size, (y+1)*square_size, fill=color)

root.mainloop()
