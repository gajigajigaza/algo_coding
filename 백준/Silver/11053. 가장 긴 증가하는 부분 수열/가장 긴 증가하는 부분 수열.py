import sys
a = int(input())
b = list(map(int, sys.stdin.readline().split()))
res = [1]*(a+1)
for i in range(1, a):
    m = 0
    for j in range(0, i):
        if b[i] > b[j]:
            if m < res[j]:
                m = res[j]
    res[i] = m+1
print(max(res))