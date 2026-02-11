import sys
from collections import deque

def dfs(ground): #ground는 배추 2차원 배열
    need_visited = []
    cnt = 0

    dx = [0, 0, -1, 1] # 방향 
    dy = [1, -1, 0, 0]

    for i in range (n):
        for j in range (m):
            if ground[i][j] == 1:
                ground[i][j] = 0
                need_visited.append((i,j))
                cnt += 1

                while need_visited:
                    cx, cy = need_visited.pop()

                    for k in range(4): # 방향
                        nx = cx + dx[k]
                        ny = cy + dy[k]

                        if 0 <= nx < n and 0 <= ny < m and ground[nx][ny] == 1:
                            ground[nx][ny] = 0 # 방문 처리
                            need_visited.append((nx, ny))           

    return cnt

t = int(sys.stdin.readline())

for i in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    ddang = [[0 for _ in range (m)] for _ in range (n)]

    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        ddang[b][a] = 1

    print(dfs(ddang))