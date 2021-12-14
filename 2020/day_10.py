with open("day_10.txt") as puzzleInput:
    adapters = [int(line.strip()) for line in puzzleInput.readlines()]
    adapters.sort()

deviceJoltage = adapters[-1]+3
joltageCount = [0,0,0,0]
chain = [0] + adapters + [deviceJoltage]

i = 1
while i < len(chain):
    difference = chain[i] - chain[i-1]

    if difference > 3:
        print("impossible chain")
        break
    else:
        joltageCount[difference] += 1
    i += 1

print(joltageCount[1]*joltageCount[3])

count = {0:1}
for jolt in chain[1:]:
    possible = 0
    
    if jolt-1 in count:
        possible += count[jolt-1]
    if jolt-2 in count:
        possible += count[jolt-2]
    if jolt-3 in count:
        possible += count[jolt-3]

    count[jolt] = possible

print(count[deviceJoltage])
