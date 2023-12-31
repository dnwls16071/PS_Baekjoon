# 수열 A가 주어졌을 때, 가장 긴 감소하는 부분 수열을 구하는 프로그램을 작성하시오.
#
# 예를 들어, 수열 A = {10, 30, 10, 20, 20, 10} 인 경우에 가장 긴 감소하는 부분 수열은 A = {10, 30, 10, 20, 20, 10}  이고, 길이는 3이다.

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().strip().split()))

dp = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] < A[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))