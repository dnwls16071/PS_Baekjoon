# 네 점이 주어졌을 때, 네 점을 이용해 정사각형을 만들 수 있는지 없는지를 구하는 프로그램을 작성하시오.

import math
import sys

T = int(input())

for _ in range(T):
    dot_li = []
    for _ in range(4):
        x, y = map(int, sys.stdin.readline().strip().split())
        dot_li.append([x, y])
    dot_li = sorted(dot_li, key = lambda x : (x[0], x[1]))
    side1 = math.sqrt(abs((dot_li[0][0] - dot_li[1][0])**2) + abs((dot_li[0][1] - dot_li[1][1])**2))
    side2 = math.sqrt(abs((dot_li[0][0] - dot_li[2][0])**2) + abs((dot_li[0][1] - dot_li[2][1])**2))
    side3 = math.sqrt(abs((dot_li[3][0] - dot_li[2][0])**2) + abs((dot_li[3][1] - dot_li[2][1])**2))
    side4 = math.sqrt(abs((dot_li[3][0] - dot_li[1][0])**2) + abs((dot_li[3][1] - dot_li[1][1])**2))

    diagonal1 = math.sqrt(abs((dot_li[1][0] - dot_li[2][0])**2) + abs((dot_li[1][1] - dot_li[2][1])**2))
    diagonal2 = math.sqrt(abs((dot_li[3][0] - dot_li[0][0])**2) + abs((dot_li[3][1] - dot_li[0][1])**2))
    if (side1 == side2 == side3 == side4) and diagonal1 == diagonal2:
        print(1)
    else:
        print(0)