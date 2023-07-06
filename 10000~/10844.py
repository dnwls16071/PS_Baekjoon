# 45656이란 수를 보자.
#
# 이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.
#
# N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.

import sys
input = sys.stdin.readline

N = int(input().strip())

dp = [[0] * 10 for _ in range(101)]
for i in range(1, 10):
    dp[1][i] = 1
    for a in range(2, N+1):
        for b in range(10):
            if b == 0:
                dp[a][b] = dp[a-1][1]
            elif b == 9:
                dp[a][b] = dp[a-1][8]
            else:
                dp[a][b] = dp[a-1][b-1] + dp[a-1][b+1]
print(sum(dp[N]) % 1000000000)