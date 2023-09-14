n, m = map(int, input().split())
lst1 = list(range(0, n+1))
for _ in range(m):
    i, j = map(int, input().split())
    lst1[i], lst1[j] = lst1[j], lst1[i]
print(*lst1[1:], end=' ')