import sys

n = int(input())
dp = [0] * (n+1)

for i in range (2, n+1):
    #dp[i]가 숫자 i를 만드는데 필요한 최소 연산 횟수
    dp[i] = dp[i-1] + 1 
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])
