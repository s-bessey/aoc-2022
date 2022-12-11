class Monkey:
    def __init__(self, number, items, op_type, op_val, test, to_monkeys):
        self.number = number
        self.items = items
        self.interactions = 0
        self.test = test
        self.op_type = op_type
        self.op_val = op_val
        self.to_monkeys = to_monkeys
    def inspect(self, item):
        self.interactions += 1
        # if changing by the old value, get the old value
        if self.op_val == "old":
            op_val = item
        else:
            op_val = int(self.op_val)
        # change the value
        if self.op_type == "*":
            item *= op_val
        else:
            item += op_val
        # inspection finished, worry level decreased
        return item
    def test_and_throw(self, item, monkeys):
        if item % self.test == 0:
            monkeys[self.to_monkeys[0]].items.append(item)
        else:
            monkeys[self.to_monkeys[1]].items.append(item)

def read_monkeys(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    monkeys = []
    to_monkeys = []
    for line in lines:
        l = line.split()
        if len(l) == 0:
            monkeys.append(Monkey(number, items, op_type, op_val, test, to_monkeys))
            to_monkeys = []
        elif l[0] == "Monkey":
            number = int(l[1].replace(":", ""))
        elif l[0] == "Starting":
            items = [int(item.replace(",", "")) for item in l[2:]]
        elif l[0] == "Operation:":
            op_type = l[-2]
            op_val = l[-1]  # note: can be "old" instead of a number
        elif l[0] == "Test:":
            test = int(l[-1])
        elif l[0] == "If":
            to_monkeys.append(int(l[-1]))
    # return monkeys
    monkeys.append(Monkey(number, items, op_type, op_val, test, to_monkeys))
    return monkeys

def part1(filename):
    monkeys = read_monkeys(filename)
    for _ in range(20):
        for monkey in monkeys:
            tmp = list(monkey.items)
            for item in tmp:
                new_item = monkey.inspect(item) // 3
                monkey.items.remove(item)
                monkey.test_and_throw(new_item, monkeys)

    # for monkey in monkeys: print(vars(monkey))
    interactions = [i.interactions for i in monkeys]
    interactions.sort()
    return(interactions[-1] * interactions[-2])

def part2(filename):
    monkeys = read_monkeys(filename)
    lcm = 1
    for monkey in monkeys:
        lcm *= monkey.test
    for _ in range(10000):
        for monkey in monkeys:
            tmp = list(monkey.items)
            for item in tmp:
                new_item = monkey.inspect(item) % lcm
                monkey.items.remove(item)
                monkey.test_and_throw(new_item, monkeys)

    # for monkey in monkeys: print(vars(monkey))
    interactions = [i.interactions for i in monkeys]
    interactions.sort()
    return(interactions[-1] * interactions[-2])

# print(part1("day11/data.txt"))
print(part2("day11/data.txt"))
