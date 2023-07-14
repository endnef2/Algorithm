lst = []
for i in range(5):
    lst.append(input())
for j in range(15):
    for i in range(5):
        if j < len(lst[i]):
            print(lst[i][j], end='')