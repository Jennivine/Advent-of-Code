with open("day_12.txt") as puzzleInput:
    instructions = [line.strip() for line in puzzleInput.readlines()]

currDirection = 1
compass = ['N', 'E', 'S', 'W'] 
location = [0,0] # [East, North]
waypoint = [10,1]

def part1():
    global instructions
    for line in instructions:
        code, value = line[0],line[1:]

        if code == 'F':
            code = compass[currDirection]

        if code == 'N':
            location[1] += int(value)
        elif code == 'S':
            location[1] -= int(value)
        elif code == 'E':
            location[0] += int(value)
        elif code == 'W':
            location[0] -= int(value)
        else:
            turns = int(value)//90
            if code == 'L':
                currDirection = (currDirection-turns) % 4
            else:
                currDirection = (currDirection+turns) % 4
        
    print(abs(location[0]) + abs(location[1]))


def part2():
    global instructions
    for line in instructions:
        code, value = line[0], line[1:]
    
        if code == 'N':
            waypoint[1] += int(value)
        elif code == 'S':
            waypoint[1] -= int(value)
        elif code == 'E':
            waypoint[0] += int(value)
        elif code == 'W':
            waypoint[0] -= int(value)
        elif code == 'F':
            location[0] += waypoint[0]*int(value)
            location[1] += waypoint[1]*int(value)
        else:
            turns = (int(value)//90) % 4
            if code == 'L':
                turns = 4-turns
            for i in range(turns):
                temp = waypoint[0]
                waypoint[0] = waypoint[1]
                waypoint[1] = (-1)*temp

    print(abs(location[0]) + abs(location[1]))

part2()
