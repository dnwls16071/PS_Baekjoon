# 지구 온난화로 인하여 북극의 빙산이 녹고 있다. 빙산을 그림 1과 같이 2차원 배열에 표시한다고 하자. 빙산의 각 부분별 높이 정보는 배열의 각 칸에 양의 정수로 저장된다. 빙산 이외의 바다에 해당되는 칸에는 0이 저장된다. 그림 1에서 빈칸은 모두 0으로 채워져 있다고 생각한다.
#
# 빙산의 높이는 바닷물에 많이 접해있는 부분에서 더 빨리 줄어들기 때문에, 배열에서 빙산의 각 부분에 해당되는 칸에 있는 높이는 일년마다 그 칸에 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다. 단, 각 칸에 저장된 높이는 0보다 더 줄어들지 않는다. 바닷물은 호수처럼 빙산에 둘러싸여 있을 수도 있다. 따라서 그림 1의 빙산은 일년후에 그림 2와 같이 변형된다.
#
# 그림 3은 그림 1의 빙산이 2년 후에 변한 모습을 보여준다. 2차원 배열에서 동서남북 방향으로 붙어있는 칸들은 서로 연결되어 있다고 말한다. 따라서 그림 2의 빙산은 한 덩어리이지만, 그림 3의 빙산은 세 덩어리로 분리되어 있다.
#
# 한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램을 작성하시오. 그림 1의 빙산에 대해서는 2가 답이다. 만일 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력한다.

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
iceberg = [list(map(int, input().strip().split())) for _ in range(N)]

def BFS(a, b):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True
    while queue:
        x, y = queue.popleft()
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if iceberg[nx][ny] != 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                else:
                    sea[x][y] += 1

year = 0
while True:
    visited = [[False] * M for _ in range(N)]
    sea = [[0] * M for _ in range(N)]
    li = []
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] != 0 and not visited[i][j]:
                li.append(BFS(i, j))

    for i in range(N):
        for j in range(M):
            iceberg[i][j] -= sea[i][j]
            if iceberg[i][j] < 0:
                iceberg[i][j] = 0

    if len(li) == 0 or len(li) >= 2:
        break
    else:
        year += 1

if len(li) >= 2:
    print(year)
else:
    print(0)