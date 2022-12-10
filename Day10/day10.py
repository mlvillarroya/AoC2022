   
alist = [line.rstrip().split(' ') for line in open('Day10/input.txt')]
cycle = 1
value = 1 
cycle_value = {}
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
print(cycle_value[20]*20 \
    + cycle_value[60]*60 \
    + cycle_value[100]*100 \
    + cycle_value[140]*140 \
    + cycle_value[180]*180 \
    + cycle_value[220]*220) 