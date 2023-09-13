# N×M 크기의 공간에 아기 상어 여러 마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 아기 상어가 최대 1마리 존재한다.
#
# 어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다. 두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수이고, 이동은 인접한 8방향(대각선 포함)이 가능하다.
#
# 안전 거리가 가장 큰 칸을 구해보자.

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(N)

queue = deque()

def BFS():
    while queue:
        y, x = queue.popleft()

        dy = [0, 1, 1, 1, 0, -1, -1, -1]
        dx = [-1, -1, 0, 1, 1, 1, 0, -1]
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if 0 <= ny < N and 0 <= nx < M:
                if not graph[ny][nx]:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append([ny, nx])

distance = 0
for y in range(N):
    for x in range(M):
        if graph[y][x] == 1:
            queue.append([y, x])

BFS()
for i in range(N):
    temp = max(graph[i])
    distance = max(distance, temp)
print(distance-1)