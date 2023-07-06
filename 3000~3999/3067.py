# 우리나라 화폐단위, 특히 동전에는 1원, 5원, 10원, 50원, 100원, 500원이 있다. 이 동전들로는 모든 정수의 금액을 만들 수 있으며 그 방법도 여러 가지가 있을 수 있다. 예를 들어 30원을 만들기 위해서는 1원짜리 30개 또는 10원짜리 2개와 5원짜리 2개 등의 방법이 가능하다.
#
# 동전의 종류가 주어질 때에 주어진 금액을 만드는 모든 방법을 세는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().strip().split()))
    cost = int(input())

    dp = [0] * (cost + 1)
    dp[0] = 1   # 0원을 만들 수 있는 방법은 1가지

    # dp 테이블의 정의
    # dp[i] = i원을 만드는데 드는 경우의 수

    # 1원과 2원만 존재
    for i in range(N):
        # 1원만 사용할 경우
        # ex. 1원 만드는데 드는 경우의 수 : 1가지
        # ex. 2원 만드는데 드는 경우의 수 : 1가지
        # ex. 3원 만드는데 드는 경우의 수 : 1가지

        # dp 테이블 상태 : [1, 1, 1, 1]

        # 2원도 사용한다면?
        # ex. 1원 만드는데 드는 경우의 수 : 1가지
        # ex. 2원 만드는데 드는 경우의 수 : 2가지
        # ex. 3원 만드는데 드는 경우의 수 : 2가지

        # dp 테이블 상태 : [1, 1, 2, 2]
        for j in range(coins[i], cost+1):
            dp[j] = dp[j] + dp[j - coins[i]]
    print(dp[cost])