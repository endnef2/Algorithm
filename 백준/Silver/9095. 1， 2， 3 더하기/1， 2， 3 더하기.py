from collections import deque
def bfs(n):
    que=deque([n])
    cnt=0
    while que:
        node = que.popleft()
        if node==0:
            cnt+=1
        else:
            for i in [node-1, node-2, node-3]:
                if i >= 0:
                    que.append(i)
    return cnt
T = int(input())
for i in range(T):
    n = int(input())
    print(bfs(n))