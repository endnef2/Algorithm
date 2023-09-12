n = int(input())
lst1 = list(map(int, input().split()))
key = int(input())
cnt = 0
for j in lst1:
    if j == key:
        cnt+=1
print(cnt)