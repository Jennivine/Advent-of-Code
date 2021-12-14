with open("day_8.txt") as puzzleInput:
    instructions = [line.strip() for line in puzzleInput.readlines()]


def part1(instructions):
    accumulator = 0
    counter = 0
    visited = [0 for i in range(len(instructions))]

    while True:
        if visited[counter]:
            return False, accumulator

        visited[counter] = 1
        code, offset = instructions[counter].split(" ")

        if code == 'nop':
            counter += 1
        elif code == 'acc':
            accumulator += int(offset)
            counter += 1
        else:
            counter += int(offset)

        if counter >= len(instructions):
            return True, accumulator

print(part1(instructions))

def part2(instructions):
    for index, line in enumerate(instructions):
        if 'acc' in line:
            continue
        if 'nop' in line:
            instructions[index] = line.replace('nop', 'jmp')
        else:
            instructions[index] = line.replace('jmp', 'nop')

        boolState, value = part1(instructions)
        if boolState:
            return value
        else:
            instructions[index] = line

print(part2(instructions))
