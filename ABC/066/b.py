S = input()
n = len(S)

while True:
    m = len(S)
    S = S[:m - 2]
    if not S:
        print(1)
        exit()
    m = len(S)
    if S[:int(m / 2)] + S[:int(m / 2)] == S:
        print(len(S))
        exit()
