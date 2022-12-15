import sys
if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = 'test.txt'
with open(fname,'r') as fi:
    lines = list(map(str.strip, fi.readlines()))

# keep track of head and tail starting at (0,0) --> (x,y)
# R: +x, L: -x, U: +y, D: -y
# keep a list of visited points for the tail and take its set at the end for #
# of unique spots
# for each move, conduct the move incrementally. move the head first, then check
# if the tail needs to move
# diagonal would be +/-x and +/-y

head_pos = (0,0)
tail_pos = (0,0)
visits = []

def tail_touching():
    global head_pos, tail_pos
    if head_pos[0] == tail_pos[0] and head_pos[1] == tail_pos[1]:
        # same pos, touching
        return True
    if head_pos[0] == tail_pos[0]:
        # same col, check if row of head is +/- 1 of tail
        if head_pos[1] == tail_pos[1]+1 or head_pos[1] == tail_pos[1]-1:
            return True
    if head_pos[1] == tail_pos[1]:
        # same row, check if col of head is +/- 1 of tail
        if head_pos[0] == tail_pos[0]+1 or head_pos[0] == tail_pos[0]-1:
            return True
    # not same row or column, could be diagonal
    if head_pos[0] == tail_pos[0]-1:
        if head_pos[1] == tail_pos[1]-1 or head_pos[1] == tail_pos[1]+1:
            return True
    if head_pos[0] == tail_pos[0]+1:
        if head_pos[1] == tail_pos[1]-1 or head_pos[1] == tail_pos[1]+1:
            return True

    # not touching
    return False

def adjust_tail():
    global head_pos, tail_pos
    if head_pos[0] == tail_pos[0]:
        # same x, adjust y of tail to keep up
        if head_pos[1] > tail_pos[1]:
            tail_pos = (tail_pos[0], tail_pos[1]+1)
        else:
            tail_pos = (tail_pos[0], tail_pos[1]-1)

    elif head_pos[1] == tail_pos[1]:
        # same y, adjust x of tail to keep up
        if head_pos[0] > tail_pos[0]:
            tail_pos = (tail_pos[0]+1, tail_pos[1])
        else:
            tail_pos = (tail_pos[0]-1, tail_pos[1])

    else:
        # diff x and diff y, need to figure out the diagonal move of the tail
        if head_pos[0] > tail_pos[0] and head_pos[1] > tail_pos[1]:
            tail_pos = (tail_pos[0]+1, tail_pos[1]+1)
        elif head_pos[0] > tail_pos[0] and head_pos[1] < tail_pos[1]:
            tail_pos = (tail_pos[0]+1, tail_pos[1]-1)
        elif head_pos[0] < tail_pos[0] and head_pos[1] > tail_pos[1]:
            tail_pos = (tail_pos[0]-1, tail_pos[1]+1)
        elif head_pos[0] < tail_pos[0] and head_pos[1] < tail_pos[1]:
            tail_pos = (tail_pos[0]-1, tail_pos[1]-1)

def inc_move(x_move, y_move):
    # move head, check if tail should move 
    global head_pos
    head_pos = (head_pos[0]+x_move, head_pos[1]+y_move)
    if not tail_touching():
        # move tail
        adjust_tail()

def move(direction, amt):
    x_move = 0 
    y_move = 0 
    if direction == 'R':
        x_move = 1
    elif direction == 'L':
        x_move = -1
    elif direction == 'U':
        y_move = 1 
    else:
        y_move = -1

    for i in range(amt):
        inc_move(x_move, y_move)
        visits.append(tail_pos)

for line in lines:
    l = line.split(' ')
    direction = l[0]
    amt = int(l[1])
    move(direction, amt)

print('answer:',len(set(visits)))
