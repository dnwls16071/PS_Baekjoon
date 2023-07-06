# K개의 소수가 있다. 이때, 이 소수들 중에서 몇 개를 곱해서 얻게 되는 수들이 있을 것이다. 소수들을 선택할 때에는 같은 수를 선택해도 되며, 주어지는 소수 자체도 포함시키자.
#
# 예를 들어 세 소수가 2, 5, 7이었다면, 이러한 곱들을 오름차순으로 나타내 보면, 2, 4, 5, 7, 8, 10, 14, 16, 20, 25, 28, 32, 35, 등이 된다.
#
# K개의 소수가 주어졌을 때, 이러한 소수의 곱들 중에서 N번째 수를 구해 보자. 단 정답은 231보다 작은 자연수이다.

import heapq
import sys
input = sys.stdin.readline

K, N = map(int, input().strip().split())
li = list(map(int, input().strip().split()))

heap = []
for i in li:
    heapq.heappush(heap, i)

for i in range(N):
    num = heapq.heappop(heap)
    for j in range(K):
        temp = num * li[j]
        heapq.heappush(heap, temp)
        if num % li[j] == 0:
            break
else:
    print(num)



