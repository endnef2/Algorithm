lst1 = list(map(int, input().split()))
lst1.remove(max(lst1))
print(max(lst1))