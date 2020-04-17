S = list(input())


def dfs(count, string):
    if count == 4:
        if eval(string) == 7:
            return string + '=7'
        else:
            return ''
    plus = dfs(count + 1, string + '+' + S[count])
    minus = dfs(count + 1, string + '-' + S[count])
    return plus + minus


print(dfs(1, S[0])[:9])
