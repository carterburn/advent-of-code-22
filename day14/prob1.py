import sys
if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = 'test.txt'
with open(fname,'r') as fi:
    lines = list(map(str.strip,fi.readlines()))

grid = {}
points = [eval('(' + x + ')') for s in lines for x in s.replace(' ','').split('->')]
grid[points[0]] = '#'
for i in range(1,len(points)):
    grid[points[i]] = '#'
    if points[i][0] == points[i-1][0]:
        # same row
        for j in range(points[i-1][1]+1, points[i][1]):
            grid[(points[i][0],j)] = '#'
    elif points[i][1] == points[i-1][1]:
        # same col
        for j in range(points[i-1][0]+1, points[i][0]):
            grid[(j,points[i][1])] = '#'
    else:
        # new line
        continue

for row in range(min(grid.keys(),key=lambda x: x[0]),max(grid.keys(),key=lambda x: x[0])):
    for col in range(min(grid.keys(),key=lambda x:x[1]),max(grid.keys(),key=lambda x: x[1])):
        if grid[(row,col)] == '#':
            sys.stdout.write('#')
        else:
            sys.stdout.write('.')
    sys.stdout.write('\n')



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
