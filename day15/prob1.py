import re
import bisect
import operator
import sys

if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = 'test.txt'
with open(fname,'r') as fi:
    lines = list(map(str.strip,fi.readlines()))

class Intervals():
    def __init__(self):
        self.inter = []

    def __len__(self):
        return sum(len(range(start,stop)) for start, stop in self.inter)

    def add(self, start, stop):
        # find if start overlaps with other intervals' stop
        i = bisect.bisect_left(self.inter, start, key=operator.itemgetter(1))
        # find if stop overlaps with other intervals' start
        j = bisect.bisect_right(self.inter, stop, key=operator.itemgetter(0))
        if i < j:
            start = min(start, self.inter[i][0])
            stop = max(stop, self.inter[j-1][1])
        self.inter[i:j] = [(start,stop)]
    
INTS = re.compile(r"-?\d+")

def part1(lines,y=2000000):
    intervals, beacons = Intervals(), set()
    for line in lines:
        sx,sy,bx,by = (int(match.group(0)) for match in INTS.finditer(line))
        diff = abs(sx-bx) + abs(sy-by) - abs(sy-y)
        if diff >= 0:
            intervals.add(sx-diff, sx+diff+1)
        if y == by:
            beacons.add(bx)
    return len(intervals) - len(beacons)

print('answer',part1(lines))
