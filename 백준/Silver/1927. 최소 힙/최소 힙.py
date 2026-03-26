import sys
from collections import deque

'''
시간초과 코드

n = int(sys.stdin.readline())
cnt = []
for i in range (n):
    inp = int(sys.stdin.readline())
    if inp == 0:
        if not cnt: print(0)
        else: 
            print(min(cnt))
            cnt.remove(min(cnt))
    else:
        cnt.append(inp)
'''

from heapq import heappush, heappop

heap = []
n = int(sys.stdin.readline())
for i in range (n):
    inp = int(sys.stdin.readline())
    if inp == 0:
        if not heap: print(0)
        else: 
            print(heappop(heap))
    else:
        heappush(heap, inp)

