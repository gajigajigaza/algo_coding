import sys

n = int(input())
num = set(map(int, sys.stdin.readline().split()))
m = int(input())
res = list(map(int, sys.stdin.readline().split()))
for i in res:
    if i in num: print(1)
    else: print(0)