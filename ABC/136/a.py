A, B, C = map(int, input().split())
D = A - B
if D >= C:
    print(0)
else:
    print(C - D)
