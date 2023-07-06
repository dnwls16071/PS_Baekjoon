# 2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
#
# 아래 그림은 2×17 직사각형을 채운 한가지 예이다.

n = int(input())
dp = [0, 1, 3]
for i in range(3, n+1):
    dp.append(dp[i-2] * 2 + dp[i-1])
print(dp[n] % 10007)