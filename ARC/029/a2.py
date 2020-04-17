N = int(input())
T = []
for i in range(N):
    T.append(int(input()))

def dfs(right, left, count):
    if count == N:
        return ':'+str(max(right,left))+
    