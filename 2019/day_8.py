with open("day_8.txt") as f:
	encoded = list(map(int,list(f.readline().strip())))

def image(encoded, w, h):
	image = []

	start = 0

	for k in range(int(len(encoded)/(w*h))):
		layer = []
		for i in range(h):
			row = []
		
			for j in range(w):
				row.append(encoded[start + j])
		
			start += w
			layer.append(row)

		image.append(layer)
	
	return image


### MAIN ###

# part 1
image = image(encoded, 25, 6)

minSoFar = 10**18
fewestLayer = 0

for layer in range(len(image)):
	numberZero = 0
	for i in image[layer]:
		numberZero += i.count(0)

	if numberZero < minSoFar:
		minSoFar = numberZero
		fewestLayer = layer

ans = 0
numberOne = 0
numberTwo = 0

for i in image[fewestLayer]:
	numberOne += i.count(1)
	numberTwo += i.count(2)

ans = numberOne * numberTwo
print(ans)

# part 2
layers = len(image)
w = 25
h = 6

for i in range(h):
	row = []
	for j in range(w):
		k = 0
		while image[k][i][j] == 2:
			k += 1
		
		if image[k][i][j] == 0:
			print(".", end="")
		else:
			print("#", end="")
	print()



