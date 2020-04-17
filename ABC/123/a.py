a, b, c, d, e, k = int(input()), int(input()), int(input()), int(input()), int(
    input()), int(input())

ABC = [a, b, c, d, e]

for i in range(5):
    for j in range(5):
        if abs(ABC[i] - ABC[j]) > k:
            print(':(')
            exit()
print('Yay!')
