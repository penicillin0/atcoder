import sys
input = sys.stdin.buffer.readline


def canMakeNumber(k, s):
    k = str(k).zfill(3)
    dic = {0: False, 1: False, 2: False}
    for t in s:
        if dic[0] is False:
            if t == k[0]:
                dic[0] = True
        else:
            if dic[1] is False:
                if t == k[1]:
                    dic[1] = True
            else:
                if dic[2] is False:
                    if t == k[2]:
                        dic[2] = True
                        return True
                else:
                    return True
    return False


N = int(input())
S = input()
ans = 0
for i in range(0, 1000):
    if canMakeNumber(i, str(S)):
        ans += 1
print(ans)
