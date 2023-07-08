N, M = map(int, input().split())
lst = list(map(int, input().split()))
total = []
for i in range(len(lst)):
    for j in range(len(lst)):
        for k in range(len(lst)):
            if lst[i] == lst[j] or lst[j] == lst[k] or lst[i]==lst[k]:
                continue
            total.append(lst[i]+lst[j]+lst[k])
result = sorted(set(total))
answer = []
for i in result:
    if i <= M:
        answer.append(i)
print(max(answer))