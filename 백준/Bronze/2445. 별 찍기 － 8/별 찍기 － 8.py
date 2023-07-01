import sys
n = int(sys.stdin.readline())
for i in range(1, n):
    print('*'*i + ' '*(n-i) + ' '*(n-i) +'*'*i, sep='')
for i in range(n, 0, -1):
    print('*'*i + ' '*(n-i) + ' '*(n-i) +'*'*i, sep='')
