# 게임 개발자인 밀리는 전투력 시스템을 만들어, 캐릭터가 가진 전투력을 기준으로 칭호를 붙여주려고 한다.
#
# 예를 들어, 전투력 10,000 이하의 캐릭터는 WEAK, 10,000 초과 그리고 100,000 이하의 캐릭터는 NORMAL, 100,000 초과 그리고 1,000,000 이하의 캐릭터는 STRONG 칭호를 붙여준다고 하자. 이를 IF문으로 작성한다면 아래와 같이 구현할 수 있다.
#
# if power <= 10000
#  print WEAK
# else if power <= 100000
#  print NORMAL
# else if power <= 1000000
#  print STRONG
# 혼자서 게임을 개발하느라 매우 바쁜 밀리를 대신해서, 캐릭터의 전투력에 맞는 칭호를 출력하는 프로그램을 작성하자.

#1
# from bisect import bisect_left, bisect_right
# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().strip().split())
# title = []
# damage = []
# for i in range(N):
#     status, val = map(str, input().strip().split())
#     val = int(val)
#     title.append(status)
#     damage.append(val)
#
# for i in range(M):
#     print(title[bisect_left(damage, int(input()))])

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
title = []
damage = []
for i in range(N):
    status, val = map(str, input().strip().split())
    val = int(val)
    title.append(status)
    damage.append(val)

def binary_search(target):
    start = 0
    end = len(damage)-1
    while start <= end:
        mid = (start + end) // 2
        if target > damage[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return title[end+1]

for _ in range(M):
    tmp = int(input())
    print(binary_search(tmp))