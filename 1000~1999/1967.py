# 트리(tree)는 사이클이 없는 무방향 그래프이다. 트리에서는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다. 트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것이다. 이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.
#
#
#
# 이런 두 노드 사이의 경로의 길이를 트리의 지름이라고 한다. 정확히 정의하자면 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다.
#
# 입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하는 프로그램을 작성하시오. 아래와 같은 트리가 주어진다면 트리의 지름은 45가 된다.
#
#
#
# 트리의 노드는 1부터 n까지 번호가 매겨져 있다.

# 트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우를 찾기
# 루트 노드 - 리프 노드 가중치의 합을 비교

# from collections import deque
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# graph = [[] for _ in range(n+1)]
# for _ in range(n-1):
#     a, b, c = map(int, input().strip().split())
#     graph[a].append([b, c])
#     graph[b].append([a, c])
#
# # 시작점, 누적합, 배열
# def BFS(start, prefix_sum, result):
#     queue = deque()
#     queue.append([start, prefix_sum])
#     while queue:
#         s, p = queue.popleft()
#         for i in graph[s]:
#             node, cost = i
#             if result[node] == -1:
#                 queue.append([node, cost])
#                 result[node] = cost + result[s]
#     return result
#
# result = [-1] * (n+1)
# result[1] = 0
# BFS(1, 0, result)
# num = result.index(max(result))
#
# result = [-1] * (n+1)
# result[num] = 0
# BFS(num, 0, result)
# print(max(result))

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().strip().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

def DFS(start, prefix_sum, result):
    for i in graph[start]:
        node, cost = i
        if result[node] == -1:
            result[node] = prefix_sum + cost
            DFS(node, prefix_sum + cost, result)
    return result

result = [-1] * (n+1)
result[1] = 0
DFS(1, 0, result)
num = result.index(max(result))

result = [-1] * (n+1)
result[num] = 0
DFS(num, 0, result)
print(max(result))