# 때는 2040년, 이민혁은 우주에 자신만의 왕국을 만들었다. 왕국은 N개의 행성으로 이루어져 있다. 민혁이는 이 행성을 효율적으로 지배하기 위해서 행성을 연결하는 터널을 만들려고 한다.
#
# 행성은 3차원 좌표위의 한 점으로 생각하면 된다. 두 행성 A(xA, yA, zA)와 B(xB, yB, zB)를 터널로 연결할 때 드는 비용은 min(|xA-xB|, |yA-yB|, |zA-zB|)이다.
#
# 민혁이는 터널을 총 N-1개 건설해서 모든 행성이 서로 연결되게 하려고 한다. 이때, 모든 행성을 터널로 연결하는데 필요한 최소 비용을 구하는 프로그램을 작성하시오.

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

N = int(input())
parent = [0] * (N+1)
edges = []
result = 0

for i in range(1, N+1):
    parent[i] = i

x_planet = []
y_planet = []
z_planet = []
for i in range(1, N+1):
    x, y, z = map(int, input().strip().split())
    x_planet.append([x, i])
    y_planet.append([y, i])
    z_planet.append([z, i])

x_planet.sort()
y_planet.sort()
z_planet.sort()
for i in range(N-1):
    edges.append([abs(x_planet[i+1][0] - x_planet[i][0]), x_planet[i][1], x_planet[i+1][1]])
    edges.append([abs(y_planet[i+1][0] - y_planet[i][0]), y_planet[i][1], y_planet[i+1][1]])
    edges.append([abs(z_planet[i+1][0] - z_planet[i][0]), z_planet[i][1], z_planet[i+1][1]])
edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)