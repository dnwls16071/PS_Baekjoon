# N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 버스가 M개 있다. 각 버스는 A, B, C로 나타낼 수 있는데, A는 시작도시, B는 도착도시, C는 버스를 타고 이동하는데 걸리는 시간이다. 시간 C가 양수가 아닌 경우가 있다. C = 0인 경우는 순간 이동을 하는 경우, C < 0인 경우는 타임머신으로 시간을 되돌아가는 경우이다.
#
# 1번 도시에서 출발해서 나머지 도시로 가는 가장 빠른 시간을 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(start):
    dist[start] = 0
    for i in range(N):
        for j in range(M):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                if i == N-1:
                    return True
    return False

N, M = map(int, input().strip().split())
dist = [INF] * (N+1)
edges = []

for _ in range(M):
    A, B, C = map(int, input().strip().split())
    edges.append([A, B, C])

negative_cycle = bf(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, N+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])