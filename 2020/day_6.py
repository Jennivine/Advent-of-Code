with open("day_6.txt") as puzzleInput:
    groupsA = []; groupsB = []
    lines = puzzleInput.readlines()
    localA = set(); localB = set(list(lines[0].strip()))
    
    for i in range(len(lines)):
        l = lines[i].strip()
        if l == '':
            groupsA.append(localA)
            groupsB.append(localB)
            localA = set(); localB = set(list(lines[i+1].strip()))
        else:
            localA = localA.union(set(list(l)))
            localB = localB.intersection(set(list(l)))

    groupsA.append(localA)
    groupsB.append(localB)

    ansA = sum([len(s) for s in groupsA])
    ansB = sum([len(s) for s in groupsB])

    print(ansB)
