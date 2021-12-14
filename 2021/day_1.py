with open("day_1.txt") as puzzleInput:
    depth = [int(line.strip()) for line in puzzleInput.readlines()]

increase = 0
prev = depth[0]

for measurement in depth:
    if measurement > prev:
        increase += 1
    prev = measurement

print("part a: " + str(increase))

sumIncrease = 0
prevWindow = sum(depth[:3])
for i in range(1, len(depth)-3):
    currWindow = prevWindow + depth[i+3] - depth[i]
    if currWindow > prevWindow:
        sumIncrease += 1
    prevWindow = currWindow

print("part b: " + str(sumIncrease))
