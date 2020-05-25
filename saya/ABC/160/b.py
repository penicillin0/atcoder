x = int(input())

happy1 = x // 500 * 1000
amari = x % 500
happy2 = amari // 5 * 5

print(happy1 + happy2)
