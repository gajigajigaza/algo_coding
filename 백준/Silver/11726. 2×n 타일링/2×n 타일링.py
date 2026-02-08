import sys
from collections import deque

def dp(num):
    cnt = [0] * (num+1)
    for i in range(num+1):
        if i <= 3: cnt[i] = i
        else: cnt[i] = cnt[i-1] + cnt[i-2]
    return cnt[num]

n = int(input())
print(dp(n) % 10007)