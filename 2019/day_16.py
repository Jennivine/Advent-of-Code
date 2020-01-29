def nextPhase(digits):
	basePattern = [0, 1, 0, -1]
	newPhase = []

	repeats = 1
	
	for i in range(len(digits)):
		patternCounter = 0
		tempSum = 0
		counter = 0
		offset = 1
		for x in digits:
			if offset:
				if counter == repeats-1:
					patternCounter = (patternCounter + 1) % 4
					counter = 0
					offset = 0

			if counter == repeats:
				patternCounter = (patternCounter + 1) % 4
				counter = 0

			tempSum += x * basePattern[patternCounter]
			counter += 1
			# print(x, end= " * ")
			# print(basePattern[patternCounter])
		
		repeats += 1
		newPhase.append(abs(tempSum)%10)
		# print(abs(tempSum)%10)
		# print()
	
	return newPhase

# yeet so brute force is not gonna work for part 2
# better think of a better solution :))

n = 59796737047664322543488505082147966997246465580805791578417462788780740484409625674676660947541571448910007002821454068945653911486140823168233915285229075374000888029977800341663586046622003620770361738270014246730936046471831804308263177331723460787712423587453725840042234550299991238029307205348958992794024402253747340630378944672300874691478631846617861255015770298699407254311889484508545861264449878984624330324228278057377313029802505376260196904213746281830214352337622013473019245081834854781277565706545720492282616488950731291974328672252657631353765496979142830459889682475397686651923318015627694176893643969864689257620026916615305397

digits = [int(x) for x in list(str(n))]
offset = int(str(n)[:7])

realInput = digits*10000

for i in range(100):
	realInput = nextPhase(realInput)

print(digits[offset:offset+8])
