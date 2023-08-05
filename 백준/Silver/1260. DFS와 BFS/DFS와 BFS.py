def dfs(v):
    stack=[]
    visit=[0]*(n+1)
    stack.append(v)
    while len(stack)>0:
        curr=stack[-1]
        if visit[curr]==0:
            print(curr, end=' ')
            visit[curr]=1
        flag = False
        for i in sorted(graph[curr]):
            if visit[i]==0:
                stack.append(i)
                flag=True
                break
        if not flag:
            stack.pop()

def bfs(v):
    visit = [0]*(n+1)
    que = deque()
    que.append(v)
    visit[v]=1
    while que:
        a = que.popleft()
        print(a, end=' ')
        for i in sorted(graph[a]):
            if 0<=i<=n and visit[i]==0:
                que.append(i)
                visit[i]=1
from collections import deque
n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n):
    graph[i].sort()
dfs(v)
print()
bfs(v)