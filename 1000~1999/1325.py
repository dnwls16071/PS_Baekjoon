# 해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다. 김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.
#
# 이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.
#
# 이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

# from collections import deque
# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().strip().split())
# graph = [[] for _ in range(N+1)]
# for _ in range(M):
#     A, B = map(int, input().strip().split())
#     graph[B].append(A)
#
# def BFS(start):
#     queue = deque()
#     queue.append(start)
#     visited = [False] * (N+1)
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         for i in graph[v]:
#             if not visited[i]:
#                 visited[i] = True
#                 queue.append(i)
#     return visited.count(True)
#
# hacking = [0] * (N+1)
# for i in range(1, N+1):
#     hacking[i] = BFS(i)
#
# Max = max(hacking)
# for i in range(N+1):
#     if hacking[i] == Max:
#         print(i, end = " ")

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().strip().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().strip().split())
    graph[B].append(A)


def DFS(start, visited):
    global depth
    visited[start][0] = True
    for i in graph[start]:
        if not visited[i][0]:
            depth += 1
            DFS(i, visited)
    return depth


visited = [[False, 0] for _ in range(N + 1)]
hacking = [0] * (N + 1)
for i in range(1, N + 1):
    depth = 1
    visited = [[False, 0] for _ in range(N + 1)]
    hacking[i] = DFS(i, visited)

Max = max(hacking)
for i in range(1, N+1):
    if hacking[i] == Max:
        print(i, end = " ")
