import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))


def divide_2(num):
    while num % 2 == 0:
        num /= 2
    return int(num)


ans = set()
for a in A:
    ans.add(divide_2(a))
print(len(ans))
