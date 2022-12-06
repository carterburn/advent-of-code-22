fname = 'input.txt'
with open(fname, 'r') as fi:
    lines = fi.readlines()

lines = list(map(str.strip, lines))
pairs = 0
for line in lines:
    l = line.split(',')
    e1 = l[0].split('-')
    e2 = l[1].split('-')
    e1start = int(e1[0])
    e1stop = int(e1[1])
    e2start = int(e2[0]) 
    e2stop = int(e2[1])
    # check if e2 contained within e1
    if e2start >= e1start and e2stop <= e1stop:
        pairs += 1
        continue
    # check if e1 contained within e2
    if e1start >= e2start and e1stop <= e2stop:
        pairs += 1
        continue
    
print('answer', pairs)
