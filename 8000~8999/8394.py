# 회의가 끝났고, 이제 악수를 하는 시간이다. 모든 사람은 직사각형 탁자 하나의 한 면에 앉아있다.
#
# 자리를 벗어나지 않고 악수를 하는 방법의 수는 총 몇 가지일까?
#
# 각 사람들은 자신의 왼쪽이나 오른쪽에 있는 사람들과 악수를 할 수 있다. (안 할 수도 있다)

import sys
input = sys.stdin.readline
n = int(input())

dp = [0, 2, 3]
for i in range(3, n+1):
    dp.append((dp[i-2] + dp[i-1]) % 10)

print(dp[n-1])
