import sys
N = int(input())
lst1 = set()
for i in range(N):
    lst1.add(int(sys.stdin.readline()))
lst2 = sorted(set(lst1))
for i in lst2 : 
    print(i)