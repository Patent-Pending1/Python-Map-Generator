import random
from random import choice
import tkinter as tk
from Risk import Generation
from Risk import neighbors
from Risk import finalGen
# generates a board form the risk.py
n = 200
board = finalGen(n)
root = tk.Tk()
root.title("risk")

# this set the size of the square make it what ever
square_size = 5

# random tk stuff (did not steal from there webstie)
canvas = tk.Canvas(root, width=len(board[0])*square_size, height=len(board)*square_size)
canvas.pack()

# goes through the board
for y, row in enumerate(board):
    for x, values in enumerate(row):
        if values.count('I') == 1:
            color = '#7390B5'
        elif values.count('-') == 1:
            if neighbors(board,"water",x,y,n) == 1:
                if y > (n*3//5)*(1/4) and y < (n*3//5)*(3/4):
                    color = "#F6F693"
                else:
                    color = "#414040"
            elif neighbors(board,"water",x,y,n) == 2 or neighbors(board,"water",x,y,n) == 3:
                color = "#0e80c7"
            else:
                hexValues = ['#003186','#1B0794','#001A82']
                color = choice(hexValues)
        elif values.count('^') > 0:
            e = str(6-values.count('^'))
            color = '#'+e+'0'+e+'0'+e+'0'
        elif values.count('!') == 1 or values.count('!!') == 1:
            color = '#FFFFFF'
        elif values.count('@') == 1:
            hexValues = ['#e3e100','#C9C800','#9C9B00','#BDBB1C','#FFFD00']
            color = choice(hexValues)
        elif values.count('&') == 1:
            hexValues = ['#C2823A','#9E692C','#AD722F','#A16B2F','#805321']
            color = choice(hexValues)
        elif values.count('#') == 1:
            hexValues = ['#013220','#014220','#013810']
            color = choice(hexValues)
        elif values.count('+') == 1 or values.count('%') == 1:
            hexValues = ['#027D00','#028D00','#026D00','#025F00']
            color = choice(hexValues)
        canvas.create_rectangle(x*square_size, y*square_size, (x+1)*square_size, (y+1)*square_size, fill=color)

root.mainloop()
