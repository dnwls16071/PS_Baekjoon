# 자연수
# \(N\)과 정수
# \(K\)가 주어졌을 때 이항 계수
# \(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())

dp = [1] * (N+1)
for i in range(1, N+1):
    dp[i] = i * dp[i-1]

print(dp[N] // (dp[N - K] * dp[K]))