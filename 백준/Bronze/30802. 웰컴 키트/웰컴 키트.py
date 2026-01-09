n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())
ti = 0
for i in size:
    if i % t == 0: ti += i//t
    else: ti+= (i//t) +1
print(ti)
print(n//p, n%p)