import sys

n = int(sys.stdin.readline())
m = []
res, before = 0, 0

for i in range (n):
    m.append(list(map(int, sys.stdin.readline().split())))

sorted_m = sorted(m, key=lambda x: (x[1], x[0]))

for i in sorted_m:
    if i[0] >= before:
        res += 1
        before = i[1]

print(res)