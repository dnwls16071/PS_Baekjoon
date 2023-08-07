# 홀수인 자연수 N이 주어지면, 다음과 같이 1부터 N2까지의 자연수를 달팽이 모양으로 N×N의 표에 채울 수 있다.
#
# 9	2	3
# 8	1	4
# 7	6	5
# 25	10	11	12	13
# 24	9	2	3	14
# 23	8	1	4	15
# 22	7	6	5	16
# 21	20	19	18	17
# N이 주어졌을 때, 이러한 표를 출력하는 프로그램을 작성하시오. 또한 N2 이하의 자연수가 하나 주어졌을 때, 그 좌표도 함께 출력하시오. 예를 들어 N=5인 경우 6의 좌표는 (4,3)이다.

import sys
input = sys.stdin.readline

N = int(input())
digit_number = int(input())
table = [[0] * N for _ in range(N)]

current_number = N * N
x, y = 0, 0
direction = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while current_number >= 1:
    table[y][x] = current_number

    if current_number == digit_number:
        target_x, target_y = x, y

    next_x, next_y = x + dx[direction], y + dy[direction]

    if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N or table[next_y][next_x] != 0:
        direction = (direction + 1) % 4

    x, y = x + dx[direction], y + dy[direction]
    current_number -= 1

for row in table:
    print(" ".join(map(str, row)))

for i in range(N):
    for j in range(N):
        if table[i][j] == digit_number:
            print(i+1, j+1)
            break