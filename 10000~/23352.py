# 여러 방들로 둘러싸인 구역을 탈출해야 한다. 알맞은 비밀번호를 입력하면 탈출할 수 있다.
#
# 구역의 지도는
# $N \times M$ 크기의 격자판으로 나타낼 수 있으며 각 칸은 방을 의미하고 각 칸에는 0부터 9까지의 숫자가 적혀있는데 이는 해당하는 방에 적힌 숫자를 의미한다.
#
# 상하좌우 4가지 방향으로만 움직일 수 있으며, 0이 적힌 방은 들어갈 수 없다.
#
# 비밀번호의 힌트는 다음과 같다.
#
# 임의의 방에서 다른 방으로 이동할 때는 항상 두 방 사이의 최단 경로로 이동한다.
# 1번을 만족하는 경로 중 가장 긴 경로의 시작 방과 끝 방에 적힌 숫자의 합
# 만약 위 2가지 조건을 만족하는 경로가 여러 개라면, 시작 방과 끝 방에 적힌 숫자의 합이 가장 큰 값이 비밀번호가 된다.
#
# 시작 방과 끝 방은 동일한 위치일 수도 있다.
#
# <예시>
# $5 \times 5$ 형태의 지도가 주어질 때, 위의 2가지 조건을 만족하는 경로는 다음과 같다.
#
#
#
# 이 때 비밀번호가 무엇인지를 구해라.
#
# 만약 비밀번호를 만들 수 없는 경우 0을 출력한다.

from collections import deque
import sys
import copy
input = sys.stdin.readline

def BFS(a, b):
    map = copy.deepcopy(Map)
    Visited = copy.deepcopy(visited)
    queue = deque([])
    queue.append([a, b])
    start = Map[a][b]
    Map[a][b] = 0   # 다시 회귀할 수 있으므로 반드시 0으로 처리
    while queue:
        queue = list(queue)
        x, y = queue.popleft()
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and Map[nx][ny] > 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    # 큐에 남아있는 맨 마지막의 원소가 도착 지점이 된다.
    end = 0
    for i, j in queue:
        end = Map[i][j]
    # 시작 지점과 도착 지점이 동일한 경우
    if end == 0:
        end = start
    # 시작 지점과 도착 지점이 동일하지 않은 경우
    result.append([max(map(max, visited)), start + end])
    return max(map(max, visited))

N, M = map(int, input().strip().split())
Map = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
result = []

move_cnt = 0
for i in range(N):
    for j in range(M):
        if Map[i][j] != 0:
            val = BFS(i, j)
            if move_cnt < val:
                move_cnt = val

# i : visited배열의 최댓값
# j : 시작 지점과 도착 지점의 번호를 더한 값
password = 0
for i, j in result:
    if i == move_cnt and j > password:
        password = j
print(password)
