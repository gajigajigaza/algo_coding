import sys
from collections import defaultdict

n = int(input())
num = defaultdict(int)
inp = list(map(int, sys.stdin.readline().split()))
for i in inp:
    num[i] += 1
m = int(input())
cnt = list(map(int, sys.stdin.readline().split()))
res = []
for i in cnt:
    res.append(num[i])
print(*res)
