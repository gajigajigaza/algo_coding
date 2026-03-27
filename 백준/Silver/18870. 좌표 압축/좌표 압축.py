import sys

n = int(sys.stdin.readline())
inp = list(map(int, sys.stdin.readline().split()))
s_inp = sorted(set(inp))
d = {}
for k, v in enumerate(s_inp):
    d[v] = k

for i in inp:
    print(d[i], end=" ")