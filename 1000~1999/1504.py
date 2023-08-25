# 방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.
#
# 세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라. 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().strip().split())
start = 1
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().strip().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
V1, V2 = map(int, input().strip().split())

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance = [INF] * (N + 1)
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
    return distance

start_path = dijkstra(start)
v1_path = dijkstra(V1)
v2_path = dijkstra(V2)

# 1, V1, V2를 거치는 경로 : 1 → V2 → V1 → N
# 1, V1, V2를 거치는 경로 : 1 → V1 → V2 → N
v1_result = start_path[V1] + v1_path[V2] + v2_path[N]
v2_result = start_path[V2] + v2_path[V1] + v1_path[N]

if v1_path[V2] == INF or v2_path[N] == INF or v2_path[V1] == INF or v1_path[N] == INF:
    print(-1)
else:
    print(min(v1_result, v2_result))