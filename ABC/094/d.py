n = int(input())
A = list(map(int, input().split()))

big = -float('inf')
number = 0

for a in A:
    big = max(big, a)


ans = -float('inf')
ans_num = 0
for a in A:
    if a == big:
        continue
    number = min(a, big - a)
    if ans < number:
        ans = number
        ans_num = a
print(big, ans_num)
