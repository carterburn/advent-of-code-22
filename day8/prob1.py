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

# exterior trees are automatically visible
visible = num_row*2 + ((num_col-2)*2)

def vis_rt(row, col):
    tree = forest[row][col]
    for x in forest[row][col+1:]:
        if x >= tree:
            return False
    return True

def vis_lt(row, col):
    tree = forest[row][col]
    for x in forest[row][:col]:
        if x >= tree:
            return False
    return True

def vis_up(row, col):
    tree = forest[row][col]
    for r in range(0, row):
        if forest[r][col] >= tree:
            return False
    return True

def vis_down(row, col):
    tree = forest[row][col]
    for r in range(row+1, num_row):
        if forest[r][col] >= tree:
            return False
    return True

# determine visible trees on the interior
# tree is visible if all of the other trees between it and an edge of 
# the grid are shorter than it 
for r in range(1, num_row-1):
    for c in range(1, num_col-1):
        if vis_rt(r,c) or vis_lt(r,c) or vis_up(r,c) or vis_down(r,c):
            visible += 1

print('answer:',visible)
