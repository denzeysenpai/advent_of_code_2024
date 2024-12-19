import re
import numpy as np


inp = open("../../input/day3.txt", "r")

def partOne():
    res = 0
    for line in inp:
        for y in re.findall(r"mul+\(+[0-9]+,[0-9]+\)", line):
            if y[0]+y[1]+y[2] == "mul" and len(y[3:]) <= 12:
                val = re.findall(r"[0-9]+,[0-9]+",re.findall(r"\([^)]*\)",y[3:])[0])
                if len(val) > 0:
                    cont = val[0] + ""
                    values = cont.split(",")
                    reslt = int(values[0]) * int(values[1])
                    res = res + reslt
    return res
# 173785482

def partTwo():
    res = 0
    lines = []
    for line in inp:
        l = line.split("do()")
        lines.append(l)
    dos = []
    for line in lines:
        for l in line:
            dos.append(l.split("don't()")[0])
            print(l)
            print(l.split("don't()"))
    for line in dos:
        for y in re.findall(r"mul+\(+[0-9]+,[0-9]+\)", line):
            if y[0]+y[1]+y[2] == "mul" and len(y[3:]) <= 12:
                val = re.findall(r"[0-9]+,[0-9]+",re.findall(r"\([^)]*\)",y[3:])[0])
                if len(val) > 0:
                    cont = val[0] + ""
                    values = cont.split(",")
                    reslt = int(values[0]) * int(values[1])
                    res = res + reslt
    return res
print(partTwo())