import sys
from collections import deque

n = int(input())
queue = deque([n])
visited = [0] * (n+1)

while queue:
    current = queue.popleft()

    if current == 1:
        print(visited[1])
        break

    next = []
    if current % 3 == 0: next.append(current//3)
    if current % 2 == 0: next.append(current//2)
    if current - 1 >= 1: next.append(current-1)

    for i in next:
        if visited[i] == 0:
            visited[i] = visited[current] + 1
            queue.append(i)
