from collections import deque as dq
from math import ceil, floor

with open("day_14.txt") as f:
	book = f.readlines()

	adjList = dict()
	netAmountNeeded = dict()

	for reaction in book:
		reactants, product = reaction.strip().split(" => ")
		
		quantity, productName = product.split(" ")
		reactantList = reactants.split(", ")

		adjList[productName] = tuple([quantity]) + tuple(reactantList)
		netAmountNeeded[productName] = 0

def getQuantity(product):
	toReturn = []

	quantity = netAmountNeeded[product]

	reaction = list(adjList[product])

	reactionQuantity = int(reaction[0])
	reactantsNeeded = reaction[1:]

	timesFactor = ceil(quantity/reactionQuantity)
	toReturn.append(reactionQuantity * timesFactor)

	for reactant in reactantsNeeded:
		quantity, name = reactant.split(" ")
		quantity = int(quantity) * timesFactor
		package = tuple([quantity, name])
		toReturn.append(package)

	return toReturn

def oreNeeded(fuel):
	oreCount = 0
	queue = dq()
	queue.append("FUEL")
	netAmountNeeded["FUEL"] = fuel

	while len(queue):
		product = queue.popleft()
		reactants = getQuantity(product)
		total = reactants[0]
		netAmountNeeded[product] -= total 
	
		for reactant in reactants[1:]:
			quantity, name = reactant
			if name == "ORE":
				oreCount += int(quantity)
			else:
				if netAmountNeeded[name] <= 0:
					queue.append(name)
				netAmountNeeded[name] += int(quantity)

	# clean-up the netAmountNeeded cache
	for key in netAmountNeeded:
		netAmountNeeded[key] = 0

	return oreCount


# part 1
fuelPerOre = oreNeeded(1)
print(fuelPerOre)

# part 2
totalOre = 1000000000000
fuelMin = floor(totalOre / 13312)
fuelMax = fuelMin * 2

while fuelMin+1 != fuelMax:
	middle = (fuelMin + fuelMax) // 2

	oreAmount = oreNeeded(fuel=middle)
	if oreAmount > totalOre:
		fuelMax = middle
	else:
		fuelMin = middle

print(fuelMin)

