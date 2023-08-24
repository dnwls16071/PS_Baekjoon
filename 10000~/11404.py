# n(2 ≤ n ≤ 100)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다. 각 버스는 한 번 사용할 때 필요한 비용이 있다.
#
# 모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
# n개의 도시(n * n)
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
    # a : 시작 도시, b : 도착 도시, c : 한 번 타는데 필요한 비용
    a, b, c = map(int, input().strip().split())
    # a → b를 연결하는 노선은 하나가 아닐 수 있다.(따라서, 최솟값으로 갱신을 해줘야한다.)
    graph[a][b] = min(graph[a][b], c)

# 점화식에 따라 플로이드-워셜 알고리즘을 진행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end = " ")
        else:
            print(graph[a][b], end = " ")
    print()