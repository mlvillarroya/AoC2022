alist = [line for line in open('Day6/input.txt')][0]

def has_repeated_characters(text):
    return len(text) != len(set(text))

for index in range(0,len(alist)-3):
    if not has_repeated_characters(alist[index:index+4]): 
        print(index+4)
        break