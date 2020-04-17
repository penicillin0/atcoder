s = input()
K = int(input())
n = len(s)

a = set()
for i in range(1, 6):  # i文字
    for j in range(n - (i - 1)):  # j回
        a.add(s[j:j + i])
print(sorted(a)[K - 1])
