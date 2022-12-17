import sys
if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = 'test.txt'
with open(fname,'r') as fi:
    lines = list(map(str.strip,fi.readlines()))

class Monkey:
    def __init__(self, num):
        self. num = num
        self.inspected_items = 0

    def set_monkey(self, starting_items, operation_str, test_int, true_throw,
            false_throw):
        self.items = starting_items
        self.operation = lambda x: eval('x ' + operation_str)
        self.test = lambda x: (x % test_int) == 0
        self.true_monkey = true_throw
        self.false_monkey = false_throw

    def round(self):
        # inspect each item 
        while True:
            # peek
            if len(self.items) == 0:
                break
            # grab
            item = self.items[0]
            # reset
            if len(self.items) == 0:
                self.items = []
            else:
                self.items = self.items[1:]
            # monkey inspects
            new_worry = self.do_op(item)
            # gets bored, divides by 3
            new_worry = new_worry // 3
            #print(' div3',m.num,new_worry)
            if (new_worry % self.test) == 0:
                self.true_monkey.items.append(new_worry)
            else:
                self.false_monkey.items.append(new_worry)
            self.inspected_items += 1

    def do_op(self,itm):
        return eval(self.operation.replace('x',str(itm)))


    def __str__(self):
        return 'Monkey ' + str(self.num) + ' ' + str(self.items)


monkeys = {}
# find number of monkeys
for line in lines:
    if line.startswith('Monkey'):
        n = int(line[line.index(' ')+1:line.index(':')])
        monkeys[n] = Monkey(n)

# parse monkey input
num = 0
for i in range(1,len(lines)):
    line = lines[i]
    if line.startswith('Monkey'):
        num += 1
    elif line.startswith('Starting'):
        itms = line[line.index(':')+2:]
        monkeys[num].items = []
        for x in itms.split(','):
            monkeys[num].items.append(int(x.strip()))
    elif line.startswith('Operation'):
        op = line[line.index('=')+2:]
        monkeys[num].operation = op.replace('old','x')
    elif line.startswith('Test'):
        monkeys[num].test = int(line[line.index('by')+len('by '):])
    elif line.startswith('If true:'):
        monkeys[num].true_monkey = monkeys[int(line[-1])]
    elif line.startswith('If false:'):
        monkeys[num].false_monkey = monkeys[int(line[-1])]

for i in range(20):
    # iterate through monkeys for round i
    for _,m in monkeys.items():
        m.round()

    # print current monkey items
    for _,m in monkeys.items():
        print('monkey',m.num,':',m.items)

# find two most active monkeys
active = [x.inspected_items for _,x in monkeys.items()]
active.sort()
print('answer:',active[-1] * active[-2])
