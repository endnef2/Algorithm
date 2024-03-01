n, m = map(int, input().split())
lst1 = [0]*n
for _ in range(m):
    i, j, k = map(int, input().split())
    for x in range(i-1, j):
        lst1[x] = k
print(*lst1)