# 어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
picture = [list(map(int, input().strip().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def BFS(x, y):
    area = 0
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if 0 <= nx < n and 0 <= ny < m and picture[nx][ny] == 1 and not visited[nx][ny]:
                area += 1
                visited[nx][ny] = True
                queue.append((nx, ny))
    return area + 1

cnt = 0
max_area = 0
for i in range(n):
    for j in range(m):
        if picture[i][j] == 1 and not visited[i][j]:
            cnt += 1
            max_area = max(max_area, BFS(i, j))
print(cnt)
print(max_area)