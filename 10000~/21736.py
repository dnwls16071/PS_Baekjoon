# 2020년에 입학한 헌내기 도연이가 있다. 도연이는 비대면 수업 때문에 학교에 가지 못해 학교에 아는 친구가 없었다. 드디어 대면 수업을 하게 된 도연이는 어서 캠퍼스 내의 사람들과 친해지고 싶다.
#
# 도연이가 다니는 대학의 캠퍼스는
# $N \times M$ 크기이며 캠퍼스에서 이동하는 방법은 벽이 아닌 상하좌우로 이동하는 것이다. 예를 들어, 도연이가 (
# $x$,
# $y$)에 있다면 이동할 수 있는 곳은 (
# $x+1$,
# $y$), (
# $x$,
# $y+1$), (
# $x-1$,
# $y$), (
# $x$,
# $y-1$)이다. 단, 캠퍼스의 밖으로 이동할 수는 없다.
#
# 불쌍한 도연이를 위하여 캠퍼스에서 도연이가 만날 수 있는 사람의 수를 출력하는 프로그램을 작성해보자.

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
campus = []
visited = [[False] * M for _ in range(N)]
for i in range(N):
    lst = list(input().strip())
    campus.append(lst)

cnt = 0
def BFS(a, b):
    global cnt
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
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    if campus[nx][ny] == "O":
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                    elif campus[nx][ny] == "P":
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                        cnt += 1
                    else:
                        continue
    if cnt == 0:
        return "TT"
    else:
        return cnt

for i in range(N):
    for j in range(M):
        if campus[i][j] == "I":
            print(BFS(i, j))