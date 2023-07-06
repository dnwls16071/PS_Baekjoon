# 용사는 마왕이 숨겨놓은 공주님을 구하기 위해 (N, M) 크기의 성 입구 (1,1)으로 들어왔다. 마왕은 용사가 공주를 찾지 못하도록 성의 여러 군데 마법 벽을 세워놓았다. 용사는 현재의 가지고 있는 무기로는 마법 벽을 통과할 수 없으며, 마법 벽을 피해 (N, M) 위치에 있는 공주님을 구출해야만 한다.
#
# 마왕은 용사를 괴롭히기 위해 공주에게 저주를 걸었다. 저주에 걸린 공주는 T시간 이내로 용사를 만나지 못한다면 영원히 돌로 변하게 된다. 공주님을 구출하고 프러포즈 하고 싶은 용사는 반드시 T시간 내에 공주님이 있는 곳에 도달해야 한다. 용사는 한 칸을 이동하는 데 한 시간이 걸린다. 공주님이 있는 곳에 정확히 T시간만에 도달한 경우에도 구출할 수 있다. 용사는 상하좌우로 이동할 수 있다.
#
#
#
# 성에는 이전 용사가 사용하던 전설의 명검 "그람"이 숨겨져 있다. 용사가 그람을 구하면 마법의 벽이 있는 칸일지라도, 단숨에 벽을 부수고 그 공간으로 갈 수 있다. "그람"은 성의 어딘가에 반드시 한 개 존재하고, 용사는 그람이 있는 곳에 도착하면 바로 사용할 수 있다. 그람이 부술 수 있는 벽의 개수는 제한이 없다.
#
# 우리 모두 용사가 공주님을 안전하게 구출 할 수 있는지, 있다면 얼마나 빨리 구할 수 있는지 알아보자.

from collections import deque
import sys
input = sys.stdin.readline

N, M, T = map(int, input().strip().split())
castle = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
result = 100000

def BFS():
    global result
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
    while queue:
        x, y = queue.popleft()
        # 만약 칼이 있다면? (0, 0)부터
        if castle[x][y] == 2:
            result = N-1-x + M-1-y + visited[x][y] - 1
        if x == N-1 and y == M-1:
            return min(result, visited[x][y] - 1)
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if 0 <= nx < N and 0 <= ny < M and castle[nx][ny] != 1:
                if visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    return result

val = BFS()
if val > T:
    print("Fail")
else:
    print(val)