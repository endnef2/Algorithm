import sys
N = int(sys.stdin.readline())
data = []
for i in range(N):
    data.append(int(sys.stdin.readline()))
data.sort()
print(*data, sep = '\n')