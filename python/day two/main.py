import numpy as np
import math as mt

inp = open("../../input/day22.txt", "r")

def CheckDifference(bigger, smaller):
    dif = bigger - smaller
    return  dif > 0 and dif <= 3

def partOne():
    safeCount = 0
    for _ in inp:
        dampener = 0
        rowR = _.strip().split(" ")
        rowS = np.array([])
        for val in rowR:
            rowS = np.append(rowS,int(val))
        isIncreasing = True
        isValid = True
        if rowS[0] > rowS[np.size(rowS) - 1]:
            isIncreasing = False
        numOfRows = np.size(rowS)
        for it in range( numOfRows - 1):
            curr = rowS[it]
            next = rowS[it + 1]
            if isIncreasing:
                curr = rowS[(numOfRows - 1) - it]
                next = rowS[(numOfRows - 2) - it]
                if not CheckDifference(curr, next):
                    if dampener > 0 :
                        isValid = False
                        break
                    else:
                        dampener = dampener + 1
        if isValid:
            print(rowS)
            safeCount = safeCount + 1
    return safeCount

def breakP(value):
    print(value)
    # input()

def partTwo():
    safeCount = 0
    items = 0
    for _ in inp:
        dampener = 0
        rowR = _.strip().split(" ")
        rowS = np.array([])
        items = items + 1
        for val in rowR:
            rowS = np.append(rowS,int(val))
        isIncreasing = True
        isValid = True
        numOfRows = np.size(rowS)
        if rowS[0] > rowS[numOfRows- 1] or (rowS[0] >= rowS[numOfRows- 1] and rowS[numOfRows - 1] < rowS[mt.floor(numOfRows / 2)]):
            # print("dec ",rowS)
            isIncreasing = False
        for va in range(numOfRows - 1):
            if dampener > 2:
                isValid = False
                continue
            curr = rowS[va]
            next = rowS[va + 1]
            if isIncreasing:
                curr = rowS[numOfRows - 1 - va]
                next = rowS[numOfRows - 2 - va]
            if not CheckDifference(curr, next):
                dampener = dampener + 1
                val = va + 2
                if val != np.size(rowS):
                    next = rowS[val]
                if isIncreasing:
                    next = rowS[numOfRows - 3 - va]
                if (not CheckDifference(curr, next)) and dampener <= 1:
                    dampener = dampener + 1

        breakP((isValid,dampener,rowS))
        if isValid:
            safeCount = safeCount + 1
    return safeCount, items 
print(partTwo())

# if unsafe detected, dampener--
# if dampener is zero and is unsafe