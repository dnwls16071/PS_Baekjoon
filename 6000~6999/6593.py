# 당신은 상범 빌딩에 갇히고 말았다. 여기서 탈출하는 가장 빠른 길은 무엇일까? 상범 빌딩은 각 변의 길이가 1인 정육면체(단위 정육면체)로 이루어져있다. 각 정육면체는 금으로 이루어져 있어 지나갈 수 없거나, 비어있어서 지나갈 수 있게 되어있다. 당신은 각 칸에서 인접한 6개의 칸(동,서,남,북,상,하)으로 1분의 시간을 들여 이동할 수 있다. 즉, 대각선으로 이동하는 것은 불가능하다. 그리고 상범 빌딩의 바깥면도 모두 금으로 막혀있어 출구를 통해서만 탈출할 수 있다.
#
# 당신은 상범 빌딩을 탈출할 수 있을까? 만약 그렇다면 얼마나 걸릴까?

from collections import deque
import sys
input = sys.stdin.readline

def BFS(z, x, y):
    queue = deque()
    queue.append((z, x, y))
    visited[z][x][y] = 1
    while queue:
        z, x, y = queue.popleft()
        dz = [0, 0, 0, 0, 1, -1]
        dy = [0, 1, 0, -1, 0, 0]
        dx = [-1, 0, 1, 0, 0, 0]
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            # 범위 밖이라면?
            if nz < 0 or nz >= L or nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            # 금으로 막혀있어 지나갈 수 없는 칸인 #의 경우라면?
            if Building[nz][nx][ny] == "#":
                continue
            # 만약 도착점에 도착했다면?
            if Building[nz][nx][ny] == "E":
                print("Escaped in", visited[z][x][y], "minute(s).")
                return
            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C and visited[nz][nx][ny] == 0:
                if Building[nz][nx][ny] == ".":
                    visited[nz][nx][ny] = visited[z][x][y] + 1
                    queue.append((nz, nx, ny))
    print("Trapped!")

while True:
    L, R, C = map(int, input().strip().split())
    if L == 0 and R == 0 and C == 0:
        break
    Building = [[] * R for _ in range(L)]
    visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    for l in range(L):  # 층 수
        for r in range(R):
            Building[l].append(list(input().strip()))
        input()

    for a in range(L):
        for b in range(R):
            for c in range(C):
                if Building[a][b][c] == "S":
                    BFS(a, b, c)