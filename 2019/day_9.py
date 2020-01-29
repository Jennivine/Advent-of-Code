import Intcode

with open("day_9.txt") as f:
    code = list(map(int, f.readline().strip().split(",")))

    print("Part 1:", Intcode.VM(code, 1).run())
    print("Part 2:", Intcode.VM(code, 2).run())
