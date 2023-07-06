# LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
#
# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

import sys
input = sys.stdin.readline

String1 = input().strip()
String2 = input().strip()
lenString1 = len(String1)
lenString2 = len(String2)

dp = [[0] * (lenString1+1) for _ in range(lenString2+1)]

for i in range(1, lenString2+1):
    for j in range(1, lenString1+1):
        if String2[i-1] == String1[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])