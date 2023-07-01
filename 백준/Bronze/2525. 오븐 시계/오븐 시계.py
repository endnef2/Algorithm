import sys
a, b = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
if b+c>=60:
    n = (b+c)//60
    if (a+n) < 24:
        print(a+n, b+c-60*n)
    else:
        print(a+n-24, b+c-60*n)
else:
    print(a, b+c)