#PART ONE
with open("day1in.txt") as I:
	frequencies = map(int, I.readlines())

reachedFreq = set()
ans = 0

for i in frequencies:
	ans += i

print ans


#PART TWO
ans = 0 #reset ans for second part :)
SIZE = len(frequencies)
i = 0

while not ans in reachedFreq:
	reachedFreq.add(ans)
	ans += frequencies[i]
	i = (i+1)%SIZE

print ans

'''
import itertools
for num in itertools.cycle(frequencies):
	ans += num
	if ans in reachedFreq:
		print ans
		break
	reachedFreq.add(ans)

'''
