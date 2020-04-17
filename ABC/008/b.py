n = int(input())
S = [input() for _ in range(n)]

kouho = {}

for s in S:
    if s in kouho:
        kouho[s] += 1
    else:
        kouho[s] = 1

for key, value in kouho.items():
    if value == max(list(kouho.values())):
        print(key)
        exit()
