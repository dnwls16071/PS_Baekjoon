# 어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.
#
# 이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오. 또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.
#
# 예를 들어 N=4, K=2, X=1일 때 다음과 같이 그래프가 구성되어 있다고 가정하자.
#
#
#
# 이 때 1번 도시에서 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 2인 도시는 4번 도시 뿐이다.  2번과 3번 도시의 경우, 최단 거리가 1이기 때문에 출력하지 않는다.

#1
from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().strip().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().strip().split())
    graph[A].append(B)

distance = [-1] * (N + 1)
distance[X] = 0


def BFS(v):
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if distance[i] == -1:
                distance[i] = distance[v] + 1
                queue.append(i)


BFS(X)
check = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        check = True

if check == False:
    print(-1)

#2
from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().strip().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().strip().split())
    graph[A].append(B)

distance = [-1] * (N + 1)
distance[X] = 0

def BFS(v):
    li = []
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if distance[i] == -1:
                distance[i] = distance[v] + 1
                queue.append(i)
                if distance[i] == K:
                    li.append(i)
    li.sort()
    if len(li) == 0:
        print(-1)
    else:
        for i in li:
            print(i)

BFS(X)