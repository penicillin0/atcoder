s = int(input())


def gusu_fanc(num):
    ans = int(num / 2)
    return ans


def kisu_fanc(num):
    ans = int(3 * num + 1)
    return ans


num_list = [s]
hantei = 0
numbers = s

while hantei == 0:
    # 次の項を追加
    if numbers % 2 == 0:
        numbers = gusu_fanc(numbers)
    else:
        numbers = kisu_fanc(numbers)
    num_list.append(numbers)
    # チェック
    for i in range(len(num_list) - 1):
        if num_list[i] == numbers:
            hantei = 1
print(i + 2)
