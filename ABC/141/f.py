import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    A[i] *= - 1

heapq.heapify(A)

for i in range(M):
    big = (heapq.heappop(A) * -1) // 2
    heapq.heappush(A, big * -1)

print(-sum(A))
