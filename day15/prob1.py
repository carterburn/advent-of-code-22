import sys
if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = 'test.txt'
with open(fname,'r') as fi:
    lines = list(map(str.strip,fi.readlines()))

def get_coordinates(coord):
    stripped = coord[coord.index('x'):]
    x = stripped[stripped.index('x')+len('x='):stripped.index(',')]
    y = stripped[stripped.index('y')+len('y='):]
    return int(x),int(y)

grid = {}
# will map each sensor's closest beacon based on manhattan distance
stob = {}
for line in lines:
    line = line.split(':')
    sensor = line[0]
    beacon = line[1]
    sx,sy = get_coordinates(sensor)
    bx,by = get_coordinates(beacon)
    grid[(sx,sy)] = 'S'
    grid[(bx,by)] = 'B'
    stob[(sx,sy)] = (bx,by)

def print_grid(grid):
    minx = min(grid.keys(),key=lambda x: x[0])[0]
    maxx = max(grid.keys(),key=lambda x: x[0])[0]
    miny = min(grid.keys(),key=lambda x: x[1])[1]
    maxy = max(grid.keys(),key=lambda x: x[1])[1]
  
    # print col numbers
    sys.stdout.write(' '*8)
    for i in range(minx,maxx+1):
        if i % 5 == 0 and i >= 10:
            sys.stdout.write(str(i//10))
        else:
            sys.stdout.write(' ')
    sys.stdout.write('\n' + ' '*8)
    for i in range(minx,maxx+1):
        if i % 5 == 0:
            sys.stdout.write(str(i%10))
        else:
            sys.stdout.write(' ')
    sys.stdout.write('\n')


    for y in range(miny,maxy):
        sys.stdout.write(f'{y: >7} ')
        for x in range(minx,maxx):
            if (x,y) in grid.keys():
                sys.stdout.write(grid[(x,y)])
            else:
                sys.stdout.write('.')
        sys.stdout.write('\n')

def plot_distance(senspos,distance):
    global grid
    # start at max y distances and incrementally increase
    sensorx = senspos[0]
    sensory = senspos[1]
    for y in range(sensory-distance,sensory+distance+1):
        remainder = distance - manhattan((sensorx,sensory), (sensorx,y))
        for x in range(sensorx-remainder,sensorx+remainder+1):
            if (x,y) not in grid.keys():
                # only if an S/B isn't present
                grid[(x,y)] = '#' 

def manhattan(pt1,pt2):
    return abs(pt1[0]-pt2[0]) + abs(pt1[1]-pt2[1])

# find range of each sensor
sensor_range = {}
for sens in stob.keys():
    sensor_range[sens] = manhattan(sens,stob[sens])

beacons = set(stob.values())

def find_coverage(row):
    global sensor_range
    close = {s:r for s,r in sensor_range.items() if abs(s[1] - row) <= r}
    intervals = []
    for sensor, rng in close.items():
        vert_dist = abs(sensor[1] - row)
        max_x = rng - vert_dist
        start = sensor[0] - max_x 
        stop  = sensor[0] + max_x
        intervals.append([start,stop])

    # compress the intervals
    intervals.sort()
    stack = []
    stack.append(intervals[0])

    for interval in intervals[1:]:
        if stack[-1][0] <= interval[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], interval[-1])
        else:
            stack.append(interval)

    return stack

tgt = 10
covintervals = find_coverage(tgt)
coveragecnt = sum(interval[1]-interval[0]+1 for interval in covintervals)
exclude = sum(1 for beacon in beacons if beacon[1] == tgt)
print('answer:',coveragecnt-exclude)

"""
# plot the no detected beacons for each sensor
for sens in stob.keys():
    dist = manhattan(sens,stob[sens])
    plot_distance(sens, dist)

#print_grid(grid)
row = 10
cnt = 0
minx = min(grid.keys(),key=lambda x: x[0])[0]
maxx = max(grid.keys(),key=lambda x: x[0])[0]
for x in range(minx,maxx+1):
    if (x,row) in grid.keys() and grid[(x,row)] == '#':
        cnt += 1

print('answer:',cnt)
"""
