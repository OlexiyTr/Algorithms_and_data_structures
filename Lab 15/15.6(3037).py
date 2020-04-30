n,m = map(int,input().split())

a = [[] for _ in range(50005)]
last = [[0, 0, 0, 0, 0] for _ in range(50005)]
visited = [0] * 50005
result = [0] * 50005
top = []

def dfs(v):
    visited[v] = 1
    for u in a[v]:
        if not visited[u]:
            dfs(u)
    top.append(v)

for i in range(m):
    x, y = map(int,input().split())
    x-=1
    y-=1
    a[y].append(x)

k = int(input())

for i in range(k):
    y, x = map(int,input().split())
    y-=1
    x-=1
    last[x][y] = i + 1

for i in range(n):
    if not visited[i]:
        dfs(i)

for v in top:
    for u in a[v]:
        last[v][3] = max(last[v][3], last[u][3])
    result[v] = result[v] | (last[v][0] > last[v][1])
    for u in a[v]:
        result[v] = result[v] | (result[u] and (max(last[u][2],last[u][3]) > last[u][4]))

for i in range(n):
    print(result[i], end = ' ')
