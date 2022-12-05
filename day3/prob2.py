fname = 'input.txt'
with open(fname, 'r') as fi:
    lines = fi.readlines()

def repeat_finder(s, t):
    for char in s:
        if t.find(char) != -1:
            return char

def find_common(s,t,u):
    # sort all three strings to make it faster
    ns = sorted(s)[0]
    nt = sorted(t)[0]
    nu = sorted(u)[0]
    for c in sorted(s)[1:]:
        if c != ns[-1]:
            ns += c
    for c in sorted(t)[1:]:
        if c != nt[-1]:
            nt += c
    for c in sorted(u)[1:]:
        if c != nu[-1]:
            nu += c
    
    for x in ns:
        for y in nt:
            for z in nu:
                if x == y and y == z:
                    return x

badges = []
lines = list(map(str.strip, lines))
for i in range(0, len(lines), 3):
    group = lines[i:i+3]
    # find common item in all three rucksacks
    badges.append(find_common(group[0], group[1], group[2]))

# compute the priority of each badge
total = 0
for r in badges:
    if ord(r) > ord('Z'):
        # lowercase 
        total += (ord(r) - ord('a') + 1)
    else:
        # uppercase
        total += (ord(r) - ord('A') + 27)

print('answer', total)
