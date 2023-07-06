# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 4가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다. 합을 이루고 있는 수의 순서만 다른 것은 같은 것으로 친다.
#
# 1+1+1+1
# 2+1+1 (1+1+2, 1+2+1)
# 2+2
# 1+3 (3+1)
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

T = int(input().strip())
for i in range(T):
    n = int(input().strip())
    dp = [1] * (n+1)
    for i in range(2,n+1):
        dp[i] += dp[i-2]

    for i in range(3, n+1):
        dp[i] += dp[i-3]

    print(dp[n])