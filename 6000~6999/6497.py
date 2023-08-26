# 성진이는 한 도시의 시장인데 거지라서 전력난에 끙끙댄다. 그래서 모든 길마다 원래 켜져 있던 가로등 중 일부를 소등하기로 하였다. 길의 가로등을 켜 두면 하루에 길의 미터 수만큼 돈이 들어가는데, 일부를 소등하여 그만큼의 돈을 절약할 수 있다.
#
# 그러나 만약 어떤 두 집을 왕래할 때, 불이 켜져 있지 않은 길을 반드시 지나야 한다면 위험하다. 그래서 도시에 있는 모든 두 집 쌍에 대해, 불이 켜진 길만으로 서로를 왕래할 수 있어야 한다.
#
# 위 조건을 지키면서 절약할 수 있는 최대 액수를 구하시오.

import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

while True:
    m, n = map(int, input().strip().split())
    parent = [0] * (m+1)
    edges = []
    result = 0
    if m == 0 and n == 0:
        break

    for i in range(1, m+1):
        parent[i] = i

    for _ in range(n):
        x, y, z = map(int, input().strip().split())
        edges.append([z, x, y])
    edges.sort()

    for edge in edges:
        cost, x, y = edge
        if find_parent(parent, x) != find_parent(parent, y):
            union_parent(parent, x, y)
        else:
            result += cost
    print(result)