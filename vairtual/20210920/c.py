def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X % n)
    return str(X % n)


ans = []
n = int(input())


for i in range(3 ** n):
    str_i = Base_10_to_n(i, 3).zfill(n)
    password = str_i.replace('0', 'a').replace('1', 'b').replace('2', 'c')
    ans.append(password)

print(*sorted(ans), sep='\n')
