# n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그러면서 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.
#
# 사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
coins = []
for i in range(n):
    coins.append(int(input()))

dp = [10001] * (k+1)
dp[0] = 0
for i in range(k+1):
    for coin in coins:
        if i >= coin:
            dp[i] = min(dp[i], dp[i-coin]+1)
        else:
            continue

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])