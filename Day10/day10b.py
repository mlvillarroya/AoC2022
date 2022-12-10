   
alist = [line.rstrip().split(' ') for line in open('Day10/input.txt')]
cycle = 1
value = 1 
cycle_value = {cycle:value}
for instruction in alist:
    if instruction[0] == 'addx':
        cycle += 1
        cycle_value[cycle] = value
        cycle += 1
        value += int(instruction[1])
        cycle_value[cycle] = value
    elif instruction[0] == 'noop' :
        cycle += 1
        cycle_value[cycle] = value

for times in range(0,6):
    row = ''
    for position in range(1,41):
        if abs(cycle_value[40 * times + position]-position+1)<2: row += 'x'
        else: row += ' '
    print(row)
