# 오늘도 서준이는 너비 우선 탐색(BFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.
#
# N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다. 정점 R에서 시작하여 너비 우선 탐색으로 만들어 지는 트리를 너비 우선 탐색 트리라고 하자. 너비 우선 탐색 트리에 있는 i번 노드의 깊이(depth)를 di라고 하자. 시작 정점 R의 깊이는 0이고 방문 되지 않는 노드의 깊이는 -1이다. 정점 R에서 시작하여 너비 우선 탐색으로 노드를 방문할 경우 i번 노드의 방문 순서를 ti라고 하자. 시작 정점의 방문 순서는 1이고 시작 정점에서 방문할 수 없는 노드는 0이다. 모든 노드에 대한 di × ti 값의 합을 구해보자.
#
# 너비 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 오름차순으로 방문한다.
#
# bfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
#     for each v ∈ V - {R}
#         visited[v] <- NO;
#     visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
#     enqueue(Q, R);  # 큐 맨 뒤에 시작 정점 R을 추가한다.
#     while (Q ≠ ∅) {
#         u <- dequeue(Q);  # 큐 맨 앞쪽의 요소를 삭제한다.
#         for each v ∈ E(u)  # E(u) : 정점 u의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
#             if (visited[v] = NO) then {
#                 visited[v] <- YES;  # 정점 v를 방문 했다고 표시한다.
#                 enqueue(Q, v);  # 큐 맨 뒤에 정점 v를 추가한다.
#             }
#     }
# }

from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(len(graph)):
    graph[i].sort()

# 노드의 깊이
visited = [-1] * (N+1)
# 노드의 방문 순서 → idx로 구현
sequence = [0] * (N+1)
idx = 1

def BFS(x):
    global idx
    queue = deque()
    queue.append(x)
    visited[x] = 0      # 시작 정점의 깊이는 0, 방문 되지 않은 노드의 깊이는 -1
    sequence[x] = 1     # 시작 정점의 방문 순서는 1, 방문할 수 없는 노드는 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                idx += 1
                visited[i] = visited[v] + 1
                sequence[i] = idx
                queue.append(i)

BFS(R)
Sum = 0
for i in range(N+1):
    Sum += visited[i] * sequence[i]
print(Sum)