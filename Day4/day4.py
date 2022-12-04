import string

def createSet(limits):
    newSet = set()
    for i in range(int(limits.split("-")[0]),int(limits.split("-")[1])+1):
        newSet.add(i)
    return newSet

alist = [line.rstrip() for line in open('Day4/input.txt')]
subsets = 0
for line in alist:
    sections = line.split(",")
    set1 = createSet(sections[0])
    set2 = createSet(sections[1])
    if (set1.issubset(set2) or set2.issubset(set1)): subsets += 1
print(subsets)