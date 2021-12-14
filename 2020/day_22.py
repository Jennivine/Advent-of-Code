from collections import deque

with open("day_22.txt") as puzzleInput:
    line = puzzleInput.readline().strip()
    
    player1 = deque()
    player2 = deque()

    while line != "":
        if line.isnumeric():
            player1.append(int(line))
        line = puzzleInput.readline().strip()

    line = puzzleInput.readline().strip()
    while line != "":
        if line.isnumeric():
            player2.append(int(line))
        line = puzzleInput.readline().strip()

def combat(p1, p2):
    while len(p1) != 0 and len(p2) != 0:
        a = p1.popleft()
        b = p2.popleft()

        if a > b:
            p1.append(a)
            p1.append(b)
        else:
            p2.append(b)
            p2.append(a)

    winningDeck = p1 if len(p1) != 0 else p2
    return winningDeck

winner = combat(player1, player2)
ans = sum([(len(winner)-i)*v for i,v in enumerate(list(winner))]) 
print(f"part 1: %d" % ans)

def deck2string(deck):
    return "".join("{:02d}".format(v) for v in deck)

def recursiveCombat(player1, player2, return_deck=False):
    prevRounds = set()
    while True:
        thisConfig = (deck2string(player1), deck2string(player2))
        if thisConfig in prevRounds:
            if return_deck:
                return "p1", player1
            else:
                return "p1"

        prevRounds.add(thisConfig)

        a,b = player1.pop(0), player2.pop(0)

        if len(player1) >= a and len(player2) >= b:
            round_winner = recursiveCombat(player1[:a], player2[:b])
        else:
            round_winner = "p1" if a > b else "p2"

        if round_winner == "p1":
            player1.append(a)
            player1.append(b)
        else:
            player2.append(b)
            player2.append(a)

        if len(player1) != 0 and len(player2) != 0:
            continue
        
        return_value = "p1" if len(player2) == 0 else "p2"
        if return_deck:
            return_value = (return_value, player1 if return_value == "p1" else player2)
        return return_value

_, winner2 = recursiveCombat(list(player1), list(player2), True)
ans = sum([(len(winner2)-i)*v for i,v in enumerate(list(winner2))]) 
print(f"part 2: %d" % ans)

