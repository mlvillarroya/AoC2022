alist = [line.rstrip() for line in open('Day1/input.txt')]
max = 0
current = 0
for line in alist:
    if line != '':
        current += int(line)
        continue
    if current > max: 
        max = current
    current = 0
print(max)
    
