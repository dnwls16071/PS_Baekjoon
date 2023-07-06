# 입력으로 양의 정수 A와 K가 주어지면, 아래 연산을 이용하여 A를 K로 변경하려고 한다. 정수 A를 변경할 때 사용할 수 있는 연산 종류는 다음과 같다.
#
# 연산 1: 정수 A에 1을 더한다.
# 연산 2: 정수 A에 2를 곱한다.
# 정수 A를 정수 K로 만들기 위해 필요한 최소 연산 횟수를 출력하자.

import sys

A, K = map(int, sys.stdin.readline().strip().split())

cnt = 0
while True:
    if A == K:
        break

    if K % 2 == 0 and K >= A*2:
        K //= 2
        cnt += 1
    else:
        K -= 1
        cnt += 1
print(cnt)
