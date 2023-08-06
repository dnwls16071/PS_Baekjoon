# N행 M열의 표 A가 있고, 표의 각 칸에는 숫자가 하나씩 적혀있다.
#
# 연두는 서로 다른 1개 이상의 칸을 선택하려고 하는데, 행의 번호가 선택한 순서대로 등차수열을 이루고 있어야 하고, 열의 번호도 선택한 순서대로 등차수열을 이루고 있어야 한다. 이렇게 선택한 칸에 적힌 수를 순서대로 이어붙이면 정수를 하나 만들 수 있다.
#
# 연두가 만들 수 있는 정수 중에서 가장 큰 완전 제곱수를 구해보자. 완전 제곱수란 어떤 정수를 제곱한 수이다.

import math
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [input().strip() for _ in range(N)]
answer = -1

def func(x):
    x = int(x)
    num = math.sqrt(x)
    if int(num) * int(num) == x:
        return True
    return False

if N == 1 and M == 1:
    result = int(''.join(map(str, table)))
    if func(result):
        print(result)
    else:
        print(answer)
else:
    for y in range(N):
        for x in range(M):
            for dy in range(-N + 1, N):
                for dx in range(-M + 1, M):
                    num = ""
                    current_y = y
                    current_x = x
                    if dx == 0 and dy == 0:
                        continue
                    while 0 <= current_x < M and 0 <= current_y < N:
                        num += table[current_y][current_x]
                        current_x += dx
                        current_y += dy
                        if func(num):
                            answer = max(answer, int(num))
    print(answer)