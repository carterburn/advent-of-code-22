OROCK = 'A'
OPAPER = 'B'
OSCIS = 'C'
LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'
ROCK = LOSE
PAPER = DRAW
SCIS = WIN

fname = 'input.txt'
with open(fname, 'r') as fi:
    lines = fi.readlines()

def play_round(rnd):
    opponent = rnd[0]
    player = rnd[1]
    # score for selection
    score = ord(player) - ord('X') + 1

    # play the round
    if ord(opponent)-ord('A') == ord(player)-ord('X'):
        # draw
        return score + 3
    if opponent == OROCK:
        if player == SCIS:
            return score
        elif player == PAPER:
            return score + 6
    elif opponent == OPAPER:
        if player == ROCK:
            return score
        elif player == SCIS:
            return score + 6
    elif opponent == OSCIS:
        if player == PAPER:
            return score
        elif player == ROCK:
            return score + 6

def compute(rnd):
    opponent = rnd[0]
    choice = rnd[1]

    if choice == LOSE:
        # lose the round
        if opponent == OROCK:
            return play_round([opponent, SCIS])
        elif opponent == OPAPER:
            return play_round([opponent, ROCK])
        else:
            return play_round([opponent, PAPER])
    elif choice == DRAW:
        # choose the same thing as the opponent
        return play_round([opponent, chr((ord(opponent)-ord('A'))+ord('X'))])
    else:
        # win the round
        if opponent == OROCK:
            return play_round([opponent, PAPER])
        elif opponent == OPAPER:
            return play_round([opponent, SCIS])
        else:
            return play_round([opponent, ROCK])

lines = map(str.split, lines)
print('answer:', sum(map(compute, lines)))
