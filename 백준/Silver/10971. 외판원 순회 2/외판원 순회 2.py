N = int(input())
lst1 = []
for _ in range(N):
    lst1.append(list(map(int, input().split())))
visit = [0]*N
min_cost = float('inf')
# dfs
def dfs(depth, start, cost):
    global min_cost
    if depth == N-1 and lst1[start][0]!=0:
        min_cost=min(min_cost, cost+lst1[start][0])
        return
    for i in range(N):
        if visit[i]==0 and lst1[start][i]!=0:
            visit[i]=1
            dfs(depth+1, i, cost+lst1[start][i])
            visit[i]=0
visit[0]=1
dfs(0, 0, 0)
print(min_cost)