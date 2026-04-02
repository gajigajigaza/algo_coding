import sys
n, m = map(int, sys.stdin.readline().split())
namu = list(map(int, sys.stdin.readline().split()))
# 시간 초과난 코드 
# for i in range (max(namu), 0, -1):
#     cnt = 0
#     for j in namu:
#         h = j - i
#         if h > 0: cnt += h
#     if cnt >= m:
#         print(i)
#         break

# check[False]*(leng+1) 해서 체크했더니 메모리 초과

#새로
leng = max(namu)

def binary_search(left, right, ans):
    if left > right: return ans
    cnt = 0
    mid = (left + right) // 2
    for j in namu:
        if (j-mid) > 0: cnt += (j-mid)
    if cnt >= m : 
        ans = mid
        left = mid+1
        return binary_search(left, right, mid)
    else: 
        right = mid-1
        return binary_search(left, right, ans)


print(binary_search(1, leng, 0))