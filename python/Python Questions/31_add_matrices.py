A = [[1,2,4],
     [3,4,5],
     [4,5,7]]
B = [[4,6,3],
     [6,3,6],
     [8,6,4]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]



for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j]+B[i][j]


for r in result:
    print(r)