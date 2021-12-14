from collections import Counter

with open('day_5.txt') as f:
    segments = [line.strip().replace(' -> ', ',') for line in f.readlines()]

def AOC_day5(segments, include_diagonal):
    straight, diagonal = [], []
    for line in segments:
        x1, y1, x2, y2 = map(int, line.split(','))
        (x1, y1), (x2, y2) = sorted([(x1, y1), (x2, y2)])
        if x1 == x2 or y1 == y2:
            straight += [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]
        elif y1 < y2:
            diagonal += [(x, y1 + idx) for idx, x in enumerate(range(x1, x2 + 1))]
        else:
            diagonal += [(x, y1 - idx) for idx, x in enumerate(range(x1, x2 + 1))]
    position_counts = Counter(straight)
    if include_diagonal:
        position_counts += Counter(diagonal)
    return sum(v > 1 for v in position_counts.values())

print(AOC_day5(segments, include_diagonal=False))
print(AOC_day5(segments, include_diagonal=True ))
