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
    if len(set1.intersection(set2)) > 0: subsets += 1
print(subsets)