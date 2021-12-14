from collections import deque
import statistics

with open("day_10.txt") as puzzleInput:
    syntax = [list(line.strip()) for line in puzzleInput.readlines()]

syntax_score = {
    ')': 3,
    ']': 57, 
    '}': 1197, 
    '>': 25137
}

autocomplete_score = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

opening = {'(', '[', '{', '<'}
closing = {')', ']', '}', '>'}

def matching(a, b):
    if a == '(':
        return b == ')'
    elif a == '[':
        return b == ']'
    elif a == '{':
        return b == '}'
    elif a == '<':
        return b == '>'
    else:
        return "error: a is not an opening character"

def partA():
    total = 0
    incomplete = []
    for line in syntax:
        stack = deque()
        illegal = False
        for character in line:
            if character in opening:
                stack.append(character)
            elif character in closing:
                top = stack.pop()
                if matching(top, character):
                    pass
                else:
                    total += syntax_score[character]
                    illegal = True
                    break
            else:
                print("unrecognizable character")
        
        if not illegal:
            incomplete.append((line, stack))
    
    print(total)
    return incomplete

def partB():
    scores = []
    incomplete = partA()
    for line, stack in incomplete:
        total = 0
        while len(stack) > 0:
            top = stack.pop()
            total *= 5
            total += autocomplete_score[top]
        scores.append(total)

    return statistics.median(scores)

print(partB())
