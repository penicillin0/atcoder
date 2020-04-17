a, b, c, d, e, f = map(int, input().split())


cap = e / (100 + e)
max_noudo = 0
sugar_ans, water_ans = 0, 0
for i in range(f//(100*a)+1):
    for j in range((f - (100 * a * i)) // (100 * b) + 1):
        water = 100 * (i * a + j * b)
        for k in range(((i * a + j * b)*e)//c+1):
            for l in range(((i * a + j * b)*e - k*c)//d+1):
                sugar = k * c + l * d
                if f < water + sugar or water == 0:
                    continue
                else:
                    noudo = sugar / (water + sugar)
                    if max_noudo <= noudo <= cap:
                        max_noudo = noudo
                        sugar_ans = sugar
                        water_ans = water
print(water_ans+sugar_ans, sugar_ans)
