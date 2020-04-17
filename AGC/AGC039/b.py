from collections import deque

N = int(input())

SS = [list(map(int, list(input()))) for _ in range(N)]


s = 0

cnt_list = [[0, 0] for _ in range(N)]

for i in range(N):
    cnt_list[i] = [i, SS[i].count(1)]
# print(cnt_list)
cnt_list.sort(key=lambda x: x[1])
# print(cnt_list)
num = cnt_list[0][0]

List = [0] * N
ans_list = [[] for _ in range(N+1)]
# print(num)


# def DFS(cnt, List, me):
#     if List == [-1] * N:
#         return
#     List[me] = -1
#     ans_list[cnt].append(me)
#     for i, aite in enumerate(SS[me]):
#         if aite == 1 and List[i] == 0:
#             DFS(cnt + 1, List, i)


def BFS(me):
    roots = deque(SS[me])
    List = [0] * N
    while roots:
        List[me] = -1
        ans_list[cnt] += 1
        nex = roots.pop()
        for num, nxt in enumerate(SS[me]):
            num = N - num
        r = roots.pop()
        if r != 0:
            roots.appendleft(r)
        if List == [-1] * N:
            return


BFS(1, List, num)

print(ans_list)
