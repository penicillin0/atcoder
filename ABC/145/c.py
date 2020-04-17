import itertools
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
L = list(range(N))
jun = list(itertools.permutations(L))
# print(jun)

ans = 0


for j in jun:
    for num, index in enumerate(j):
        if num == 0:
            bx, by = XY[index]
            continue
        else:
            x, y = XY[index]
            ans += ((x - bx) ** 2 + (y - by) ** 2) ** (0.5)
            bx, by = x, y
# print(len(jun))
print(ans / len(jun))
