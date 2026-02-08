import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
prefix_sum = [0]
cnt = 0
for i in range(n):
    cnt += num[i]
    prefix_sum.append(cnt)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(prefix_sum[b]-prefix_sum[a-1])