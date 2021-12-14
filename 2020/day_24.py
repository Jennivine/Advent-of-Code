import sys, collections
def parse(s):
    q, r = 0, 0
    while s.strip():
        if s[0] == 'w':      q, s = q-1, s[1:]
        elif s[0] == 'e':    q, s = q+1, s[1:]
        elif s[0:2] == 'se': r, s = r+1, s[2:]
        elif s[0:2] == 'nw': r, s = r-1, s[2:]
        elif s[0:2] == 'sw': q, r, s = q-1, r+1, s[2:]
        elif s[0:2] == 'ne': q, r, s = q+1, r-1, s[2:]
    return q, r
cnt = collections.Counter(map(parse, open("day_24.txt").read().splitlines()))
print(sum(v % 2 for v in cnt.values()))

bnd = max(max(abs(q),abs(r)) for q, r in cnt.keys())
nbs = [(0,-1), (0,1), (-1,0), (1,0), (-1,1), (1,-1)]
black, new = {k for k, v in cnt.items() if v % 2 == 1}, set()
for b in range(1, 101):
    for q in range(-b-bnd, bnd+b+1):
        for r in range(-b-bnd, bnd+b+1):
            cnt = sum((q+dq, r+dr) in black for dq, dr in nbs)
            if (q, r) in black and 1 <= cnt <= 2 or \
                    (q, r) not in black and cnt == 2:
                new.add((q, r))
    black, new = new, set()
print(len(black))
