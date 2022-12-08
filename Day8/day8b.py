def look_left(matrix,i,j):
    result = 0
    for k in range(0,j):
        result += 1
        if matrix[i][j] <= matrix[i][j-k-1]: break
    return result

def look_right(matrix,i,j):
    result = 0
    for k in range(j+1,len(matrix[0])):
        result += 1
        if matrix[i][j] <= matrix[i][k]: break
    return result

def look_up(matrix,i,j):
    result = 0
    for k in range(0,i):
        result += 1
        if matrix[i][j] <= matrix[i-k-1][j]: break
    return result

def look_down(matrix,i,j):
    result = 0
    for k in range(i+1,len(matrix)):
        result += 1
        if matrix[i][j] <= matrix[k][j]: break
    return result

matrix = []
for line in open('Day8/input.txt'):
    line = list(map(int,list(line.rstrip())))
    matrix.append(line)

points_list = []
for i,row in enumerate(matrix):
    for j,element in enumerate(row):
        points = look_left(matrix,i,j) * \
                 look_right(matrix,i,j) * \
                 look_up(matrix,i,j) * \
                 look_down(matrix,i,j)
        points_list.append(points)
points_list.sort()
print(points_list[-1])