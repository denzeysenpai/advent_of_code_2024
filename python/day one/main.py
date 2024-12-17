inp = open("../../input/day1.txt", "r")


def splitData():
    left = []
    right = []
    for _ in inp:
        row = _.replace("\n","").split("   ")
        col1 = int(row[0])
        col2 = int(row[1])
        left.append(col1)
        right.append(col2)

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