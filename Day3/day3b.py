import string

alist = [line.rstrip() for line in open('Day3/input.txt')]
# List elements number has to be multiply of three
if len(alist)%3 != 0: raise Exception("Sorry, list row number has to be multiply of 3") 

# Create dictionary
letter_dictionary = {}
for index,letter in enumerate(string.ascii_letters):
    letter_dictionary[letter]=index+1
    
#for each word
points = 0
i = 0
while (i < len(alist)):
    #look for the repeated letter
    repeated = "".join(set(alist[i]).intersection(alist[i+1]).intersection(alist[i+2]))
    points += letter_dictionary[repeated]
    i+=3
print(points)