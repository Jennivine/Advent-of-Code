with open("day_3.txt") as puzzleInput:
    forest = [line.strip() for line in puzzleInput.readlines()]
    length = len(forest[0])

ansA = 0

j = 0
for i in range(1, len(forest)):
    j = (j+3) % length
    if forest[i][j] == "#":
        ansA += 1

sample = ["..##.......",
          "#...#...#..",
          ".#....#..#.",
          "..#.#...#.#",
          ".#...##..#.",
          "..#.##.....",
          ".#.#.#....#",
          ".#........#",
          "#.##...#...",
          "#...##....#",
          ".#..#...#.#"]

def traverseMap(b,a):
    global forest, length
    j = 0
    ans = 0

    for i in range(a, len(forest), a):
        j = (j+b) % length
        if forest[i][j] == "#":
            ans += 1

    return ans

toCheck = [(1,1),(3,1),(5,1),(7,1),(1,2)]
ansB = 1

for (a,b) in toCheck:
    ansB *= traverseMap(a,b)

print(ansB)
