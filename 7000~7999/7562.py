# 체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?
#

from collections import deque
import sys
input = sys.stdin.readline

def BFS(cx, cy, dx, dy):
    queue = deque()
    queue.append((cx, cy))
    visited[cx][cy] = True
    graph[cx][cy] = 1
    sx = [-2, -2, -1, 1, 2, 2, 1, -1]
    sy = [-1, 1, 2, 2, 1, -1, -2, -2]
    while queue:
        x, y = queue.popleft()
        if x == dx and y == dy:
            print(graph[dx][dy] - 1)
            return

        for i in range(8):
            nx = x + sx[i]
            ny = y + sy[i]
            if nx < 0 or nx >= I or ny < 0 or ny >= I:
                continue
            if 0 <= nx < I and 0 <= ny < I and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

T = int(input())
for _ in range(T):
    I = int(input())
    graph = [[0] * I for _ in range(I)]
    visited = [[False] * I for _ in range(I)]
    cx, cy = map(int, input().strip().split())
    dx, dy = map(int, input().strip().split())
    BFS(cx, cy, dx, dy)