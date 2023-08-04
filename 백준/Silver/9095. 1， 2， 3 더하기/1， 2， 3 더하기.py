from collections import deque
def bfs(n):
    que=deque([(n, 1)])
    total=0
    while que:
        node, cnt = que.popleft()
        if node==0:
            total+=cnt
        else:
            for i in [node-1, node-2, node-3]:
                if i >= 0:
                    que.append((i, cnt))
    return total
T = int(input())
for i in range(T):
    n = int(input())
    print(bfs(n))