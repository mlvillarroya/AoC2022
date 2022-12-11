import re

class Monkey():
    def __init__(self) -> None:
        self.number = 0
        self.items = []
        self.operation = []
        self.test = 0
        self.test_true = 0
        self.test_false = 0
        self.inspecting_times = 0
    def __str__(self) -> str:
        return f'Monkey: {self.number}\nTrue: {self.test_true}\nFalse: {self.test_false}'
    
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
    
    def operate(self,item):
        if self.operation[1].isnumeric(): qty = int(self.operation[1])
        else: qty = item
        if self.operation[0] == '*': return item * qty
        else: return item + qty
    
    def manage_items(self,monkey_list):
        while len(self.items) > 0:
            self.inspecting_times += 1
            item = self.items.pop(0)
            item = self.operate(item)
            item = int(item/3)
            if item % self.test == 0: monkey_list[self.test_true].items.append(item)
            else: monkey_list[self.test_false].items.append(item)
            
            

alist = [line.rstrip() for line in open('Day11/input.txt')]
instruction_size = 7
monkey_list = []
monkeys = 0
while monkeys*6 + instruction_size < len(alist):
    monkey = Monkey()
    monkey.read_instruction(alist[monkeys * instruction_size : monkeys * instruction_size + instruction_size])
    monkey_list.append(monkey)
    monkeys += 1

for times in range(0,20):    
    for monkey in monkey_list:
        monkey.manage_items(monkey_list)
inspecting_times = []
for monkey in monkey_list:
    inspecting_times.append(monkey.inspecting_times)
inspecting_times.sort()
print(inspecting_times[-1]*inspecting_times[-2])