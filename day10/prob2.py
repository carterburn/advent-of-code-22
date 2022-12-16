import sys
if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = 'test.txt'
with open(fname,'r') as fi:
    lines = list(map(str.strip, fi.readlines()))

measurements = []

def cycle_exec(cyc, reg):
   # if cyc == reg-1|reg|reg+1, draw a #, o.w. draw a .
   pixel = (cyc-1) % 40
   if pixel == reg-1 or pixel == reg or pixel == reg+1:
       sys.stdout.write('#')
   else:
       sys.stdout.write('.')

   if pixel == 39:
        sys.stdout.write('\n')

# difficulty here is measuring DURING cycles
# addx will finish execution after 2 cycles
X = 1
cycle = 1
for inst in lines:
    inst = inst.split(' ')
    # start of cycle 'cycle'
    # measure X DURING this cycle
    cycle_exec(cycle, X)
    if inst[0] == 'noop':
        # increase cycle by 1, X is unchanged
        cycle += 1
    elif inst[0] == 'addx':
        # finish cycle 'cycle'
        cycle += 1
        # start new cycle, measure X DURING this cycle
        cycle_exec(cycle, X)
        # end cycle
        cycle += 1
        # finish execution of addx instruction
        X += int(inst[1])
