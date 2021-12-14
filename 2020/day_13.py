import math

with open("day_13.txt") as puzzleInput:
    departure = int(puzzleInput.readline().strip())
    busIDs = puzzleInput.readline().strip().split(",")
    buses = ['x' if x == 'x' else int(x) for x in busIDs]

currMin = 1e9
ID = 0

for bus in list(filter(lambda a: a != 'x', buses)):
    waitTime = math.ceil(departure/bus)*bus
    if waitTime < currMin:
        currMin = waitTime
        ID = bus

print(ID*(currMin-departure))

mods = {bus: -i % bus for i, bus in enumerate(buses) if bus != 'x'}
vals = list(reversed(sorted(mods)))
val = mods[vals[0]]
r = vals[0]
for b in vals[1:]:
    while val % b != mods[b]:
        val += r
    r *= b

print(val)

