inp = open("../../input/day1.txt", "r")


def splitData():
    left = []
    right = []
    for _ in inp:
        row = _.replace("\n","").split("   ")
        left.append(int(row[0]))
        right.append(int(row[1]))
    return [left, right]

def partOne():
    total = 0
    data = splitData()
    left = data[0]
    right = data[1]
    left.sort()
    right.sort()
    for _ in range(len(left)):
        total = total + (max(left[_], right[_]) - min(left[_], right[_]))
    return total

def partTwo():
    total = 0
    data = splitData()
    left = data[0]
    right = data[1]
    for _ in range(len(left)):
        val = left[_]
        total = total + ( val * right.count(val))
    return total

print(partTwo())