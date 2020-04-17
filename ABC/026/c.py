N = int(input())
B = [int(input()) for _ in range(N-1)]


def make_buka_list(num):
    rep_list = []
    for i, b in enumerate(B):
        i += 2
        if i == num:
            continue
        elif b == num:
            rep_list.append(i)
    return rep_list


def dfs(buka_list, num):
    if buka_list == []:
        return 1
    else:

        return max([dfs(make_buka_list(i), i) for i in buka_list]) + min([dfs(make_buka_list(i), i) for i in buka_list]) + 1


print(dfs(make_buka_list(1), 1))
