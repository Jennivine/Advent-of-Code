from collections import deque
# contruct orbit graph, and keep a set of all the objects

# a : b -> a orbits around b 
spaceTree = {}
visited = {}

q = deque()

planets = set()

with open("day_6.txt") as f:
	spaceMap = f.readlines()

	for orbit in spaceMap:
		b,a = orbit.strip().split(")")

		if a not in planets:
			spaceTree[a] = [b]
			planets.add(a)
		else:
			spaceTree[a].append(b)
			
		# part 2 requires bi-directional paths
		if b not in planets:
			spaceTree[b] = [a]
			planets.add(b)
		else:
			spaceTree[b].append(a)

		visited[a] = 0
		visited[b] = 0

def checkOrbit(planet):
	if planet == "COM":
		return 0
	
	return checkOrbit(spaceTree[planet][0]) + 1

def BFS(start, target):
	dist = {}
	
	q = deque()
	q.append(start)
	dist[start] = 0

	while len(q) != 0:
		current = q.popleft()

		if current == target:
			break
	
		for i in spaceTree[current]:
			if visited[i]:
				continue

			dist[i] = dist[current] + 1
			q.append(i)
			visited[i] = 1
	
	return dist[target]

### MAIN ###

# part 1: for each planet, follow the tree and count the number of steps to get to COM
checkSum = 0

for i in planets:
	checkSum += checkOrbit(i)

print(checkSum)

# part 2:
start = spaceTree["YOU"][0]
target = spaceTree["SAN"][0]

print(BFS(start, target))

