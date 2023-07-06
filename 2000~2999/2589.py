# 보물섬 지도를 발견한 후크 선장은 보물을 찾아나섰다. 보물섬 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다. 각 칸은 육지(L)나 바다(W)로 표시되어 있다. 이 지도에서 이동은 상하좌우로 이웃한 육지로만 가능하며, 한 칸 이동하는데 한 시간이 걸린다. 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다. 육지를 나타내는 두 곳 사이를 최단 거리로 이동하려면 같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안 된다.
#
#
#
# 예를 들어 위와 같이 지도가 주어졌다면 보물은 아래 표시된 두 곳에 묻혀 있게 되고, 이 둘 사이의 최단 거리로 이동하는 시간은 8시간이 된다.
#
#
#
# 보물 지도가 주어질 때, 보물이 묻혀 있는 두 곳 간의 최단 거리로 이동하는 시간을 구하는 프로그램을 작성하시오.

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
Map = [list(input().strip()) for _ in range(N)]

def BFS(a, b):
    time = 0
    queue = deque()
    queue.append((a, b))
    # 육지인 L의 경우라면 BFS 함수가 실행되므로 함수 내에 선언해서 각각의 육지 좌표에 따른 최단거리를 계산하여 최댓값을 출력
    visited = [[0] * M for _ in range(N)]
    visited[a][b] = 1
    while queue:
        x, y = queue.popleft()
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if Map[nx][ny] == "W":
                continue
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and Map[nx][ny] == "L":
                visited[nx][ny] = visited[x][y] + 1
                time = max(time, visited[nx][ny])
                queue.append((nx, ny))
    return time-1

result = 0
for i in range(N):
    for j in range(M):
        if Map[i][j] == "L":
            result = max(result, BFS(i, j))
print(result)
