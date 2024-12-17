import numpy as np

inp = open("../../input/day2.txt", "r")

def rec(row, index, val, count):
    if np.size(row) - 1 == index:
        if np.size(row) - 1 == count:
            return val + 1
        else:
            return val
    
    if row[index] - row[index + 1] == 0:
        return val
    if row[index] - row[index + 1] <= 3:
        return rec(row, index + 1, val, count + 1)
    else:
        return rec(row, index + 1, val, count)


def partOne():
    safeCount = 0
    for _ in inp:
        rowR = _.strip().split(" ")
        rowS = np.array([])
        for val in rowR:
            rowS = np.append(rowS,int(val))
        a = np.sort(rowS)
        b = np.flip(a)
        if (a.all() == rowS.all() or b.all() == rowS.all()):
            safeCount = rec(b, 0, safeCount, 0)
    return safeCount

print(partOne())