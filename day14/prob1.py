import sys
from itertools import count
if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = 'test.txt'
with open(fname,'r') as fi:
    lines = list(map(str.strip,fi.readlines()))

def count_ind(start, stop):
    if start < stop:
        for i in range(start, stop+1):
            yield i
    else:
        for j in range(start, stop-1, -1):
            yield j

grid = {}
points = [eval('(' + x + ')') for s in lines for x in s.replace(' ','').split('->')]
for line in lines:
    path = [eval('(' + x + ')') for x in line.replace(' ','').split('->')]
    for i in range(len(path)-1):
        start = path[i]
        stop = path[i+1]
        if start[0] == stop[0]:
            # same x, step through y
            x = start[0]
            for y in count_ind(start[1], stop[1]):
                grid[(x, y)] = '#'
        else:
            # same y, step through x
            y = start[1]
            for x in count_ind(start[0], stop[0]):
                grid[(x,y)] = '#'

minx = min(grid.keys(), key=lambda x: x[1])



"""for path in paths:
    # plot first point
    grid[eval('(' + path[0] + ')')] = '#'
    for i in range(1,len(path)):
        p = eval('(' + path[i] + ')')
        if p[0] == path[i-1][0]:
            # col changes
            for i in range(path[i][1]
        else:
            # row changes
        """
