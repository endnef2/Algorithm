n, m = map(int, input().split())
lst1=[]
for i in range(n):
    lst1.append(i+1)
for i in range(m):
    a, b = map(int, input().split())
    c = lst1[a-1]
    lst1[a-1] = lst1[b-1]
    lst1[b-1] = c
print(*lst1)