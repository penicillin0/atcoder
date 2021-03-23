N, C = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(N)]

plans = []
for a, b, c in ABC:
    plans.append((a - 1, 's', c))
    plans.append((b, 'e', c))

plans.sort(key=lambda x: x[0])

ans = 0
now_cost = 0
now_day = 0
for p in plans:
    if now_cost < C:
        ans += (p[0] - now_day) * now_cost
    else:
        ans += (p[0] - now_day) * C

    if p[1] == 's':
        now_cost += p[2]
    elif p[1] == 'e':
        now_cost -= p[2]
    now_day = p[0]
print(ans)
