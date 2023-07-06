# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
#
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for a in range(N):
    for b in range(a):
        if arr[a] > arr[b]:
            dp[a] = max(dp[a], dp[b] + 1)
print(max(dp))