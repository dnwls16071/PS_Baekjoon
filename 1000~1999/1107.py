# 수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.
#
# 리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다. 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.
#
# 수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.
#
# 수빈이가 지금 보고 있는 채널은 100번이다.

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
button = list(map(str, input().strip().split()))
cnt = abs(N - 100)  # 채널의 개수는 0 <= N <= 500,000이고 현재 수빈이가 시청하고있는 채널은 100번으로 0번으로 이동할 수 있으므로

if N == 100:
    print(0)
    sys.exit()
else:
    for i in range(1000001):
        for j in str(i):
            if j in button:
                break
        else:
            cnt = min(cnt, len(str(i)) + abs(N-i))
print(cnt)