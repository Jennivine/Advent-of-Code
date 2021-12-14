def main():
    with open('day_4.txt') as f:
        lines = f.readlines()
        lines.append('\n')

    boards = []
    currentBoard = []
    for line in lines[2:]:
        if line == '\n':
            boards.append(currentBoard)
            currentBoard = []
        else:
            currentBoard.append(list(map(int, line.split())))

    chosenNumbers = list(map(int, lines[0].split(',')))
    wonBingos = set()
    firstWin = -1
    lastWin = 0
    for number in chosenNumbers:
        for boardIndex in range(len(boards)):
            if boardIndex in wonBingos:
                continue

            board = boards[boardIndex]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == number:
                        board[i][j] = -1

            if check_board(board):
                if firstWin < 0:
                    firstWin = score(board) * number
                else:
                    lastWin = score(board) * number
                wonBingos.add(boardIndex)

    print(firstWin)
    print(lastWin)

def score(board):
    answer = 0
    for row in board:
        for number in row:
            if number > 0:
                answer += number
    return answer

def check_board(board):
    boardT = tuple(zip(*board))
    SET_OF_NEGATIVE_ONE = set([-1])
    for i in range(len(board)):
        if set(board[i]) == SET_OF_NEGATIVE_ONE or set(boardT[i]) == SET_OF_NEGATIVE_ONE:
            return True
    return False

main()
