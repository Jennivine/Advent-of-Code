with open("day_7.txt") as puzzleInput:
    positions = list(map(int, puzzleInput.readline().strip().split(',')))
    start, end = min(positions), max(positions)+1

def getCost(a, b):
    n = abs(a-b)
    return (n*(n+1))//2

def partA(positions, start, end):
    costs = []
    for pos in range(start, end):
        costs.append(sum(abs(pos-i) for i in positions))

    return min(costs)

print(partA(positions, start, end))

def partB(positions, start, end):
    costs = []
    for pos in range(start, end):
        costs.append(sum(getCost(i, pos) for i in positions))

    return min(costs)

print(partB(positions, start, end))
    

