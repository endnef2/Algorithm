lst1 = list(map(int, input().split()))
del lst1[lst1.index(max(lst1))]
print(max(lst1))