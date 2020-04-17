n = int(input())
A = list(map(int, input().split()))

def func(a):
    num = a % 6
    if num == 0:
        return 6 - 3
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    elif num == 3:
        return 0
    elif num == 4:
        return 1
    elif num == 5:
        return 2

ans = 0
for a in A:
    ans += func(a)
print(ans)