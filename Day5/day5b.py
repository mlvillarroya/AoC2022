import re

def search_blank_row(text):
    for index,line in enumerate(text):
        if line == '\n': return index
def prepare_matrix(number):
    stacks = []
    for column in range(0,number):
        stacks.append([])
    return stacks
def how_many_movements(row):
    return 1

alist = [line for line in open('Day5/input.txt')]
# Stacks: area before the blank row
blank_line = search_blank_row(alist)
stacks_number = int(max(set(alist[blank_line-1].strip())))
stacks = prepare_matrix(stacks_number)
for row in range(0,blank_line-1):
    for column in range(0,stacks_number):
        if alist[row][(column*4)+1]!= ' ': stacks[column].append(alist[row][(column*4)+1])
for stack in stacks:
    stack.reverse()
# read and execute instructions
for row in range(blank_line+1,len(alist)):
    instructions=re.findall(r'\d+',alist[row])
    aux=[]
    for times in range(0,int(instructions[0])):
        aux.append(stacks[int(instructions[1])-1].pop())
    aux.reverse()
    stacks[int(instructions[2])-1] += aux

final_letters = ''
for stack in stacks:
    final_letters+=stack[-1]
print(final_letters)