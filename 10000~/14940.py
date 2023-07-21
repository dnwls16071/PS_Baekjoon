# 지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.
#
# 문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
# 주어지는 지도
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip().split())))
# 확인 완료

visited = [[False] * m for _ in range(n)]
result = [[-1] * m for _ in range(n)]
# 확인 완료

def BFS(a, b):
    queue = deque()
    queue.append((a, b))
    while queue:
        x, y = queue.popleft()
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx = x + dx[i]    # 가로
            ny = y + dy[i]    # 세로
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                result[nx][ny] = result[x][y] + 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            visited[i][j] = True
            x, y = i, j
            result[i][j] = 0

        if graph[i][j] == 0:
            result[i][j] = 0

BFS(x, y)
for i in result:
    for j in i:
        print(j, end = " ")
    print()