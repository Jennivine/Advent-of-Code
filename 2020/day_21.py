with open("day_21.txt") as puzzleInput:
    input = puzzleInput.read().splitlines()

alrgs = {}
ingrs = []

for e in input:
    a,b = e.rstrip(")").split("(contains ")
    ingr = a.split()
    ingrs.append(ingr)
    for alrg in b.split(", "):
        if alrg not in alrgs:
            alrgs[alrg] = set(ingr)
        else:
            alrgs[alrg] &= set(ingr)

all_alrgs = set(e for a in alrgs.values() for e in a)
print( sum(i not in all_alrgs for ingr in ingrs for i in ingr))

def remove(a, alrgs):
    singletons = set()
    for k in alrgs:
        if len(alrgs[k]) > 1 and a in alrgs[k]:
            alrgs[k].remove(a)
            if len(alrgs[k]) == 1:
                singletons |= alrgs[k]
    return singletons

r = next(list(v) for v in alrgs.values() if len(v) == 1)
while r:
    r += list(remove(r.pop(), alrgs))

print(','.join(str(i.pop()) for a,i in sorted((k,v) for k,v in alrgs.items())))
