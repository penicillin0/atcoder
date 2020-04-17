def dfs(n, string):
    if n == N:
        print(string)
    else:
        dfs(n + 1, string + 'a')
        dfs(n + 1, string + 'b')
        dfs(n + 1, string + 'c')


N = int(input())
dfs(0, '')
