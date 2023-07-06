n = int(input())
lst1 = list(map(int,input().split()))
a = []
for i in lst1:
    if i > 1 :
        for j in range(2, i):
            if i%j ==0:
                a.append(i)
    else:
        a.append(i)
print(n-len(set(a)))