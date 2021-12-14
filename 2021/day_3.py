from collections import Counter

with open("day_3.txt") as puzzleInput:
    data = [list(line.strip()) for line in puzzleInput.readlines()]
    transposed = list(zip(*data))

def partA(data):
    gemma_rate = ""
    epsilon_rate = ""

    for line in data:
        info = Counter(line)
        gemma_rate += max(line, key = info.get)
        epsilon_rate += min(line, key = info.get)

    # PART A: CALCULATING THE POWER CONSUMPTION
    print(int(gemma_rate, 2) * int(epsilon_rate, 2))

def mostCommonFilter(data, index):
    transposed = list(zip(*data))[index]
    info = Counter(transposed)
    if info['1'] >= info['0']:
        mostCommon = '1'
    else:
        mostCommon = '0'

    oxygenFiltered = []
    for d in data:
        if d[index] == mostCommon:
            oxygenFiltered.append(d)
    
    return oxygenFiltered

def leastCommonFilter(data, index):
    transposed = list(zip(*data))[index]
    info = Counter(transposed)
    if info['1'] >= info['0']:
        leastCommon = '0'
    else:
        leastCommon = '1'

    CO2Filtered = []
    for d in data:
        if d[index] == leastCommon:
            CO2Filtered.append(d)

    return CO2Filtered


def oxygen_Rating(data):
    index = 0
    while len(data) > 1:
        data = mostCommonFilter(data, index)
        index += 1

    return data[0]

def CO2_Rating(data):
    index = 0
    while len(data) > 1:
        data = leastCommonFilter(data, index)
        index += 1

    return data[0]

def partB(data):
    oxygen = oxygen_Rating(data)
    CO2 = CO2_Rating(data)

    print(int(''.join(oxygen), 2) * int(''.join(CO2),2))

partB(data)
