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
        for item in self.items:
            # monkey inspects
            new_worry = self.operation(item)
            # gets bored, divides by 3
            new_worry = new_worry // 3
            if self.test(new_worry):
                self.true_monkey.items.append(new_worry)
            else:
                self.false_monkey.items.append(new_worry)
            self.inspected_items += 1

    def __str__(self):
        return 'Monkey ' + str(self.num) + ' ' + str(self.items)


monkeys = {}
m = None
for line in lines:
    line = line.strip()
    if line.startswith('Monkey'):
        if m:
            monkeys[m.num] = m
        col = line.split(':')[0]
        num = int(col.split(' ')[1])
        m = Monkey(num)
    elif line.startswith('Starting items:'):
        itms = line.split(':')[1].strip()
        m.items = eval('[' + itms + ']')
    elif line.startswith('Operation'):
        op = line[line.index('old ')+len('old '):]
        m.operation = lambda x: eval('x ' + op)
    elif line.startswith('Test'):
        mod = int(line[line.index('by ')+len('by '):])
        m.test = lambda x: (x % mod) == 0
    elif line.startswith('If true'):
        monk = int(line[line.index('monkey')+len('monkey '):])
        m.true_monkey = monk
    elif line.startswith('If false'):
        monk = int(line[line.index('monkey')+len('monkey '):])
        m.false_monkey = monk

# commit last one
monkeys[m.num] = m
# doctor up the true/false monkey piece (change type to actual monkey)
for _, m in monkeys.items():
    m.true_monkey = monkeys[m.true_monkey]
    m.false_monkey = monkeys[m.false_monkey]


for i in range(20):
    # iterate through monkeys for round i
    for _,m in monkeys.items():
        m.round()

    # print current monkey items
    for _,m in monkeys.items():
        print('monkey',m.num,':',m.items)

# find two most active monkeys
active = [x.inspected_items for x in monkeys.keys()]
active.sort()
print('answer:',active[-1] * active[-2])
