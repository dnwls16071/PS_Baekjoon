# N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다.
#
# 어느 날 이 N명의 학생이 X (1 ≤ X ≤ N)번 마을에 모여서 파티를 벌이기로 했다. 이 마을 사이에는 총 M개의 단방향 도로들이 있고 i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비한다.
#
# 각각의 학생들은 파티에 참석하기 위해 걸어가서 다시 그들의 마을로 돌아와야 한다. 하지만 이 학생들은 워낙 게을러서 최단 시간에 오고 가기를 원한다.
#
# 이 도로들은 단방향이기 때문에 아마 그들이 오고 가는 길이 다를지도 모른다. N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구일지 구하여라.

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M, X = map(int, input().strip().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
for _ in range(M):
    a, b, T = map(int, input().strip().split())
    graph[a].append([b, T])

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * (N + 1)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

result = 0
for i in range(1, N+1):
    start = dijkstra(i)
    end = dijkstra(X)
    result = max(result, start[X] + end[i])
print(result)