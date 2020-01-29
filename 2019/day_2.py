
def testInput(a,b):

	program = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,1,13,23,27,1,6,27,31,1,31,10,35,1,35,6,39,1,39,13,43,2,10,43,47,1,47,6,51,2,6,51,55,1,5,55,59,2,13,59,63,2,63,9,67,1,5,67,71,2,13,71,75,1,75,5,79,1,10,79,83,2,6,83,87,2,13,87,91,1,9,91,95,1,9,95,99,2,99,9,103,1,5,103,107,2,9,107,111,1,5,111,115,1,115,2,119,1,9,119,0,99,2,0,14,0]
	
	# part 1: a = 12, b = 2
	program[1] = a
	program[2] = b

	for i in range(len(program)//4):
		if program[i*4] == 1:
			# add and overwrite
			program[program[i*4+3]] = program[program[i*4+1]] + program[program[i*4+2]]
		
		elif program[i*4] == 2:
			# multiply and overwrite
			program[program[i*4+3]] = program[program[i*4+1]] * program[program[i*4+2]]

		else:
			break

	return program[0]


# main
for i in range(100):
	for j in range(100):
		if testInput(i,j) == 19690720:
			print(100*i + j)
