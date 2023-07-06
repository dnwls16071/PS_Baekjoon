# 상근이는 빈 공간과 벽으로 이루어진 건물에 갇혀있다. 건물의 일부에는 불이 났고, 상근이는 출구를 향해 뛰고 있다.
#
# 매 초마다, 불은 동서남북 방향으로 인접한 빈 공간으로 퍼져나간다. 벽에는 불이 붙지 않는다. 상근이는 동서남북 인접한 칸으로 이동할 수 있으며, 1초가 걸린다. 상근이는 벽을 통과할 수 없고, 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없다. 상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있다.
#
# 빌딩의 지도가 주어졌을 때, 얼마나 빨리 빌딩을 탈출할 수 있는지 구하는 프로그램을 작성하시오.

from collections import deque
import sys
input = sys.stdin.readline

def burn():
    for _ in range(len(fire)):
        x, y = fire.popleft()
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if Building[nx][ny] != "#" and Building[nx][ny] != "*":
                    Building[nx][ny] = "*"
                    fire.append((nx, ny))

def escape():
    flag = False
    for _ in range(len(start)):
        x, y = start.popleft()
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                # 만약 이동하고자하는 좌표가 벽이 아니면서 불이 붙은 좌표가 아니고 빈 공간이라면?
                if not visited[nx][ny] and Building[nx][ny] == "." and Building[nx][ny] != "#" and Building[nx][ny] != "*":
                    flag = True
                    visited[nx][ny] = visited[x][y] + 1
                    start.append((nx, ny))
                # 만약 이동할 수 있는 위치가 없다면?
            else:
                return visited[x][y]
    if not flag:
        return "IMPOSSIBLE"

T = int(input().strip())
for _ in range(T):
    w, h = map(int, input().strip().split())
    Building = []
    fire = deque()      # 불
    start = deque()     # 시작점
    for i in range(h):
        Building.append(list(input().strip()))
        for j in range(w):
            if Building[i][j] == "*":
                fire.append((i, j))
            elif Building[i][j] == "@":
                start.append((i, j))
    visited = [[0 for _ in range(w)] for _ in range(h)]
    visited[start[0][0]][start[0][1]] = 1

    while True:
        burn()
        result = escape()
        if result:
            break
    print(result)


