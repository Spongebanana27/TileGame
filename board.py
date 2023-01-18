
import random

class Board:

    width = 6
    height = 6
    numOfValues = 10
    rep = [[]]

    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)
        self.generateRandomBoard()

    def reset(self):
        self.__init__()

    def updateFirstTile(self, row, col, new):
        old = self.rep[row][col]
        self.rep[row][col] = new
        if old != new:
            if row != 0:
                if self.rep[row - 1][col] == old:
                    self.updateTile(row - 1, col, new, old)
            if row != self.height - 1:
                if self.rep[row + 1][col] == old:
                    self.updateTile(row + 1, col, new, old)
            if col != 0:
                if self.rep[row][col - 1] == old:
                    self.updateTile(row, col - 1, new, old)
            if col != self.width - 1:
                if self.rep[row][col + 1] == old:
                    self.updateTile(row, col + 1, new, old)

    def updateTile(self, row, col, new, old):
        self.rep[row][col] = new
        if row != 0:
            if self.rep[row - 1][col] == old:
                self.updateTile(row - 1, col, new, old)
        if row != self.height - 1:
            if self.rep[row + 1][col] == old:
                self.updateTile(row + 1, col, new, old)
        if col != 0:
            if self.rep[row][col - 1] == old:
                self.updateTile(row, col - 1, new, old)
        if col != self.width - 1:
            if self.rep[row][col + 1] == old:
                self.updateTile(row, col + 1, new, old)

    def generateRandomBoard(self):
        self.rep = [[0 for x in range(self.width)] for y in range(self.height)] 
        for column in range(self.width):
            for row in range(self.height):
                self.rep[row][column] = random.randint(0, self.numOfValues - 1)

    def prettyPrint(self):
        s = ""
        for row in range(self.height):
            for column in range(self.width):
                s += str(self.rep[row][column]) + " "
            s += "\n"
        print(s)
