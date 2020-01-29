# range: 273025-767253

def adjSame(n):
	number = list(str(n))

	for i in range(len(number)-1):
		if number[i] == number[i+1]:
			return True

def nonDec(n):
	number = list(str(n))
	number = [int(i) for i in number]

	for i in range(len(number)-1):
		if number[i+1] < number[i]:
			return False

	return True

def noRepeat(n):
	number = list(str(n))

	for i in range(len(number)-1):
		if number[i] == number[i+1] and number.count(number[i]) == 2:
			return True

total = 0
answer = 0

for i in range(273025,767254):
	# part 1	
	if adjSame(i) and nonDec(i):
		total += 1

	# part 2
	if noRepeat(i) and nonDec(i):
		answer += 1

print(answer)
