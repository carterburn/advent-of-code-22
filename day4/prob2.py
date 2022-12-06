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
    # check which range starts later
    if e1start >= e2start:
        # e2 starts
        if e1start <= e2stop:
            pairs += 1
    else:
        # e1 starts
        if e2start <= e1stop:
            pairs += 1
        
print('answer', pairs)
