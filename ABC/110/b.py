N, M, X, Y = map(int, input().split())
XX = list(map(int, input().split()))
YY = list(map(int, input().split()))

rightX = max(XX)
leftY = min(YY)
print('No War' if max(rightX, X) < min(leftY, Y) and X < Y else 'War')
