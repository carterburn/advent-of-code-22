import sys
from functools import cmp_to_key
from math import prod
if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = 'test.txt'
with open(fname,'r') as fi:
    lines = list(map(str.strip,fi.readlines()))

pairs = []
for i in range(0,len(lines),3):
    pairs.append((eval(lines[i]), eval(lines[i+1])))

def compare(left, right):
    l = left if isinstance(left, list) else [left]
    r = right if isinstance(right, list) else [right]
    for l2, r2 in zip(l,r):
        if isinstance(l2, list) or isinstance(r2, list):
            res = compare(l2, r2)
        else:
            res = r2 - l2
        if res != 0:
            return res
    return len(r) - len(l)

packets = [y for x in pairs for y in x] + [[[2]], [[6]]]
packets = sorted(packets, key=cmp_to_key(compare), reverse=True)
print('answer:',(packets.index([[2]])+1)*(packets.index([[6]])+1))
