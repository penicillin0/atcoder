a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(
    input())
cook = [a, b, c, d, e]
A = [10 - a % 10, 10 - b % 10, 10 - c % 10, 10 - d % 10, 10 - e % 10]
for i in range(5):
    if A[i] == 10:
        A[i] = 0

print(sum(cook) + sum(A) - max(A))
