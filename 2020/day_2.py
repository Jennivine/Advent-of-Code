with open("day_2.txt") as puzzle_input:
    N = [l.strip() for l in puzzle_input.readlines()]

part_a_ans = 0
part_b_ans = 0

for line in N:
    policy, password = line.split(": ")
    range, letter = policy.split(" ")
    lower, upper = map(int, range.split("-"))

    if password.count(letter) >= lower and password.count(letter) <= upper:
        part_a_ans += 1

for line in N:
    policy, password = line.split(": ")
    pos, letter = policy.split(" ")
    a, b = map(int, pos.split("-"))

    if (password[a-1] == letter) ^ (password[b-1] == letter):
        part_b_ans += 1

print(part_b_ans)
