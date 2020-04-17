N, M = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]


def dfs(num, q):
    if q == N:
        if num == 0:
            print('Found')
            exit()
    else:
        for i in range(M):
            dfs(num ^ T[q][i], q + 1)


dfs(0, 0)
print('Nothing')
