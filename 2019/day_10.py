INFINITE = 10**18

def monitor(space, position):
	x,y = position
	
	gradients = set()
	# compute the number of asteroids it can moniter
	number  = 0

	positions = []

	for i in range(len(space)):
		for j in range(len(space[i])):
			if space[i][j] == "#" and (i,j) != (x,y):
				if j-y != 0 and i-x != 0:
					gradient = (i-x)/(j-y)

					if i < x and j > y:
						quadrant = 1
					elif i > x and j > y:
						quadrant = 2
					elif i > x and j < y:
						quadrant = 3
					elif i < x and j < y:
						quadrant = 4
		
				else:
					# vertical or horizontal gradient
					if i-x == 0:
						gradient = 0

						if j < y:
							quadrant = 4
						else:
							quadrant = 2

					if j-y == 0:
						gradient = INFINITE
						if i < x:
							quadrant = 1
						else:
							quadrant = 3

				if (gradient,quadrant) not in gradients:
					number += 1
					pos = (i,j)
					gradients.add((gradient,quadrant))
					positions.append((gradient, pos, quadrant))

	return (number, positions)

space = []
maxNum = 0
bestPos = (0,0)

with open("day_10.txt") as f:
	data = f.readlines()
	for line in data:
		space.append(list(line.strip()))

# part 1:
for i in range(len(space)):
	for j in range(len(space[i])):
		if space[i][j] == "#":
			num, _  = monitor(space, (i,j))
			if num > maxNum:
				maxNum = num
				bestPos = (i,j)

print(maxNum)

# part 2:
destroyed = 0
_, gradient = monitor(space, bestPos)

first =  [(i[0],i[1]) for i in gradient if i[2] == 1]
second = [(i[0],i[1]) for i in gradient if i[2] == 2]
third =  [(i[0],i[1]) for i in gradient if i[2] == 3] 
forth =  [(i[0],i[1]) for i in gradient if i[2] == 4]

first.sort()
second.sort()
third.sort()
forth.sort()

spaceMap = first[::-1] + second + third[::-1] + forth

destroyed = 0

for pair in spaceMap:
	m, pos = pair
	x,y = pos
	space[x][y] = "."
	destroyed += 1

	if destroyed == 200:
		print(pos)
		break
