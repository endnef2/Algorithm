lst1 = []
for i in range(9):
    lst1.append(list(map(int, input().split())))
answer = 0
a, b = 0, 0
for i in range(9):
    for j in range(9):
        if answer < lst1[i][j]:
            answer = lst1[i][j]
            a, b = i, j
print(answer)
print(a+1, b+1)