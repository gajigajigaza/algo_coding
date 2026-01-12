n, k = map(int, input().split())

def fact(m):
    res = 1
    for i in range(m, 0, -1):
        res *= i
    return res

print (int(fact(n) / (fact(k)*fact(n-k))))