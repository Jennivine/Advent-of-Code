import numpy as np

with open("day_9.txt") as puzzleInput:
    lines = [int(line.strip()) for line in puzzleInput.readlines()]

def part1 (codes, preamble):
    start = 0; end = start + preamble
    curr_index = preamble

    while curr_index < len(codes)-1:
        stack = codes[start:end]
        valid = False

        for i in range(0,preamble):
            for j in range(i+1, preamble):
                if stack[i] + stack[j] == codes[curr_index]:
                    valid = True
                    break
            if valid:
                break

        if not valid:
            return codes[curr_index]
        
        curr_index += 1
        start += 1; end += 1

def part2 (codes, invalid_num):
    contiguousList = []

    for i in range(0,len(codes)):
        for j in range(i+1, len(codes)):
            stack = np.array(codes[i:j])
            if np.sum(stack) == invalid_num:
                return(stack.min()+stack.max())

print(part1(lines, 25))
print(part2(lines, part1(lines, 25)))
