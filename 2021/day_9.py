import numpy as np
from collections import Counter
from skimage import measure

with open('day_9.txt', 'r') as puzzleInput:
    list2d = [list(map(int, list(line.strip()))) for line in puzzleInput.readlines()]

array2d = np.array(list2d)
max_y, max_x = np.shape(array2d)

def partA():
    total = 0
    for y in range(max_y):
        for x in range(max_x):
            debug_value = array2d[y][x]
            count = 0
            if x != 0:
                if array2d[y][x] < array2d[y][x-1]:
                    count += 1
            else:
                count += 1
            if x != max_x-1:
                if array2d[y][x] < array2d[y][x+1]:
                    count += 1
            else:
                count += 1
            if y != 0:
                if array2d[y][x] < array2d[y-1][x]:
                    count += 1
            else:
                count += 1
            if y != max_y-1:
                if array2d[y][x] < array2d[y+1][x]:
                    count += 1
            else:
                count += 1
            if count == 4:
                # arr_mask[y][x] = array2d[y][x]
                total += array2d[y][x] + 1

    print(total)

partA()

def partB():
    basin = (array2d != 9).astype(int)
    d = measure.label(basin, connectivity=1)
    count = Counter()
    for x in range(np.max(d))[1:]:
        count[x] = np.count_nonzero(d == x)
    basins = count.most_common(3)
    result = 1
    for x in basins:
        result = result * x[1]
    print(result)

partB()
