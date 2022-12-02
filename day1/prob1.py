fname = 'input.txt'

with open(fname, 'r') as fi:
    lines = fi.readlines()

max_cal = 0
inc = 0
for line in lines:
    if line == '\n':
        if inc > max_cal:
            max_cal = inc
        inc = 0
    else:
        inc += int(line.strip())

print('answer:', max_cal)
