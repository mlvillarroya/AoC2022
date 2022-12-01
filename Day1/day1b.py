alist = [line.rstrip() for line in open('Day1/input.txt')]
calories_array = []
current = 0
for line in alist:
    if line != '':
        current += int(line)
        continue
    calories_array.append(current)
    current = 0

calories_array.sort(reverse=True)
print(calories_array[0]+calories_array[1]+calories_array[2])    
