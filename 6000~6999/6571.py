# 피보나치 수의 정의는 다음과 같다.
#
# f1 := 1
# f2 := 2
# fn := fn-1 + fn-2 (n ≥ 3)
# 두 수 a와 b가 주어졌을 때, 구간 [a, b]에 포함되는 피보나치 수의 개수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

dp = [0] * 1001
dp[1] = 1
dp[2] = 2
for i in range(3, 1001):
    dp[i] = dp[i-1] + dp[i-2]

while True:
    cnt = 0
    a, b = map(int, input().strip().split())
    if a == 0 and b == 0:
        break
    else:
        for i in range(1, 1001):
            if dp[i] >= a and dp[i] <= b:
                cnt += 1
        print(cnt)