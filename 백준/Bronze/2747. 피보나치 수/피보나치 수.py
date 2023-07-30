n = int(input())
lst1 = [0, 1]
for i in range(2,n+1):
    lst1.append(lst1[i-1] + lst1[i-2])
print(lst1[n])