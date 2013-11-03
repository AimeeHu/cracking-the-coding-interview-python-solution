def setZero(matrix):
    m = len(matrix)       
    n = len(matrix[0])
    rows = set()
    cols = set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                rows.add(i)
                cols.add(j)

    for row in rows:
        for j in range(n):
            matrix[row][j]=0
    for col in cols:
        for i in range(m):
            matrix[i][col]=0



#-------------------test------------------
#inputMatrix
# 1,2,3,4
# 0,3,4,5
# 4,6,9,0
# 1,1,1,1
#expected output
# 0,2,3,0
# 0,0,0,0
# 0,0,0,0
# 0,1,1,0
inputMatrix = [[1,2,3,4],[0,3,4,5],[4,6,9,0],[1,1,1,1]]
setZero(inputMatrix)
print inputMatrix




