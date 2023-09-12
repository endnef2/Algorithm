n, x = map(int, input().split())
lst1 = list(map(int, input().split()))
for i in range(n):
    if lst1[i] < x:
        print(lst1[i], end=' ')