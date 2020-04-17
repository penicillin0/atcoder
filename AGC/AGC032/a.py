N = int(input())
B = list(map(int, input().split()))

for i in range(N):
    if B[i] > (i + 1):
        print('-1')
        exit()

B = reversed(B)

for i in range(N):
        