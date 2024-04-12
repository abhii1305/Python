# A = [[1,2,4],
#      [4,5,7]]


# T = [[0,0],
#     [0,0],
#     [0,0]]

# for i in range (len(A)):
#     for j in range (len(A[0])):
#         T[j][i]=A[i][j]

# for i in T:
#     print(i)


# using list comprehension
A = [[1,2,4],
     [4,5,7]]

T= [[A[j][i] for j in range (len(A))]  for i in range(len(A[0]))]

for i in T:
    print(i)