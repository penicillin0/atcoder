from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
AA = [deque(list(map(int, input().split()))) for _ in range(N)]
next_play = []
today_plan = [0] * N
next_play = [AA[i][0] for i in range(N)]

ans = 0
while True:
    game = False
    for i in range(N):
        if today_plan[i] == -1:
            continue
        aite = next_play[i]
        if next_play[aite - 1] == -1 or aite == -1:
            continue
        if (i+1) == next_play[aite-1] and today_plan[aite-1] != -1:
            today_plan[i], today_plan[aite - 1] = -1, -1
            game = True
            AA[i].popleft()
            AA[aite - 1].popleft()

            if len(AA[i]) != 0:
                next_play[i] = AA[i][0]
            else:
                next_play[i] = -1

            if len(AA[aite - 1]) != 0:
                next_play[aite - 1] = AA[aite - 1][0]
            else:
                next_play[aite - 1] = -1
    if game is False:
        print(-1)
        exit()
    else:
        today_plan = [0] * N
    ans += 1
    if next_play == [-1] * N:
        print(ans)
        exit()
