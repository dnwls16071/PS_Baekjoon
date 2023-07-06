# 젤다의 전설 게임에서 화폐의 단위는 루피(rupee)다. 그런데 간혹 '도둑루피'라 불리는 검정색 루피도 존재하는데, 이걸 획득하면 오히려 소지한 루피가 감소하게 된다!
#
# 젤다의 전설 시리즈의 주인공, 링크는 지금 도둑루피만 가득한 N x N 크기의 동굴의 제일 왼쪽 위에 있다. [0][0]번 칸이기도 하다. 왜 이런 곳에 들어왔냐고 묻는다면 밖에서 사람들이 자꾸 "젤다의 전설에 나오는 녹색 애가 젤다지?"라고 물어봤기 때문이다. 링크가 녹색 옷을 입은 주인공이고 젤다는 그냥 잡혀있는 공주인데, 게임 타이틀에 젤다가 나와있다고 자꾸 사람들이 이렇게 착각하니까 정신병에 걸릴 위기에 놓인 것이다.
#
# 하여튼 젤다...아니 링크는 이 동굴의 반대편 출구, 제일 오른쪽 아래 칸인 [N-1][N-1]까지 이동해야 한다. 동굴의 각 칸마다 도둑루피가 있는데, 이 칸을 지나면 해당 도둑루피의 크기만큼 소지금을 잃게 된다. 링크는 잃는 금액을 최소로 하여 동굴 건너편까지 이동해야 하며, 한 번에 상하좌우 인접한 곳으로 1칸씩 이동할 수 있다.
#
# 링크가 잃을 수밖에 없는 최소 금액은 얼마일까?

from collections import deque
import sys
input = sys.stdin.readline

def BFS(a, b):
    queue = deque()
    queue.append((a, b))
    while queue:
        x, y = queue.popleft()
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= T or ny < 0 or ny >= T:
                continue
            if 0 <= nx < T and 0 <= ny < T:
                if cost[nx][ny] > cost[x][y] + graph[nx][ny]:
                    cost[nx][ny] = cost[x][y] + graph[nx][ny]
                    queue.append((nx, ny))

cnt = 1
while True:
    T = int(input())
    if T == 0:
        break
    graph = [list(map(int, input().strip().split())) for _ in range(T)]
    cost = [[1000000] * T for _ in range(T)]
    cost[0][0] = graph[0][0]
    BFS(0, 0)
    print("Problem", str(cnt) + ":", cost[T-1][T-1])
    cnt += 1