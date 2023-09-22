# 평면에 네 개의 직사각형이 놓여 있는데 그 밑변은 모두 가로축에 평행하다. 이 네 개의 직사각형들은 서로 떨어져 있을 수도 있고, 겹쳐 있을 수도 있고, 하나가 다른 하나를 포함할 수도 있으며, 변이나 꼭짓점이 겹칠 수도 있다.
#
# 이 직사각형들이 차지하는 면적을 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

square = [[0] * 100 for _ in range(100)]
tot = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().strip().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            square[y][x] = 1

for row in square:
    tot += sum(row)
print(tot)