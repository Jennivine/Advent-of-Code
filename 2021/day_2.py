with open("day_2.txt") as puzzleInput:
    rawData = [line.strip().split(" ") for line in puzzleInput.readlines()]
    instructions = []
    for data in rawData:
        instructions.append((data[0],int(data[1])))


def partA(instructions):
    horizontal = 0
    depth = 0

    for line in instructions: 
        if line[0] == "forward":
            horizontal += line[1]
        elif line[0] == "up":
            depth -= line[1]
        elif line[0] == "down":
            depth += line[1]
        else:
            print("error in input")

    return (horizontal * depth)

def partB(instructions):
    horizontal = 0
    depth = 0
    aim = 0

    for line in instructions:
        if line[0] == "down":
            aim += line[1]
        elif line[0] == "up":
            aim -= line[1]
        elif line[0] == "forward":
            horizontal += line[1]
            depth += aim*line[1]
        else:
            print("error in input")

    return (horizontal * depth)

print(partB(instructions))
