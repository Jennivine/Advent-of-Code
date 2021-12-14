with open("day_5.txt") as puzzleInput:
    N = [line.strip() for line in puzzleInput]

exists = [0 for i in range(966)]

def getSeatID(string):
    # getting row number
    hiR = 127
    loR = 0
    for i in range(7):
        if string[i] == "F":
            hiR = (loR+hiR) // 2
        elif string[i] == "B":
            loR = ((loR+hiR)//2) + 1
    row = hiR
    
    hiC = 7
    loC = 0
    for i in range(7,10):
        if string[i] == "L":
            hiC = (loC + hiC) // 2
        elif string[i] == "R":
            loC = ((loC+hiC)//2) + 1
    col = loC

    return (row*8 + col)

ansA = 0
for string in N:
    id = getSeatID(string)
    exists[id] = 1
    ansA = max(ansA,id)

for i in range(1, 965):
    if exists[i-1] and exists[i+1] and not exists[i]:
        print(i)
        break
