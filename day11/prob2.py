import sys
if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = 'test.txt'
with open(fname,'r') as fi:
    lines = list(map(str.strip,fi.readlines()))

class Monkey:
    def __init__(self):
        self.val1 = 0
        self.val2 = 0
        self.op = '+'
        self.items = []
        self.test = 0
        self.true_monkey = 0
        self.false_monkey = 0
        self.inspected = 0

    def __str__(self):
        return str(self.inspected)

# one more redo
monkeys = []
for i in range(0,len(lines),7):
    line = lines[i:i+7]
    m = Monkey()

    itms = line[1].split(':')[1].strip()
    m.items = [int(x) for x in itms.split(',')]

    opline = line[2].split('=')[1].strip().split()
    m.val1 = opline[0]
    m.op = opline[1]
    m.val2 = opline[2]

    testline = line[3].split('by')[1].strip()
    m.test = int(testline)

    trueline = line[4].split('monkey')[1].strip()
    m.true_monkey = int(trueline)

    falseline = line[5].split('monkey')[1].strip()
    m.false_monkey = int(falseline)
    monkeys.append(m)

wdecrease = 1
for m in monkeys:
    wdecrease *= m.test

def test_worry_level(new_worry_level, test_num, throw_true, throw_false):
    if new_worry_level % test_num == 0:
        return throw_true
    else:
        return throw_false

def worry_level(item,op1,op2,operator,worry_decrease):
    value = int(item)
    if op1 == "old":
        op1 = value
    if op2 == "old":
        op2 = value

    if operator == "+":
        return (int(op1) + int(op2))
    elif operator == "*":
        if op1 > worry_decrease:
            return (int(op1) * int(op2)) % worry_decrease
        else:
            return (int(op1) * int(op2))

for r in range(10000):
    for m in monkeys:
        while m.items:
            m.inspected += 1
            item = m.items.pop(0)
            new = worry_level(item,m.val1,m.val2,m.op,wdecrease)
            thrw = test_worry_level(new,m.test,m.true_monkey,m.false_monkey)
            monkeys[thrw].items.append(new)

inspected_items = [m.inspected for m in monkeys]
inspected_items.sort()
print(inspected_items)
print(inspected_items[-1] * inspected_items[-2])
