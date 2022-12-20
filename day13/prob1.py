import sys
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

correct = []
for i in range(len(pairs)):
    res = compare(pairs[i][0], pairs[i][1])
    print(res)
    if res > 0:
        # not 0 indexed for the answer
        correct.append(i+1)

print(correct)
print('answer:', sum(correct))
