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
        response = re.search('Monkey (\d+)',instruction)
        pass



alist = [line.rstrip() for line in open('Day11/input.txt')]
instruction_size = 6
monkey1 = Monkey()
monkey1.read_instruction(alist[0:instruction_size])
print('a')