# 양치기 꿍은 맨날 늑대가 나타났다고 마을 사람들을 속였지만 이젠 더이상 마을 사람들이 속지 않는다. 화가 난 꿍은 복수심에 불타 아예 늑대들을 양들이 있는 울타리안에 마구 집어넣어 양들을 잡아먹게 했다.
#
# 하지만 양들은 보통 양들이 아니다. 같은 울타리 영역 안의 양들의 숫자가 늑대의 숫자보다 더 많을 경우 늑대가 전부 잡아먹힌다. 물론 그 외의 경우는 양이 전부 잡아먹히겠지만 말이다.
#
# 꿍은 워낙 똑똑했기 때문에 이들의 결과는 이미 알고있다. 만약 빈 공간을 '.'(점)으로 나타내고 울타리를 '#', 늑대를 'v', 양을 'k'라고 나타낸다면 여러분은 몇 마리의 양과 늑대가 살아남을지 계산할 수 있겠는가?
#
# 단, 울타리로 막히지 않은 영역에는 양과 늑대가 없으며 양과 늑대는 대각선으로 이동할 수 없다.

from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().strip().split())

result = [0, 0]  # 양과 늑대의 수
visited = [[False] * C for _ in range(R)]
graph = []
for _ in range(R):
    graph.append(list(input().strip()))

def BFS(a, b):
    global result
    v, k = 0, 0
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True
    while queue:
        y, x = queue.popleft()

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= C or ny < 0 or ny >= R:
                continue
            if 0 <= nx < C and 0 <= ny < R and not visited[ny][nx] and graph[ny][nx] != "#":
                visited[ny][nx] = True
                queue.append((ny, nx))
                if graph[ny][nx] == "v":
                    v += 1
                elif graph[ny][nx] == "k":
                    k += 1
    if v >= k:
        result[1] += v
    else:
        result[0] += k

for i in range(R):
    for j in range(C):
        BFS(i, j)
print(*result)