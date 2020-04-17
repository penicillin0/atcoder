N, M = map(int, input().split())

A_B = []
for i in range(N):
    A, B = map(int, input().split())
    A_B.append([A, B])

A_B_yasui = sorted(A_B, key=lambda x: x[0])

money, drink_hon = 0, 0

for a_b in A_B_yasui:
    a, b = a_b[0], a_b[1]
    if drink_hon + b >= M:
        money += (M - drink_hon) * a
        drink_hon += M - drink_hon
        print(money)
        exit()
    else:
        drink_hon += b
        money += b * a
