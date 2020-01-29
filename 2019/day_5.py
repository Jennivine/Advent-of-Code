from Intcode import VM

with open("day_5.txt") as f:
	program = list(map(int, f.readline().strip().split(",")))

	print("Part 1:", VM(program, 1).run())
	print("Part 2:", VM(program, 5).run())

