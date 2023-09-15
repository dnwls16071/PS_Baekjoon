# 게임을 좋아하는 큐브러버는 체스에서 사용할 새로운 말 "데스 나이트"를 만들었다. 데스 나이트가 있는 곳이 (r, c)라면, (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)로 이동할 수 있다.
#
# 크기가 N×N인 체스판과 두 칸 (r1, c1), (r2, c2)가 주어진다. 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 구해보자. 체스판의 행과 열은 0번부터 시작한다.
#
# 데스 나이트는 체스판 밖으로 벗어날 수 없다.

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
chess = [[0] * N for _ in range(N)]
r1, c1, r2, c2 = map(int, input().strip().split())


def BFS(a, b):
    queue = deque()
    queue.append([a, b])
    while queue:
        r, c = queue.popleft()

        dr = [0, 2, 2, 0, -2, -2]
        dc = [-2, -1, 1, 2, 1, -1]
        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if 0 <= nr < N and 0 <= nc < N and not chess[nr][nc]:
                chess[nr][nc] = chess[r][c] + 1
                queue.append([nr, nc])


BFS(r1, c1)
if chess[r2][c2] == 0:
    print(-1)
else:
    print(chess[r2][c2])