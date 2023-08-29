# 역사, 그 중에서도 한국사에 해박한 세준이는 많은 역사적 사건들의 전후 관계를 잘 알고 있다. 즉, 임진왜란이 병자호란보다 먼저 일어났으며, 무오사화가 기묘사화보다 먼저 일어났다는 등의 지식을 알고 있는 것이다.
#
# 세준이가 알고 있는 일부 사건들의 전후 관계들이 주어질 때, 주어진 사건들의 전후 관계도 알 수 있을까? 이를 해결하는 프로그램을 작성해 보도록 하자.

import sys
input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().strip().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().strip().split())
    graph[a][b] = 1

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][k] + graph[k][b] == 2:
                graph[a][b] = 1

s = int(input())
for _ in range(s):
    a, b = map(int, input().strip().split())
    if graph[a][b] == 1:
        print(-1)
    elif graph[b][a] == 1:
        print(1)
    elif graph[a][b] == INF:
        print(0)