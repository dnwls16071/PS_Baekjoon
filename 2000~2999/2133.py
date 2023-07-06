# 3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.

import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 31
dp[0] = 1
dp[2] = 3

# ex. 3 X 1 크기의 벽 : 0
# ex. 3 X 2 크기의 벽 : 3
# ex. 3 X 3 크기의 벽 : 0
# ex. 3 X 4 크기의 벽 : 11
# ex. 3 X 5 크기의 벽 : 0
# ex. 3 X 6 크기의 벽 : 41
# ex. 3 X 7 크기의 벽 : 0

if N < 4:
    if N == 0:
        print(1)
    elif N == 1 or N ==3:
        print(0)
    else:
        print(3)
else:
    for i in range(4, N+1):
        dp[i] = dp[i-2] * 4 - dp[i-4]
    print(dp[N])