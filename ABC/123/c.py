N, A, B, C, D, E = int(input()), int(input()), int(input()), int(input()), int(
    input()), int(input())
Min = min([A, B, C, D, E])
print(N // Min + 1 + 4 if N // Min != N / Min else N // Min + 4)
