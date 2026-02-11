import sys
from collections import deque

def dfs(ground): #ground는 배추 2차원 배열
    visited = []
    need_visited = []
    cnt = 0
    for i in range (n):
        for j in range (m):
            num = ground[i][j]
            if  num == 1 and (i, j) not in visited:
                need_visited.append((i, j))
                cnt += 1
                while need_visited:
                    c =(need_visited.pop())
                    visited.append(c)
                    if c[0]+1 < n and ground[c[0]+1][c[1]] == 1 and (c[0]+1, c[1]) not in visited:
                        need_visited.append((c[0]+1, c[1]))
                    if c[1]+1 < m and ground[c[0]][c[1]+1] == 1 and (c[0], c[1]+1) not in visited:
                        need_visited.append((c[0], c[1]+1))
                    if 0 <= c[0]-1 and ground[c[0]-1][c[1]] == 1 and (c[0]-1, c[1]) not in visited:
                        need_visited.append((c[0]-1, c[1]))
                    if 0 <= c[1]-1 and ground[c[0]][c[1]-1] == 1 and (c[0], c[1]-1) not in visited:
                        need_visited.append((c[0], c[1]-1))

    return cnt

t = int(sys.stdin.readline())

for i in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    ddang = [[0 for _ in range (m)] for _ in range (n)]

    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        ddang[b][a] = 1

    print(dfs(ddang))