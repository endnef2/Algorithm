n, m = map(int, input().split())
A = []
B = []
for _ in range(n):
        A.append(list(map(int, input().split())))
m, k = map(int, input().split())
for _ in range(m):
        B.append(list(map(int, input().split())))
answer = []
for i in range(n):
    lst1 = []
    for l in range(k):
        total = 0
        for j in range(m):
            total += A[i][j] * B[j][l]
        lst1.append(total)
    answer.append(lst1)
for row in answer:
    print(*row)