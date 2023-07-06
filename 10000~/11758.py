# 2차원 좌표 평면 위에 있는 점 3개 P1, P2, P3가 주어진다. P1, P2, P3를 순서대로 이은 선분이 어떤 방향을 이루고 있는지 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

x1, y1 = map(int, input().strip().split())
x2, y2 = map(int, input().strip().split())
x3, y3 = map(int, input().strip().split())

result = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
if result > 0:
    print(1)
elif result == 0:
    print(0)
else:
    print(-1)