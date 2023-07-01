import sys
n = int(sys.stdin.readline())
for i in range(0, n-1):
    print(' '*(n-i-1) + '*'*(2*i+1), sep='')
for i in range(0, n):
    print(' '*i + '*'*(2*(n-i-1)+1), sep='')