n=int(input())
l=[[0]*10 for i in range(10)]
for i in range(n):
    t=str(i+1)
    l[int(t[0])][int(t[-1])]+=1
a=0
for i in range(10):
    for j in range(10):
        a+=l[i][j]*l[j][i]
print(a)
