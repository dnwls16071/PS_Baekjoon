# N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.
#
# P1 IOI
# P2 IOIOI
# P3 IOIOIOI
# PN IOIOI...OI (O가 N개)
# I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
S = input().strip()

t = 0
cnt = 0
res = 0
while t < M-1:
    if S[t:t+3] == "IOI":
        cnt += 1
        t += 2
        if cnt == N:
            res += 1
            cnt -= 1
    else:
        t += 1
        cnt = 0
print(res)