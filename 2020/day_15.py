from collections import *

with open("day_15.txt") as puzzleInput:
    startingNums = [int(n) for n in puzzleInput.readline().strip().split(",")]

def day_15(turns):
    lastNum = startingNums[-1]
    turnNum = defaultdict(deque)

    for v, k in enumerate(startingNums):
        turnNum[k].append(v+1)

    turn = len(startingNums) + 1
    while turn <= turns:
        l = len(turnNum[lastNum])
        if l>1:
            nextSpoken = turnNum[lastNum][-1] - turnNum[lastNum][-2]
            turnNum[nextSpoken].append(turn)
        else:
            nextSpoken = 0
            turnNum[nextSpoken].append(turn)
        turn += 1
        lastNum = nextSpoken

    print(lastNum)

day_15(2020)
day_15(30000000)
