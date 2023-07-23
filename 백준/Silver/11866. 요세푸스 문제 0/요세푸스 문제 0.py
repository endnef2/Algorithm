from collections import deque
import sys
n,k = map(int, sys.stdin.readline().split())
def yo(n, k):
    answer = []
    que = deque(range(1, n + 1))
    while len(que)>=1:
        que.rotate(-(k-1))
        answer.append(str(que.popleft()))
    print('<', ", ".join(answer),'>', sep='')
yo(n, k)