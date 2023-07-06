# 정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.
#
#
#
# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.
#
# 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

from collections import deque

import sys
input = sys.stdin.readline

def BFS(graph, a, b):
    queue = deque()
    queue.append([a, b])
    graph[a][b] = 0
    while queue:
        a, b = queue.popleft()
        dx = [0, 1, 1, 1, 0, -1, -1, -1]
        dy = [-1, -1, 0, 1, 1, 1, 0, -1]
        for t in range(8):
            na = a + dx[t]
            nb = b + dy[t]
            if na < 0 or na >= h or nb < 0 or nb >= w:
                continue
            if 0 <= na < h and 0 <= nb < w and graph[na][nb] == 1:
                graph[na][nb] = 0
                queue.append([na, nb])

while True:
    w, h = map(int, input().strip().split())
    if w == 0 and h == 0:
        break

    Map = []
    cnt = 0
    for _ in range(h):
        Map.append(list(map(int, input().strip().split())))

    for i in range(h):
        for j in range(w):
            if Map[i][j] == 1:
                BFS(Map, i, j)
                cnt += 1
    print(cnt)