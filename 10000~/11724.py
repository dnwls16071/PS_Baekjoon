# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(start, depth):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            DFS(i, depth+1)


N, M = map(int, input().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)
answer = 0

for i in range(1 ,N+1):
    if not visited[i]:
        DFS(i, 0)
        answer += 1
print(answer)