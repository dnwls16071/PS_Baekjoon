# 중앙값이란, 수열을 정렬했고, 그 크기가 N일 때, 1부터 시작해서 (N+1)/2번째 있는 원소가 그 수열의 중앙값이다. 예를 들어, {1, 2, 6, 5, 4, 3}에서는 3이고, {11, 13, 12, 15, 14}에서는 13이다.
#
# 오세준은 1초에 온도를 하나씩 재는 온도계를 만들었다. 이 온도계에는 작은 디스플레이 창이 하나 있는데, 이 창에는 지금부터 최근 K초 까지 온도의 중앙값을 표시해 준다. (온도를 재기시작한지 K초부터 표시한다. 그 전에는 아무것도 출력되지 않는다.)
#
# 오세준은 온도를 N초동안 쟀다. 그 시간 동안 온도계의 디스플레이 창에 뜨는 숫자의 합을 구하는 프로그램을 작성하시오.
#
# 다른 말로 하면, 길이가 N인 수열이 주어진다. 이 수열은 N-K+1 개의 길이가 K인 연속된 부분 수열이 존재한다. 이 부분 수열의 중앙값의 합을 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
A = [int(input()) for _ in range(N)]

Sum = 0
for i in range(0, N-K+1):
    temp = A[i:i+K]
    if K % 2 == 0:
        Sum += temp[K // 2]
    else:
        Sum += temp[K // 2]