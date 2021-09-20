n = int(input())
W = list(map(str, input().split()))

convert_rule = {"b": 1, "c": 1, "d": 2, "w": 2, "t": 3, "j": 3, "f": 4, "q": 4,
                "l": 5, "v": 5, "s": 6, "x": 6, "p": 7, "m": 7, "h": 8, "k": 8, "n": 9, "g": 9, "z": 0, "r": 0}

ans = []

for w in W:
    a = ""
    for s in w:
        if s.lower() in convert_rule.keys():
            a += str(convert_rule[s.lower()])
    if a != "":
        ans.append(a)

print(*ans)
