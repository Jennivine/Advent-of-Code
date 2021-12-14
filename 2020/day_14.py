with open("day_14.txt") as puzzleInput:
    lines = [line.strip() for line in puzzleInput.readlines()]

mask = ""
mem = dict()

def getRealValue(value, mask):
    binary = bin(int(value))[2:][::-1]
    padded = binary + '0'*(36-len(binary))
    mask = mask[::-1]
    real = ""
    for i in range(36):
        if mask[i] == 'X':
            real += padded[i]
        else:
            real += mask[i]
    return int(real[::-1],2)

def getPossibleAddress(address, mask):
    binary = bin(int(address))[2:][::-1]
    padded = binary + '0'*(36-len(binary))
    mask = mask[::-1]
    real = ""; values = []
    for i in range(36):
        if mask[i] == '0':
            real += padded[i]
        else:
            real += mask[i]
    
    real = real[::-1]
    numPoss = real.count('X')
    flucts = []
    for i in range(2**numPoss):
        flucts.append(bin(i)[2:].zfill(numPoss))

    for fluct in flucts:
        i = 0
        add = ''
        for bit in real:
            if bit == 'X':
                add += fluct[i]
                i += 1
            else:
                add += bit
        values.append(str(int(add, 2)))

    return values

def part1():
    for i in lines:
        instruction, eq, value = i.split(" ")
        if instruction == 'mask':
            mask = value
        else:
            v = getRealValue(value, mask)
            address = instruction[4:-1]
            mem[address] = v

    print(sum(mem.values()))

def part2():
    for i in lines:
        instruction, eq, value = i.split(" ")
        if instruction == 'mask':
            mask = value
        else:
            addresses = getPossibleAddress(instruction[4:-1], mask)
            for address in addresses:
                mem[address] = int(value)


    print(sum(mem.values()))


part2()

