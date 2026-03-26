import sys

n = int(sys.stdin.readline())
paper, result = [], []
for i in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

def cut(x, y, l):
    color = paper[x][y]
    
    for i in range(x, x+l):
        for j in range(y, y+l):
            if paper[i][j] != color:
                cut(x, y, l//2)
                cut(x, y+l//2, l//2)
                cut(x+l//2, y, l//2)
                cut(x+l//2, y+l//2, l//2)
                return
    if color == 0: result.append(0)
    else: result.append(1)

cut(0, 0, n)
print(result.count(0)) # 하양은 0
print(result.count(1)) # 파랑은 1