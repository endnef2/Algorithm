import sys
n = int(sys.stdin.readline())
for i in range(0, n):
    print(' '*i + '*'*(2*(n-i-1)+1))