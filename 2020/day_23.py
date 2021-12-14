puzzleInput = list("156794823")

def simulateGame(rounds, cups):
    currState = [*map(int, cups)]
    cp = 0
    wrap = len(cups)

    for _ in range(rounds):
        c1, c2, c3 = currState[(cp+1) % wrap], currState[(cp+2) % wrap], currState[(cp+3) % wrap]
        target = currState[cp] - 1
        currCup = currState[cp]

        currState.remove(c1)
        currState.remove(c2)
        currState.remove(c3)

        while target not in currState:
            target = target - 1 if target > 1 else 9

        targetIndex = currState.index(target)
        currState.insert(targetIndex+1, c3)
        currState.insert(targetIndex+1, c2)
        currState.insert(targetIndex+1, c1)
        cp = (currState.index(currCup) + 1) % wrap

    cups = currState[currState.index(1) + 1:] + currState[:currState.index(1)]
    print(''.join(map(str, cups)))

def getStar(rounds, cups):
    currState = [*map(int, cups)]
    clockwise = {}

    for i in range(1000000):
        if i < len(currState) - 1:
            clockwise[currState[i]] = currState[i+1]
        elif i == len(currState) - 1:
            clockwise[currState[i]] = max(currState) + 1
        else:
            clockwise[i+1] = i+2

    clockwise[1000000] = currState[0]

    cc = currState[0]

    for i in range(rounds):
        c1 = clockwise[cc]
        c2 = clockwise[c1]
        c3 = clockwise[c2]

        clockwise[cc] = clockwise[c3]
        target = 1000000 if cc == 1 else cc-1

        while target in [c1,c2,c3]:
            target = 1000000 if target == 1 else target-1

        clockwise[c3] = clockwise[target]
        clockwise[target] = c1
        cc = clockwise[cc]

    print(clockwise[1]*clockwise[clockwise[1]])

simulateGame(100, puzzleInput)
getStar(10000000, puzzleInput)
