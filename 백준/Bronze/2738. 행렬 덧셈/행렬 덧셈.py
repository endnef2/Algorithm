x, y = [], []
n, m = map(int, input().split())
for i in range(n):
    x.append(list(map(int, input().split())))

for i in range(n):
    y.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        print(x[i][j]+y[i][j], end=' ')
    print()