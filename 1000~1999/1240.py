# N(2≤N≤1,000)개의 노드로 이루어진 트리가 주어지고 M(M≤1,000)개의 두 노드 쌍을 입력받을 때 두 노드 사이의 거리를 출력하라.

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v, w = map(int, input().strip().split())
    # 가중치가 있는 트리 구조이므로 튜플 형태로 가중치 값도 같이 넣어준다.
    graph[u].append((v, w))
    graph[v].append((u, w))

def BFS(start, find):
    queue = deque()
    queue.append((start, 0))
    visited = [False] * (N + 1)
    visited[start] = True
    while queue:
        v, d = queue.popleft()
        if v == find:
            return d
        for i, w in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append((i, d+w))

for _ in range(M):
    a, b = map(int, input().strip().split())
    print(BFS(a, b))