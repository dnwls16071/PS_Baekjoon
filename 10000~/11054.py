# 수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.
#
# 예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만,  {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.
#
# 수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input())

increase = [1 for _ in range(N)]  # 가장 긴 바이토닉 부분 수열(증가하는)
decrease = [1 for _ in range(N)]  # 가장 긴 바이토닉 부분 수열(감소하는)
dp = [0 for _ in range(N)]
A = list(map(int, input().strip().split()))

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            increase[i] = max(increase[i], increase[j]+1)

for i in range(N-1, -1, -1):
    for j in range(i+1, N):
        if A[i] > A[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

for i in range(N):
    dp[i] = increase[i] + decrease[i]
print(max(dp)-1)