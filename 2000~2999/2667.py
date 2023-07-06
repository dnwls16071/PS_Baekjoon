# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

from collections import deque

import sys
input = sys.stdin.readline

N = int(input().strip())
apartment = [list(map(int, input().strip())) for _ in range(N)]
cnt = 0

def BFS(graph, x, y):
    queue = deque()
    queue.append([x, y])
    graph[a][b] = 0
    cnt = 1
    while queue:
        x, y = queue.popleft()
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                cnt += 1
                graph[nx][ny] = 0
                queue.append([nx, ny])
    return cnt

arr = []
for a in range(N):
    for b in range(N):
        if apartment[a][b] == 1:
            arr.append(BFS(apartment, a, b))
            cnt = 0

arr.sort()
print(len(arr))
for i in arr:
    print(i)
