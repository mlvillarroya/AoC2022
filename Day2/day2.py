alist = [line.rstrip() for line in open('Day2/input.txt')]
total_points=0
for game in alist:
    value = 0
    if game[2] == 'X':
        value = 1
        if game[0] == 'A':
            value += 3
        elif game[0] == 'C':
            value += 6
    elif game[2] == 'Y':
        value = 2
        if game[0] == 'A':
            value += 6
        elif game[0] == 'B':
            value += 3
    elif game[2] == 'Z':
        value = 3
        if game[0] == 'B':
            value += 6
        elif game[0] == 'C':
            value += 3
    total_points+=value
print(total_points)