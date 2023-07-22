# 지훈이는 미로에서 일을 한다. 지훈이를 미로에서 탈출하도록 도와주자!
#
# 미로에서의 지훈이의 위치와 불이 붙은 위치를 감안해서 지훈이가 불에 타기전에 탈출할 수 있는지의 여부, 그리고 얼마나 빨리 탈출할 수 있는지를 결정해야한다.
#
# 지훈이와 불은 매 분마다 한칸씩 수평또는 수직으로(비스듬하게 이동하지 않는다) 이동한다.
#
# 불은 각 지점에서 네 방향으로 확산된다.
#
# 지훈이는 미로의 가장자리에 접한 공간에서 탈출할 수 있다.
#
# 지훈이와 불은 벽이 있는 공간은 통과하지 못한다.

import sys
input = sys.stdin.readline
from collections import deque

def BFS():
    while fire_queue:
        x, y = fire_queue.popleft()

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 불이 영역 밖으로 번지지는 않으므로
            if nx < 0 or nx >= R  or ny < 0 or ny >= C:
                continue
            # 불이 벽에는 번지지 않았거나 이미 번진 경우라면?
            if graph[nx][ny] == '#' or fire_visited[nx][ny]:
                continue
            fire_visited[nx][ny] = fire_visited[x][y] + 1
            fire_queue.append((nx, ny))

    while queue:
        x, y = queue.popleft()

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                return visited[x][y]

            if graph[nx][ny] == '#':
                continue
            if visited[nx][ny]:
                continue
            if fire_visited[nx][ny] and visited[x][y] + 1 >= fire_visited[nx][ny]:
                continue

            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))
    return "IMPOSSIBLE"

R, C = map(int, input().strip().split())
graph = []
for _ in range(R):
    graph.append(list(input().strip()))

queue = deque()
fire_queue = deque()
fire_visited = [[0] * C for _ in range(R)]
visited = [[0] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'J':
            queue.append((i, j))
            visited[i][j] = 1
        elif graph[i][j] == 'F':
            fire_queue.append((i, j))
            fire_visited[i][j] = 1
print(BFS())