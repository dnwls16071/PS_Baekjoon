# 음 아닌 정수 N이 주어졌을 때, 이 수를 서로 다른 정수 M(M ≥ 1)개의 팩토리얼의 합으로 나타낼 수 있는지 알아내는 프로그램을 작성하시오. 예를 들어 2=0!+1!로 나타낼 수 있지만, 5는 이와 같은 방식으로 나타낼 수 없다.

import sys
input = sys.stdin.readline

N = int(input().strip())
dp = [0] * 21
dp[0] = 1
for i in range(1, 20):
    dp[i] = i * dp[i-1]

if N == 0:
    print("NO")
else:
    for i in range(20, -1, -1):
        if N >= dp[i]:
            N -= dp[i]

    if N == 0:
        print("YES")
    else:
        print("NO")