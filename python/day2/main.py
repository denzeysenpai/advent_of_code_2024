import numpy as np
import math as mt

inp = open("../../input/day2.txt", "r")

def CheckDifference(bigger, smaller):
    dif = bigger - smaller
    return  dif > 0 and dif <= 3


def partOne():
    unsafe = []
    safeCount = 0
    for _ in inp:
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
                isValid = False
                unsafe.append(rowS)
                break
                   
        if isValid:
            safeCount = safeCount + 1
    return [unsafe, safeCount]

def breakP(value):
    print(value)
    # input()

def partTwo():
    items = 0
    unsafes = partOne()
    safeCount = len(unsafes[0])
    passed = np.array([])
    for row in unsafes[0]:
        ascendingCount = 0
        descendingCount = 0
        for _ in range(len(row)):
            dampener = 1
            newRow = np.delete(row, _)
            i = 0
            j = 1
            while True:
                curr = newRow[i]
                next = newRow[j]
                if ascendingCount > descendingCount:
                    curr = newRow[j]
                    next = newRow[i]
                if not CheckDifference(curr, next):
                    dampener = dampener - 1
                i = i + 1
                j = j + 1
                if j == len(newRow):
                    break
            if dampener >= 0:
                _ = len(row)
                print(newRow)
                safeCount = safeCount - 1
    return safeCount + unsafes[1]
print(partTwo())

# if unsafe detected, dampener--
# if dampener is zero and is unsafe