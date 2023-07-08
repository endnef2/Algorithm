N, M = map(int, input().split())
lst1 = [i for i in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    lst1[i-1], lst1[j-1] = lst1[j-1], lst1[i-1]
print(*lst1)