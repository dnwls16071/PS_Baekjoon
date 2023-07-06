# 코레스코 콘도미니엄 8층은 학생들이 3끼의 식사를 해결하는 공간이다. 그러나 몇몇 비양심적인 학생들의 만행으로 음식물이 통로 중간 중간에 떨어져 있다. 이러한 음식물들은 근처에 있는 것끼리 뭉치게 돼서 큰 음식물 쓰레기가 된다.
#
# 이 문제를 출제한 선생님은 개인적으로 이러한 음식물을 실내화에 묻히는 것을 정말 진정으로 싫어한다. 참고로 우리가 구해야 할 답은 이 문제를 낸 조교를 맞추는 것이 아니다.
#
# 통로에 떨어진 음식물을 피해가기란 쉬운 일이 아니다. 따라서 선생님은 떨어진 음식물 중에 제일 큰 음식물만은 피해 가려고 한다.
#
# 선생님을 도와 제일 큰 음식물의 크기를 구해서 “10ra"를 외치지 않게 도와주자.

#1
from collections import deque
import sys
input = sys.stdin.readline

def BFS(x, y):
    cnt = 0
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and school[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))
                cnt += 1
    return cnt + 1

N, M, K = map(int, input().strip().split())
school = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().strip().split())
    school[a-1][b-1] = 1

answer = 0
for a in range(N):
    for b in range(M):
        if school[a][b] == 1 and not visited[a][b]:
            answer = max(BFS(a, b), answer)
print(answer)
