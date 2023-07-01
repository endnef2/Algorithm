import sys
n = int(sys.stdin.readline())
for i in range(n, 1, -1):
    print(' '*(i-1)+'*'*(n-i+1))
for i in range(0, n):
    print(' '*i+'*'*(n-i))