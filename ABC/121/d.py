A, B = map(int, input().split())


def F(C):
    num = (C + 1) // 2
    if C % 2 == 0:
        if num % 2 == 0:
            return C
        else:
            return 1 ^ C
    else:
        if num % 2 == 0:
            return 0
        else:
            return 1


print(F(A - 1) ^ F(B))

print()
