import sys
from collections import deque

# bfs
c = int(input())
n = int(input())
que = deque()
visited = [False] * (c+1)
graph = [[False] * (c+1) for i in range (c+1)]
for i in range (n):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b], graph[b][a] = True, True
que.append(1)
visited[1] = True
while que:
    v = que.popleft()
    for i in range(1, c+1):
        if graph[v][i] and not visited[i]:
            que.append(i)
            visited[i] = True
print(sum(visited)-1)