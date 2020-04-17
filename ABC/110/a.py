a, b, c = map(int, input().split())
ABC = [a, b, c]
big = max(ABC)
small = min(ABC)
mid = sum(ABC) - big - small
print(big * 10 + mid + small)
