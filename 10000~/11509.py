# 큰 방에 N개의 풍선이 떠있다. 풍선들은 왼쪽부터 오른쪽까지 일렬로 있다. 진솔이는 화살 가지고 노는 것과 사냥 연습하는 것을 좋아한다. 진솔이는 화살을 왼쪽에서 오른쪽으로 쏜다. 높이는 임의로 선택한다. 화살은 선택된 높이 H에서 풍선을 마주칠 때까지 왼쪽에서 오른쪽으로 이동한다. 화살이 풍선을 마주치는 순간, 풍선은 터지고 사라진다. 화살은 계속해서 가던길을 가는데 높이는 1 줄어든다. 그러므로 만약 화살이 높이 H에서 이동 중이었다면 풍선을 터트린 후에는 높이가 H-1이 된다.
#
# 우리의 목표는 모든 풍선을 터트리되 가능한한 적은 화살을 사용하는 것이다.

# import sys
# input = sys.stdin.readline
#
# N = int(input())
# Ballon = list(map(int, input().strip().split()))
# arrow = 0
#
# while True:
#     Max_ballon = max(Ballon)
#     Max_idx = Ballon.index(max(Ballon))
#
#     if sum(Ballon) == 0:
#         break
#
#     for i in range(Max_idx, len(Ballon)):
#         if Max_ballon == Ballon[i]:
#             Max_ballon -= 1
#             Ballon[i] = 0
#     arrow += 1
# print(arrow)

import sys
input = sys.stdin.readline

N = int(input())
ballon = list(map(int, input().strip().split()))
arrow = [0] * 1000001

result = 0
for i in range(N):
    if arrow[ballon[i]] == 0:
        result += 1
    else:
        arrow[ballon[i]] -= 1
    arrow[ballon[i]-1] += 1
print(result)

# 1차원 배열을 이용한 관리
# 2 1 5 4 3
# 2 : 화살 한 개 필요
# 1 : 높이가 2이면 높이가 1인 지점의 풍선도 제거 가능

# 5 : 화살 한 개 필요
# 4 : 높이가 5면 높이가 4인 지점의 풍선도 제거 가능
# 3 : 높이가 4면 높이가 3인 지점의 풍선도 제거 가능