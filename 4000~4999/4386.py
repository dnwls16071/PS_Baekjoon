# 도현이는 우주의 신이다. 이제 도현이는 아무렇게나 널브러져 있는 n개의 별들을 이어서 별자리를 하나 만들 것이다. 별자리의 조건은 다음과 같다.
#
# 별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태이다.
# 모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있어야 한다.
# 별들이 2차원 평면 위에 놓여 있다. 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때, 별자리를 만드는 최소 비용을 구하시오.

import math
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

n = int(input())
parent = [0] * (n+1)
stars = []
edges = []
result = 0

for i in range(1, n+1):
    parent[i] = i

for _ in range(n):
    x, y = map(float, input().strip().split())
    stars.append([x, y])

for i in range(n-1):
    for j in range(i+1, n):
        distance = math.sqrt((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2)
        edges.append([distance, i, j])
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print("{:.2f}".format(result))
