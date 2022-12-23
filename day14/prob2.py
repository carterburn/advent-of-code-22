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

# add floor which has y index of maxy+2
minx = min(grid.keys(), key=lambda x: x[0])[0]
maxx = max(grid.keys(), key=lambda x: x[0])[0]
maxy = max(grid.keys(), key=lambda x: x[1])[1]
floory = maxy+2
floorxstart = minx-1
floorxstop = maxx+1
for x in count_ind(floorxstart, floorxstop):
    grid[(x,floory)] = '#'


def print_grid(grid):
    minx = min(grid.keys(), key=lambda x: x[0])[0]
    maxx = max(grid.keys(), key=lambda x: x[0])[0]
    maxy = max(grid.keys(), key=lambda x: x[1])[1]

    # 0 to max y
    for y in range(maxy+1):
        if y < 10:
            sys.stdout.write(' ' + str(y) + '  ')
        else:
            sys.stdout.write(str(y) + '  ')
        for x in range(minx, maxx+1):
            if (x,y) in grid.keys():
                if grid[(x,y)] == '#':
                    sys.stdout.write('#')
                else:
                    sys.stdout.write('o')
            else:
                sys.stdout.write('.')
        sys.stdout.write('\n')

#print_grid(grid)

def drop_sand(maxy):
    # start point it (500,1) (falling from (500,0) first point to decide is
    # 500,1
    global grid
    px,py = 500,0
    while True:
        # check if sand can move down one step
        if py+1 == maxy+2:
            # retroactively add a floor piece for logic (floor is infinite)
            grid[(px,py+1)] = '#'
            grid[(px-1,py+1)] = '#'
            grid[(px+1,py+1)] = '#'
        if (px,py+1) not in grid.keys():
            # clear, continue moving down
            py += 1
            continue
        else:
            # can't move down, try to move down and left
            if (px-1,py+1) not in grid.keys():
                px -= 1
                py += 1
                continue
            else:
                # can't move down and left, try down and right
                if (px+1,py+1) not in grid.keys():
                    px += 1
                    py += 1
                    continue
                else:
                    # can't move anywhere, come to rest
                    grid[(px,py)] = 'o'
                    # check if we've come to rest at 500,1 (can't go down)
                    if px == 500 and py == 0:
                        return False
                    return True
            

# start the sand falling
at_rest = 0
print_grid(grid)
maxy = (max(grid.keys(), key=lambda x: x[1])[1])-2
while drop_sand(maxy):
    at_rest += 1
print_grid(grid)
print('answer:',at_rest+1) # +1 because loop terminates before last sand drop


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
