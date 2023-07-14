# N개의 수 A1, A2, ..., AN과 L이 주어진다.
#
# Di = Ai-L+1 ~ Ai 중의 최솟값이라고 할 때, D에 저장된 수를 출력하는 프로그램을 작성하시오. 이때, i ≤ 0 인 Ai는 무시하고 D를 구해야 한다.

from collections import deque
import sys
input = sys.stdin.readline

N, L = list(map(int, input().strip().split()))
A = deque(map(int, input().strip().split()))
D = deque()

for i in range(N):
    while D and D[-1][0] > A[i]:
        D.pop()
    while D and D[0][1] <= i - L:
        D.popleft()
    D.append((A[i], i))
    print(D[0][0], end = " ")