n = int(input())
lst1 = []
for _ in range(n):
    lst1.append(int(input()))
print(*sorted(lst1), sep='\n')