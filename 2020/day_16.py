with open("day_16.txt") as puzzleInput:
    rawInput = [line.strip() for line in puzzleInput.readlines()]
    ticketRules = {}
    nearbyTickets = []

    counter = 0
    while rawInput[counter] != "":
        field, r = rawInput[counter].split(": ")
        r1, r2 = r.split(" or ")
        l1, u1 = map(int, r1.split("-"))
        l2, u2 = map(int, r2.split("-"))
        
        values = set(range(l1, u1+1)).union(set(range(l2,u2+1)))
        ticketRules[field] = values
        counter += 1

    counter += 2
    myTicket = list(map(int, rawInput[counter].split(",")))

    counter += 3
    while counter < len(rawInput):
        ticket = list(map(int, rawInput[counter].split(",")))
        nearbyTickets.append(ticket)
        counter += 1

# part 1
validTickets = []
errorRate = 0
for ticket in nearbyTickets:
    invalid = False
    for val in ticket:
        if not any(val in s for s in ticketRules.values()):
            errorRate += val
            invalid = True
    if not invalid:
        validTickets.append(ticket)

print(f'part 1 answer: %d' %errorRate)

# part 2
possibleFields = [set() for _ in myTicket]
for ticket in validTickets:
    for ix, num in enumerate(ticket):
        fields = set()

        for f, val in ticketRules.items():
            if num in val:
                fields.add(f)

        if fields:
            possibleFields[ix] = possibleFields[ix].intersection(fields) if possibleFields[ix] else fields

sortedPossFields = [[len(fields), ix, fields] for ix, fields in enumerate(possibleFields)]
sortedPossFields.sort()

visited = set()
ans = 1
for ix, data in enumerate(sortedPossFields):
    length, index, fields = data
    
    # fields[ix-1] is always a strict subset of fields[ix], 
    # and is always off-by-one

    field_name = list(fields - visited)[0]
    if 'departure' in field_name:
        ans *= myTicket[index]
    visited.add(field_name)

print(f'part 2 answer: %d' %ans)
