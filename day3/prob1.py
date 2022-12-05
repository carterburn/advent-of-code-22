fname = 'input.txt'
with open(fname, 'r') as fi:
    lines = fi.readlines()

def repeat_finder(s, t):
    for char in s:
        if t.find(char) != -1:
            return char

repeats = []
lines = list(map(str.strip, lines))
for line in lines:
    cut = len(line)//2
    # determine the repeated character
    repeats.append(repeat_finder(line[:cut], line[cut:]))

# compute the priority of each repeat
total = 0
for r in repeats:
    if ord(r) > ord('Z'):
        # lowercase 
        total += (ord(r) - ord('a') + 1)
    else:
        # uppercase
        total += (ord(r) - ord('A') + 27)

print('answer', total)
