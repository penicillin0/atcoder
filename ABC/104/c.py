D, G = map(int, input().split())
questions = []
for i in range(D):
    p, c = map(int, input().split())
    questions.append([p, c])
mini = float('inf')

for i in range(2**(D - 1)):
    bit_num = list(bin(i)[2:].zfill(D - 1))
    for j in range(D):
        bit_num1 = list(bin(i)[2:].zfill(D - 1))
        bit_num1.insert(j, '3')
        print(bit_num1, j)
        for num, one_bit in enumerate(bit_num1):
            score, count = 0, 0
            if one_bit == '1':
                score += questions[num][0] * \
                    (num + 1) * 100 + questions[num][1]
                count += questions[num][0]
            if one_bit == '3':
                for k in range(questions[j][0] + 1):
                    score0 = k * 100 * (j + 1)
                    if k == questions[j][0]:
                        score0 += questions[j][1]
                    count0 = k
                    print(score, count)
print(mini)
