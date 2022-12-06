alist = [line for line in open('Day6/input.txt')][0]

def has_repeated_characters(text):
    return len(text) != len(set(text))

for index in range(0,len(alist)-13):
    if not has_repeated_characters(alist[index:index+14]): 
        print(index+14)
        break