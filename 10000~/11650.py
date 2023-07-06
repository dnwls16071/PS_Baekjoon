# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

import sys

N = int(input())
dot = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    dot.append([x, y])

dot.sort(key=lambda x : (x[0], x[1]))
for i in dot:
    print(*i)