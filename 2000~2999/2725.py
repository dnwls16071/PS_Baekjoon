# (0,0)에서 보이는 (x,y)의 개수를 구하려고 한다.(x,y >= 0, 정수)
#
# (0,0)에서 (x,y)가 보이려면 (0,0)과 (x,y)를 연결하는 직선이 다른 점을 통과하지 않아야 한다. 예를 들어 (4,2)는 (0,0)에서 보이지 않는다. 그 이유는 (0,0)과 (4,2)를 연결하는 직선이 (2,1)을 통과하기 때문이다. 아래 그림은 0 <= x,y<=5인 경우에 (0,0)에서 보이는 점의 개수이다. 단, (0,0)은 계산하지 않는다.
#
#
#
# N이 주어졌을 때, 원점에서 보이는 (x,y) 좌표의 개수를 출력하시오. (0 <= x,y <= N)

import sys
input = sys.stdin.readline

def GCD(x, y):
    while y > 0:
        x, y = y, x % y
    return x

dp = [0] * 1001
dp[1] = 3
for i in range(2, 1001):
    cnt = 0
    for j in range(1, i+1):
        if GCD(i, j) == 1:
            cnt += 2
    dp[i] = dp[i-1] + cnt

C = int(input())
for _ in range(C):
    N = int(input())
    print(dp[N])