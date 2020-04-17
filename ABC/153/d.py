h = int(input())

num = 1
cnt = 0
while h != 1:
    # print(h)
    h = h // 2
    cnt += 1
    num *= 2
print(num + ((2 ** cnt) - 1))
# print(cnt*num)

