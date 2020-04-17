n, m = map(int, input().split())

seikai = set()
pena_num = 0
pena = [0] * (n + 1)

for i in range(m):
    p, s = map(str, input().split())
    if s == 'WA':
        if p not in seikai:
            pena[int(p)] += 1
        else:
            continue
    else:
        if p not in seikai:
            pena_num += pena[int(p)]
            seikai.add(p)
        else:
            continue
print(len(seikai), pena_num)