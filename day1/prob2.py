# need to re-adjust the tracking of the max
fname = 'input.txt'

with open(fname, 'r') as fi:
    lines = fi.readlines()

max_cal = []
inc = 0
for line in lines:
    if line == '\n':
        if len(max_cal) < 3:
            max_cal.append(inc)
        else:
            if inc > min(max_cal):
                max_cal.remove(min(max_cal))
                max_cal.append(inc)
        inc = 0
    else:
        inc += int(line.strip())

if inc > min(max_cal):
    max_cal.remove(min(max_cal))
    max_cal.append(inc)

print('answer:', sum(max_cal))
