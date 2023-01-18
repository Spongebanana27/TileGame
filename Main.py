
import Board
import tkinter as tk

hexes = ["#ff0000", "#ff8700", "#ffd300", "#deff0a", "#a1ff0a", "#0aff99", "#0aefff", "#147df5", "#580aff", "#be0aff"]


rows = 10
cols = 10
global selectedColor
selectedColor = 0

def updateWindow():
    global numTurns
    numTurns += 1
    numturnsLabel.config(text="Total moves: \n" + str(numTurns))
    for column in range(b.width):
        for row in range(b.height):
            val = b.rep[row][column]
            buttons[row][column].configure(bg=hexes[val])

def update(x, y):
    b.updateFirstTile(x, y, selectedColor)

def newColor(x):
    global selectedColor
    selectedColor = x
    currentPick.configure(bg=hexes[selectedColor])

b = Board.Board(rows, cols)

window = tk.Tk()

## Generate buttons
buttons = [[0 for x in range(b.width)] for y in range(b.height)] 
for column in range(b.width):
    for row in range(b.height):
        buttons[row][column] = tk.Button(command=lambda x1=row, y1=column:{update(x1, y1), updateWindow()}, width=10,height=5)
        buttons[row][column].grid(column=column,row=row)

currentPick = tk.Button(width = 10, height = 5, bg=hexes[selectedColor])
currentPick.grid(row=1,column=cols, padx=10)
numTurns = 0
numturnsLabel = tk.Label(text="Total moves: \n" + str(numTurns), width=10,height=5)
numturnsLabel.grid(row=0,column=cols)

## Generate buttons to select a color
selectors = [[0 for x in range(b.width)] for y in range(b.height)] 
for i in range(len(hexes)):
    selectors[i] = tk.Button(command = lambda x1=i :newColor(x1), width=10, height=5,bg=hexes[i])
    selectors[i].grid(column=cols+1,row=i)
    

updateWindow()

window.mainloop()
