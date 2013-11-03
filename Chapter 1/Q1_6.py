def rotate90Deg(matrix):
    n = len(matrix)
    for layer in range(0,(n+1)/2):
        first = layer
        last = n-layer-1
        for i in range(first, last):
            offset = i-first
            temp = matrix[first][i]                                         #save top
            matrix[first][i] = matrix[last-offset][first]                  #left to top
            matrix[last-offset][first] = matrix[last][last-offset]   #bottom to left
            matrix[last][last-offset] = matrix[i][last]               #right to bottom
            matrix[i][last] = temp                                          #top to righ
    return matrix
    


#----------------------test----------------------
# input 4*4 matrix
# 1  2 3 4
# 4  5 6 7
# 6  8 6 5
# 0 -1 4 2
# expected output
#  0 6 4 1
# -1 8 5 2
#  4 6 6 3
#  2 5 7 4
inputMatrix = [[1,2,3,4],[4,5,6,7],[6,8,6,5],[0,-1,4,2]]
expectedOutput = [[0,6,4,1],[-1,8,5,2],[4,6,6,3],[2,5,7,4]]
if rotate90Deg(inputMatrix) == expectedOutput:
    print "test passed"
else:
    print "test failed"
    print rotate90Deg(inputMatrix)

