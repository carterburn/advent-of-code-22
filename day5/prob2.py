import sys
if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = 'test.txt'
with open(fname,'r') as fi:
    lines = fi.readlines()

# start by determining the first line without crates (first char is NOT [)
crate_line = -1
for i,line in enumerate(lines):
    if line.strip()[0] != '[':
        crate_line = i
        break

num_crates = int(lines[crate_line].strip().split(' ')[-1])
# init crate data structure
crates = {}
for i in range(1, num_crates+1):
    crates[i] = []

def process_line(line):
    # processes the line provided and adds to the proper crate
    # takes chunks of 4 for each iteration (one stack)
    for i in range(0,len(line),4):
       if line[i] == '[':
           crates[(i//4)+1].append(line[i+1])


crate_input = lines[:crate_line]
for line in crate_input:
    process_line(line[:-1])
# reverse the list so that the "top" is the last item in the list for nice pop
# ops
for crate in crates:
    crates[crate].reverse()

# perform operations
for op_line in lines[crate_line+2:]:
    op = op_line.split(' ')
    quantity = int(op[1])
    frm = int(op[3])
    to = int(op[5])
    to_crates = crates[frm][-quantity:]
    for i in range(quantity):
        crates[frm].pop()
    for x in to_crates:
        crates[to].append(x)
    
print(crates)
# print out the "top" of each stack
print('answer: ',end='')
for crate in crates:
    print(crates[crate][-1], end='')
print()
