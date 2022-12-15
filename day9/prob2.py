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

knots = [(0,0) for i in range(10)]
visits = []

def tail_touching(leaderi, followeri):
    leader = knots[leaderi]
    follower = knots[followeri]
    if leader[0] == follower[0] and leader[1] == follower[1]:
        # same pos, touching
        return True
    if leader[0] == follower[0]:
        # same col, check if row of head is +/- 1 of tail
        if leader[1] == follower[1]+1 or leader[1] == follower[1]-1:
            return True
    if leader[1] == follower[1]:
        # same row, check if col of head is +/- 1 of tail
        if leader[0] == follower[0]+1 or leader[0] == follower[0]-1:
            return True
    # not same row or column, could be diagonal
    if leader[0] == follower[0]-1:
        if leader[1] == follower[1]-1 or leader[1] == follower[1]+1:
            return True
    if leader[0] == follower[0]+1:
        if leader[1] == follower[1]-1 or leader[1] == follower[1]+1:
            return True

    # not touching
    return False

def adjust_tail(leaderi, followeri):
    leader = knots[leaderi]
    follower = knots[followeri]
    if leader[0] == follower[0]:
        # same x, adjust y of tail to keep up
        if leader[1] > follower[1]:
            follower = (follower[0], follower[1]+1)
        else:
            follower = (follower[0], follower[1]-1)

    elif leader[1] == follower[1]:
        # same y, adjust x of tail to keep up
        if leader[0] > follower[0]:
            follower = (follower[0]+1, follower[1])
        else:
            follower = (follower[0]-1, follower[1])

    else:
        # diff x and diff y, need to figure out the diagonal move of the tail
        if leader[0] > follower[0] and leader[1] > follower[1]:
            follower = (follower[0]+1, follower[1]+1)
        elif leader[0] > follower[0] and leader[1] < follower[1]:
            follower = (follower[0]+1, follower[1]-1)
        elif leader[0] < follower[0] and leader[1] > follower[1]:
            follower = (follower[0]-1, follower[1]+1)
        elif leader[0] < follower[0] and leader[1] < follower[1]:
            follower = (follower[0]-1, follower[1]-1)

    # update the follower now
    knots[followeri] = follower

def inc_move(x_move, y_move):
    # move head, check if tail should move 
    head_pos = (head_pos[0]+x_move, head_pos[1]+y_move)
    if not tail_touching():
        # move tail
        adjust_tail()

def update_tail(leaderi, followeri):
    if not tail_touching(leaderi, followeri):
        adjust_tail(leaderi, followeri)

def head_move(x_move, y_move):
    knots[0] = (knots[0][0]+x_move, knots[0][1]+y_move)

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
        head_move(x_move, y_move)
        # adjust the tails with leader/follower relationship
        for i in range(len(knots)-1):
            update_tail(i, i+1)
        # update where 9 is going
        visits.append(knots[9])

for line in lines:
    l = line.split(' ')
    direction = l[0]
    amt = int(l[1])
    move(direction, amt)

print('answer:',len(set(visits)))
