inp = open("../../input/day1.txt", "r")


def main():
    total = 0
    left = []
    right = []
    for _ in inp:
        row = _.replace("\n","").split("   ")
        col1 = int(row[0])
        col2 = int(row[1])
        left.append(col1)
        right.append(col2)

    left.sort()
    right.sort()

    for _ in range(len(left)):
        total = total + (max(left[_], right[_]) - min(left[_], right[_]))

    print(total)


main()