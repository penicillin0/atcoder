from fractions import gcd
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
A = list(map(int, input().split()))
A = list(set(A))


if n == 1:
    if A[0] % 2 == 1:
        print(0)
        exit()

    b = 2 * m / A[0] - 1
    print(int(b//2))
    exit()
    


baisu = A[0]
if A[0] % 2 == 1 or A[0] == 0:
    print(0)
    exit()




for i in range(1, len(A)):
    if A[i] % 2 == 1 or A[i] == 0:
        print(0)
        exit()
    baisu = baisu * A[i] // gcd(baisu, A[i])



# for a in A:
    # baisu = lcm(baisu, a)
# print(baisu)


b = baisu // 2
c = m // b + 1
d = c // 2
print(d)
