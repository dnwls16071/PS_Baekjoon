# 2×n 직사각형을 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
#
# 아래 그림은 2×17 직사각형을 채운 한가지 예이다.

# import sys
# input = sys.stdin.readline

tile = [0] * 251
while True:
    try:
        N = int(input())
        tile[0] = 1
        tile[1] = 1
        tile[2] = 3
        if N == 0:
            print(tile[0])
        elif N == 1:
            print(tile[1])
        elif N == 2:
            print(tile[2])
        else:
            for i in range(3, N+1):
                tile[i] = tile[i-1] + 2 * tile[i-2]
            print(tile[N])
    except EOFError:
        break