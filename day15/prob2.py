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

    def itergaps(self, start, stop):
        x = start
        for interval in self.inter:
            yield from range(x, interval[0])
            x = interval[1]
        yield from range(x, stop)

INTS = re.compile(r"-?\d+")

def part2(lines,size=4000000):
    # make interval for each row in the size
    inp = [[int(match.group(0)) for match in INTS.finditer(line)] for line in lines]
    for y in range(size+1):
        intervals = Intervals()
        for sx,sy,bx,by in inp:
            diff = abs(sx-bx) + abs(sy-by) - abs(sy-y)
            start = max(0, sx-diff)
            stop = min(size, sx+diff) + 1
            if start < stop:
                intervals.add(start,stop)
        for x in intervals.itergaps(0, size+1):
            return 4000000 * x + y
    return None

print('answer:',part2(lines))
