n = int(input())
for i in range(0, n) :
    cnt = 0
    lst1 = list(map(int, input().split()))
    avg = (sum(lst1[1:]))/lst1[0]
    for j in lst1[1:] :
        if j > avg :
            cnt+=1
    print(format(cnt*100/lst1[0], '.3f')+'%')