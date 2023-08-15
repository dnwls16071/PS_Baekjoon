# 한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.
#
# N > 1인 경우, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.
#
# 다음 예는 22 × 22 크기의 배열을 방문한 순서이다.
#
# N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.
#
# 다음은 N=3일 때의 예이다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, r, c = map(int, input().strip().split())

answer = 0
def recursive(N, R, C):
    global answer
    if R == r and C == c:
        print(answer)
        sys.exit()

    if not (R <= r < R + N and C <= c < C + N):
        answer += N * N
        return

    recursive(N // 2, R, C)
    recursive(N // 2, R, C + N // 2)
    recursive(N // 2, R + N // 2, C)
    recursive(N // 2, R + N // 2, C + N // 2)


result = recursive(2 ** N, 0, 0)
print(result)