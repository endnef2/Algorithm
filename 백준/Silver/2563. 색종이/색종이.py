N = int(input())
A = []
B = []
for i in range(N):
    x, y = map(int, input().split())
    A.append(x)
    B.append(y)
C = [[0 for i in range(max(B)+10)] for i in range(max(A)+10)]
for k in range(N):
    for i in range(A[k],A[k]+10):
        for j in range(B[k],B[k]+10):
            C[i][j] = 1
total = 0
for i in range(len(C)):
    for j in range(len(C[0])):
        total+=C[i][j]
print(total)