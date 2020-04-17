N = int(input())
A = list(map(int, input().split()))
bunsi = 1
bunbo = 0
for a in A:
    bunsi *= a

for a in A:
    bunbo += bunsi / a

print(bunsi/bunbo)
