def row(i,matrix):
    return matrix[i]
def column(j,matrix):    
    return [row[j] for row in matrix]

def is_visible(matrix,i,j):
    return i == 0 or \
           j == 0 or \
           i >= (len(matrix) - 1)  or \
           j >= (len(matrix[0]) -1) or \
           all(x < matrix[i][j] for x in row(i,matrix)[0:j]) or \
           all(x < matrix[i][j] for x in row(i,matrix)[j+1:]) or \
           all(x < matrix[i][j] for x in column(j,matrix)[0:i]) or \
           all(x < matrix[i][j] for x in column(j,matrix)[i+1:])

matrix = []
for line in open('Day8/input.txt'):
    line = list(map(int,list(line.rstrip())))
    matrix.append(line)

trues = 0
for i,line in enumerate(matrix):
    for j,value in enumerate(line):
        if is_visible(matrix,i,j): trues += 1
print(trues)