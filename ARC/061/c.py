S = list(input())
N = len(S)


def dfs(count, str):
    if count == N:
        return eval(str)
    plus = dfs(count + 1, str + '+' + S[count])
    noaction = dfs(count + 1, str + S[count])
    return plus + noaction


print(dfs(1, S[0]))
