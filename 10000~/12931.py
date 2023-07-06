# 모든 값이 0으로 채워져 있는 길이가 N인 배열 A가 있다. 영선이는 다음과 같은 두 연산을 수행할 수 있다.
#
# 배열에 있는 값 하나를 1 증가시킨다.
# 배열에 있는 모든 값을 두 배 시킨다.
# 배열 B가 주어졌을 때, 배열 A를 B로 만들기 위한 연산의 최소 횟수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input().strip())
A = [0] * N
B = list(map(int, input().strip().split()))
B.sort()

cnt = 0
while True:
    flag = 0
    if sum(A) == sum(B):
        break
    for i in range(N):
        if B[i] % 2 != 0 or B[i] == 0 or B[i] == 1:
            if B[i] == 0:
                continue
            else:
                B[i] -= 1
                cnt += 1
            flag = 1
    if flag == 0:
        for i in range(N):
            B[i] //= 2
        cnt += 1
print(cnt)