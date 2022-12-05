OROCK = 'A'
OPAPER = 'B'
OSCIS = 'C'
ROCK = 'X'
PAPER = 'Y'
SCIS = 'Z'

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

lines = map(str.split, lines)
print('answer:', sum(map(play_round, lines)))
