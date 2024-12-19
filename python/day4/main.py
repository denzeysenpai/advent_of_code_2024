import numpy as np
import math as mt

inputData = open("../../input/day.txt", "r")

def removeBfromA(a, b):
    return len(a.replace(b, ""))
def getInput():
    matrix = []
    y = 0
    numOfDiff = len("XMAS")
    for line in inputData:
        x = 0
        row = []
        filteredA = removeBfromA(line,"XMAS")
        countOfA = mt.floor((len(line) - filteredA) / numOfDiff)
        filteredB = removeBfromA(line,"SAMX")
        countOfB = mt.floor((len(line) - filteredB) / numOfDiff)
        print(countOfA + countOfB)
        for char in line:
            if char != "\n":
                row.append(char)
                x = x + 1
        y = y + 1
        matrix.append(row)
    return matrix

def partOne():
    data = getInput()

    
    return
partOne()
