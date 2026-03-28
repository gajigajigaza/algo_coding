lst = [i for i in range (10000)]
result = [i for i in range (10000)]
for i in range (10000):
    check = lst[i]
    res = lst[i]
    while check > 0:
        res += check % 10
        check //= 10
    if res in result: result.remove(res)
for i in result: print(i)