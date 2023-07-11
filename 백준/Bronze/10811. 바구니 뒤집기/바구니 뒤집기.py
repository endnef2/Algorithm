N, M = map(int, input().split())
lst = list(range(1, N+1))
for _ in range(M):
    i, j = map(int, input().split())
    temp = lst[i-1:j]
    temp.reverse()
    lst[i-1:j] = temp
print(*lst)