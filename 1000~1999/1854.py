# 봄캠프를 마친 김진영 조교는 여러 도시를 돌며 여행을 다닐 계획이다. 그런데 김 조교는, '느림의 미학'을 중요시하는 사람이라 항상 최단경로로만 이동하는 것은 별로 좋아하지 않는다. 하지만 너무 시간이 오래 걸리는 경로도 그리 매력적인 것만은 아니어서, 적당한 타협안인 '
# $k$번째 최단경로'를 구하길 원한다. 그를 돕기 위한 프로그램을 작성해 보자.

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, k = map(int, input().strip().split())
start = 1
graph = [[] for _ in range(n+1)]
distance = [[INF] * k for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().strip().split())
    graph[a].append([b, c])

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start][0] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]][k-1]:
                distance[i[0]][k-1] = cost
                distance[i[0]].sort()
                heapq.heappush(queue, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i][k-1] == INF:
        print(-1)
    else:
        print(distance[i][k-1])