import sys
stack = []
n = int(sys.stdin.readline())
for i in range(n):
    lst1 = list(sys.stdin.readline().split())
    if lst1[0] == 'push':
        stack.append(lst1[1])
    elif lst1[0] == 'pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif lst1[0] == 'size':
        print(len(stack))
    elif lst1[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif lst1[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])