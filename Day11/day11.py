import re

class Monkey():
    def __init__(self) -> None:
        self.number = 0
        self.items = []
        self.operation = []
        self.test = 0
        self.test_true = 0
        self.test_false = 0
    def read_instruction(self,instruction):
        instruction = '\n'.join(instruction)
        # Look for monkey number
        self.number = re.search('Monkey (\d+)',instruction).groups()[0]
        # Look for items
        for item in re.search('Starting items: (.+)',instruction).groups()[0].split(","):
            self.items.append(int(item))
        # Look for operation
        for item in re.search('new = old (.+)',instruction).groups()[0].split(" "):
            self.operation.append(item)
        # Look for test
        self.test = int(re.search('by (\d+)',instruction).groups()[0])
        # Look for test_true
        self.test_true = int(re.search('If true: throw to monkey (\d+)',instruction).groups()[0])
        # Look for test_false
        self.test_false = int(re.search('If false: throw to monkey (\d+)',instruction).groups()[0])
        

alist = [line.rstrip() for line in open('Day11/input.txt')]
instruction_size = 7
monkey_list = []
monkeys = 0
while monkeys*6 + instruction_size < len(alist):
    monkey = Monkey()
    monkey.read_instruction(alist[monkeys * 6 : monkeys * 6 + instruction_size])
    monkey_list.append(monkey)
    monkeys += 1
print('a')