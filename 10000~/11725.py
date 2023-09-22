# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())

tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().strip().split())
    tree[a].append(b)
    tree[b].append(a)
visited = [0] * (N+1)

def DFS(start):
    for i in tree[start]:
        if not visited[i]:
            visited[i] = start
            DFS(i)

DFS(1)
for i in range(2, N+1):
    print(visited[i])