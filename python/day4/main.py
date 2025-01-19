import numpy as np
import math as mt

inputData = open("../../input/day.txt", "r")

def findOnX(count, line):
    newCount : int = count
    filteredA : int = len(line.replace("XMAS", ""))
    filteredB : int = len(line.replace("SAMX", ""))
    newCount = newCount + mt.floor((len(line) - filteredB) / 4)
    newCount = newCount + mt.floor((len(line) - filteredA) / 4)
    return newCount

def getInput():
    matrix : str[""] = []
    currentCount : int = 0
    for line in inputData:
        row : str[""] = []
        currentCount = findOnX(currentCount, line)
        for char in line:
            if char != "\n":
                row.append(char)
        matrix.append(row)
    newMat = np.rot90(np.array(matrix, str),2)
    for line in newMat:
        row : str = ""
        for val in line:
            row = row + val
        currentCount = findOnX(currentCount, row)

    return matrix, currentCount

def partOne():
    def diagonalIsFound(a : str, b : str, c : str, d : str):
        s1 : str = a + b + c + d
        s2 : str = d + c + b + a
        return s1 == "XMAS" or s1 == "SAMX" or s2 == "XMAS" or s2 == "SAMX"
    
    data = getInput()
    count : int = data[1]
    grid : str[""] = data[0]

    # DIAGONAL SEARCHING
    xAxis : int = len(grid[0])
    yAxis : int = len(grid)

    limitX : int = xAxis - 4
    limitY : int = yAxis - 4
    shiftX : int = 0
    shiftY : int = 0
    forward : bool = True

    x1 : int = 0
    x2 : int = 1
    x3 : int = 2
    x4 : int = 3

    y1 : int = 0
    y2 : int = 1
    y3 : int = 2
    y4 : int = 3

    while True:
        if diagonalIsFound(grid[x1][y1], grid[x2][y2], grid[x3][y3], grid[x4][y4]):
            count = count + 1
            if forward:
                shiftX = shiftX + 1
                if shiftX > limitX:
                    shiftX = limitX
                    forward = False
            else:
                shiftX = shiftX - 1
                if shiftX < 0:
                    shiftX = 0
                    forward = True
        
    # print(count)
    # for 
    return

partOne()
