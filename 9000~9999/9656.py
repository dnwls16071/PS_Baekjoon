# 돌 게임은 두 명이서 즐기는 재밌는 게임이다.
#
# 탁자 위에 돌 N개가 있다. 상근이와 창영이는 턴을 번갈아가면서 돌을 가져가며, 돌은 1개 또는 3개 가져갈 수 있다. 마지막 돌을 가져가는 사람이 게임을 지게 된다.
#
# 두 사람이 완벽하게 게임을 했을 때, 이기는 사람을 구하는 프로그램을 작성하시오. 게임은 상근이가 먼저 시작한다.

#1
import sys

N = int(sys.stdin.readline().strip())
cnt = 0         # 상근이가 먼저(홀수), 창영이가 다음(짝수)
while True:
    if N == 1 or N == 3:
        cnt += 1
        break
    else:
        if N == 2:
            N -= 1
            cnt += 1
        else:
            N -= 3
            cnt += 1

if cnt % 2 == 0:
    print("SK")
else:
    print("CY")

#2
import sys

N = int(sys.stdin.readline().strip())

if N % 2 == 0:
    print("SK")
else:
    print("CY")