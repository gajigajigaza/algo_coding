import sys
from collections import deque

# dp
def dp(num):
    dp = [0] * (num+1)
    for i in range (1, num+1):
        if i >= 4:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        elif i == 3:
            dp[i] = 4
        else:
            dp[i] = i
    return dp[num]

t = int(input())
for i in range(t):
    m = int(sys.stdin.readline())
    print(dp(m))
