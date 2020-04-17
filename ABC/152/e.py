import sys
def input():
    return sys.stdin.readline()[:-1]
n=int(input())
li=[[0]*10 for i in range(10)]
for i in range(n):
    tmp=str(i+1)
    li[int(tmp[0])][int(tmp[-1])]+=1
# print(li)
ans=0
for i in range(10):
    for j in range(10):
        ans+=li[i][j]*li[j][i]
print(ans)