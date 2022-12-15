import sys
if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = 'test.txt'
with open(fname,'r') as fi:
    lines = fi.readlines()

num_col = len(lines[0].strip())
num_row = len(lines)

# create data structure 
forest = []
for line in lines:
    r = []
    for tree in line.strip():
        r.append(int(tree))
    forest.append(r)

def vis_rt(row, col):
    # right edge trees get a score of 0
    if col == num_col-1:
        return 0
    tree = forest[row][col]
    s = 0
    for i in range(col+1, num_col):
        if forest[row][i] >= tree:
            return s + 1
        s += 1
    return s

def vis_lt(row, col):
    # left edge trees get a score of 0
    if col == 0:
        return 0
    tree = forest[row][col]
    s = 0
    for i in range(col-1, -1, -1):
        if forest[row][i] >= tree:
            return s + 1
        s += 1
    return s

def vis_up(row, col):
    # top edge tree; score 0
    if row == 0:
        return 0
    tree = forest[row][col]
    s = 0
    for i in range(row-1, -1, -1):
        if forest[i][col] >= tree:
            return s + 1
        s += 1
    return s

def vis_down(row, col):
    # bottom edge tree; score 0
    if row == num_row-1:
        return 0
    tree = forest[row][col]
    s = 0
    for i in range(row+1, num_row):
        if forest[i][col] >= tree:
            return s + 1
        s += 1
    return s

# determine view score in all 4 directions
max_view_score = -1
for r in range(num_row):
    for c in range(num_col):
        view_score = vis_rt(r,c) * vis_lt(r,c) * vis_up(r,c) * vis_down(r,c)
        if r == 1 and c == 2:
            print('rt',vis_rt(r,c))
            print('lt',vis_lt(r,c))
            print('up',vis_up(r,c))
            print('down',vis_down(r,c))
        if view_score > max_view_score:
            print(view_score, r, c)
            max_view_score = view_score


# TODO: need to adjust this to start counting from the tree itself, not from
# start of the edge. part 1 that was fine because it was a conditional. this
# needs to count from the tree itself
print('answer:',max_view_score)
