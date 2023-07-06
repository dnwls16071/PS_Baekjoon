# 절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.
#
# 배열에 정수 x (x ≠ 0)를 넣는다.
# 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

import heapq
import sys
input = sys.stdin.readline

heap = []
N = int(input().strip())
for _ in range(N):
    val = int(input().strip())
    if val != 0:
        heapq.heappush(heap, (abs(val), val))
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])