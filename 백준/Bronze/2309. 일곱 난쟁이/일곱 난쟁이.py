lst = []
for i in range(9):
    lst.append(int(input()))
lst.sort()
tot = sum(lst) - 100
find_first, find_second = 0, 0
for i in range(9):
    for j in range(i+1, 9):
        if (lst[i]+lst[j]) == tot:
            find_first = lst[i]
            find_second = lst[j]
            break
lst.remove(find_second)
lst.remove(find_first)
print(*lst, sep='\n')