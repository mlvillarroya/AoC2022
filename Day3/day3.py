import string

alist = [line.rstrip() for line in open('Day3/input.txt')]

# Create dictionary
letter_dictionary = {}
for index,letter in enumerate(string.ascii_letters):
    letter_dictionary[letter]=index+1
    
#for each word
points = 0
for word in alist:
    #separate word into two
    word1 = word[:int(len(word)/2)]
    word2 = word[int(len(word)/2):]
    #look for the repeated letter
    repeated = "".join(set(word1).intersection(word2))
    points += letter_dictionary[repeated]
print(points)
