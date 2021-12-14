from collections import deque 

with open("day_6.txt") as puzzleInput:
    fish = list(map(int, puzzleInput.readline().strip().split(',')))

def modelGrowth(data, iterations):
    totals = deque(data.count(i) for i in range(9))
    for _ in range(iterations):
        totals.rotate(-1)
        totals[6] += totals[8]
    return sum(totals)

print(modelGrowth(fish, 80))
print(modelGrowth(fish, 256))
