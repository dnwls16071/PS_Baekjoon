# 세계적인 도둑 상덕이는 보석점을 털기로 결심했다.
#
# 상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다. 상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다. 가방에는 최대 한 개의 보석만 넣을 수 있다.
#
# 상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.

import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
arr = []
bag = []

for i in range(N):
    M, V = map(int, input().strip().split())
    heapq.heappush(arr, (M, V))

for j in range(K):
    C = int(input())
    bag.append(C)
bag.sort()

result = []
answer = 0
for Bag in bag:
    while arr and Bag >= arr[0][0]:
        heapq.heappush(result, -arr[0][1])
        heapq.heappop(arr)
    if result:
        answer -= heapq.heappop(result)
print(answer)