k = int(input())

candidate = []


def saiki(limit, val, candidate: list):
    candidate.append(val)

    if limit == 10:
        return

    for j in range(-1, 2):
        add = j + (val % 10)
        if 0 <= add <= 9:
            new_val = val * 10 + add
            saiki(limit + 1, new_val, candidate)


# i: 最初の数
for i in range(1, 10):
    saiki(1, i, candidate)
candidate.sort()
print(candidate[k-1])
