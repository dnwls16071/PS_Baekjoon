# 명우기업은 2008년부터 택배 사업을 새로이 시작하기로 하였다. 우선 택배 화물을 모아서 처리하는 집하장을 몇 개 마련했지만, 택배 화물이 각 집하장들 사이를 오갈 때 어떤 경로를 거쳐야 하는지 결정하지 못했다. 어떤 경로를 거칠지 정해서, 이를 경로표로 정리하는 것이 여러분이 할 일이다.
#
#
#
# 예시된 그래프에서 굵게 표시된 1, 2, 3, 4, 5, 6은 집하장을 나타낸다. 정점간의 간선은 두 집하장간에 화물 이동이 가능함을 나타내며, 가중치는 이동에 걸리는 시간이다. 이로부터 얻어내야 하는 경로표는 다음과 같다.
#
#
#
# 경로표는 한 집하장에서 다른 집하장으로 최단경로로 화물을 이동시키기 위해 가장 먼저 거쳐야 하는 집하장을 나타낸 것이다. 예를 들어 4행 5열의 6은 4번 집하장에서 5번 집하장으로 최단 경로를 통해 가기 위해서는 제일 먼저 6번 집하장으로 이동해야 한다는 의미이다.
#
# 이와 같은 경로표를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().strip().split())
graph = [[INF] * (n+1) for _ in range(n+1)]     # 최단거리 정보
result = [[0] * (n+1) for _ in range(n+1)]      # 집하장 정보

for _ in range(m):
    # 집하장간 경로와 두 집하장을 오가는데 필요한 시간(가중치)
    a, b, c = map(int, input().strip().split())
    # 양방향이므로 a → b : c, b → a : c
    graph[a][b] = c
    graph[b][a] = c
    # 거치는 집하장 번호를 저장
    # a → b : b를 경유하므로 b를 저장
    # b → a : a를 경유하므로 a를 저장
    result[a][b] = b
    result[b][a] = a

# 자기 자신에서 자기 자신으로 가는 경우는 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 직접 이동하는 경우와 다른 집하장을 경유해서 가는 경우를 비교해서 최단경로를 저장
# 만약 다른 집하장을 경유해서 이동한 경우가 최단경로가 된다면 경유한 k를 집하장 번호에 저장
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                result[a][b] = result[a][k]

# 자기 자신에서 자기 자신으로 가는 경우는 -을 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            result[a][b] = "-"
            print(result[a][b], end = " ")
        else:
            print(result[a][b], end = " ")
    print()