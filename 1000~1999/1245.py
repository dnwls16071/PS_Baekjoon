# 농부 민식이가 관리하는 농장은 N×M 격자로 이루어져 있다. 민식이는 농장을 관리하기 위해 산봉우리마다 경비원를 배치하려 한다. 이를 위해 농장에 산봉우리가 총 몇 개 있는지를 세는 것이 문제다.
#
# 산봉우리의 정의는 다음과 같다. 산봉우리는 같은 높이를 가지는 하나의 격자 혹은 인접한 격자들의 집합으로 이루어져 있다. (여기서 "인접하다"의 정의는 X좌표 차이와 Y좌표 차이 모두 1 이하일 경우로 정의된다.) 또한 산봉우리와 인접한 격자는 모두 산봉우리의 높이보다 작아야한다.
#
# 문제는 격자 내에 산봉우리의 개수가 총 몇 개인지 구하는 것이다.

#1 DFS
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
#
# N, M = map(int, input().strip().split())
# farm = [list(map(int, input().strip().split())) for _ in range(N)]
# visited = [[False] * M for _ in range(N)]
#
# def DFS(a, b):
#     global flag
#     da = [0, 1, 1, 1, 0, -1, -1, -1]
#     db = [-1, -1, 0, 1, 1, 1, 0, -1]
#     for i in range(8):
#         na = a + da[i]
#         nb = b + db[i]
#         if na < 0 or na >= N or nb < 0 or nb >= M:
#             continue
#         if farm[na][nb] > farm[a][b]:
#             flag = False
#         if 0 <= na < N and 0 <= nb < M and not visited[na][nb] and farm[na][nb] == farm[a][b]:
#             visited[na][nb] = True
#             DFS(na, nb)
#
# cnt = 0
# for i in range(N):
#     for j in range(M):
#         if farm[i][j] > 0 and not visited[i][j]:
#             flag = True
#             DFS(i, j)
#
#             if flag:
#                 cnt += 1
# print(cnt)

#2 BFS
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
farm = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def BFS(a, b):
    global flag
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True
    while queue:
        x, y = queue.popleft()
        dx = [0, 1, 1, 1, 0, -1, -1, -1]
        dy = [-1, -1, 0, 1, 1, 1, 0, -1]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if farm[nx][ny] > farm[x][y]:
                flag = False
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and farm[nx][ny] == farm[x][y]:
                visited[nx][ny] = True
                queue.append((nx, ny))

cnt = 0
for i in range(N):
    for j in range(M):
        if farm[i][j] > 0 and not visited[i][j]:
            flag = True
            BFS(i, j)
            if flag:
                cnt += 1
print(cnt)