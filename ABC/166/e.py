N = int(input())
A = list(map(int, input().split()))
A.sort()
num = 2 * (10 ** 5)
mini = A[0]

B = []
for a in A:
    if a <= num:
        B.append(a)




