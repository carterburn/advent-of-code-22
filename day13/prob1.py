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
    # check lengths
    if len(left) == 0:
        # left ran out
        return True
    if len(right) == 0:
        # right ran out
        return False

    # check type mismatch of first value
    l = left[0]
    r = right[0]

    if type(l) != type(r):
        if type(l) == int:
            l = [l]
        else:
            r = [r]

    # check if out of order condition exists if l and r are ints
    if type(l) == int:
        if r > l:
            return False

    # if they're lists, drill down on the list comparing
    if not compare(l, r):
        return False

    # continue with list
    return compare(left[1:], right[1:])

correct = []
for i in range(len(pairs)):
    res = compare(pairs[i][0], pairs[i][1])
    if res:
        # not 0 indexed for the answer
        correct.append(i+1)

print('answer:', sum(correct))
"""
def compare(left, right):
    # check lenghts
    if len(left) == 0:
        # left side ran out
        return True
    if len(right) == 0:
        # right side ran out
        return False

    l = left[0]
    r = right[0]

    # mismatch?
    if type(l) != type(r):
        if type(l) == int:
            # convert l to list
            l = [l]
        else:
            r = [r]

    if type(l) == list:
        # drill down another comparison
        if not compare(l,r):
            return False


"""