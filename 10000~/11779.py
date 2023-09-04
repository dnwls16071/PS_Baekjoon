# n(1≤n≤1,000)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1≤m≤100,000)개의 버스가 있다. 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 그러면 A번째 도시에서 B번째 도시 까지 가는데 드는 최소비용과 경로를 출력하여라. 항상 시작점에서 도착점으로의 경로가 존재한다.
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)
distance = [INF] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().strip().split())
    graph[a].append([b, c])
s, e = map(int, input().strip().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next_node, next_dist in graph[now]:
            cost = dist + next_dist
            if distance[next_node] > cost:
                distance[next_node] = cost
                parent[next_node] = now
                heapq.heappush(q, [cost, next_node])
    return distance

res = dijkstra(s)
print(res[e])
path = []
destination = e
while destination:
    path.append(destination)
    destination = parent[destination]
print(len(path))
print(*path[::-1])