import sys
a, b, c = map(int, sys.stdin.readline().split())
lst1 = [a, b, c]
if a==b and a==c:
    print(10000+a*1000)
elif a==b and a!=c:
    print(1000+a*100)
elif a!=b and a==c:
    print(1000+a*100)
elif a!=b and b==c:
    print(1000+b*100)
else:
    print(max(lst1)*100)