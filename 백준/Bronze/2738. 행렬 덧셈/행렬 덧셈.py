n, m = map(int, input().split())
A , B = [], []
i = 0
while True:
    try:
        i+=1
        if i<=n:
            A.append(list(map(int, input().split())))
        else:
            B.append(list(map(int, input().split())))
    except:
        break
answer = []
for i in range(n):
    tmp = []
    for j in range(m):
        tmp.append(A[i][j]+B[i][j])
    answer.append(tmp)
for i in range(n):
    print(*answer[i])