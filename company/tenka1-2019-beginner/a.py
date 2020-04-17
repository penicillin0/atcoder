a, b, c = map(int, input().split())
big = max(a, b)
small = min(a, b)
print('Yes' if small <= c <= big else 'No')
