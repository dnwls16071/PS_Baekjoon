# 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.
#
# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다.
# A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

import sys
input = sys.stdin.readline

A, B = map(int, input().strip().split())
cnt = 1
while True:
    if A == B:
        break

    if B < A*2:
        cnt = -1
        break
    if B % 2 == 0:
        B //= 2
        cnt += 1
    else:
        if B % 10 == 1:
            B //= 10
            cnt += 1
        else:
            cnt = -1
            break
print(cnt)