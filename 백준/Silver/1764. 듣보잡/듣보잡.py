import sys

n, m = map(int, input().split())
dud = set()
bob = set()
for i in range(n):
    dud.add(sys.stdin.readline().strip())
for j in range(m):
    bob.add(sys.stdin.readline().strip())
res = dud & bob
print(len(res))
for i in sorted(res):
    print(i)