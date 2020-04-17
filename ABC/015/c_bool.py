N, M = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]


def dfs(n, q):
    if q == N:
        if n == 0:
            return True
    else:
        for t in T[q]:
            if dfs(n ^ t, q + 1):
                return True


print('Found' if dfs(0, 0) else 'Nothing')
