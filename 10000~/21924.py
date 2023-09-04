# 채완이는 신도시에 건물 사이를 잇는 양방향 도로를 만들려는 공사 계획을 세웠다.
#
# 공사 계획을 검토하면서 비용이 생각보다 많이 드는 것을 확인했다.
#
# 채완이는 공사하는 데 드는 비용을 아끼려고 한다.
#
# 모든 건물이 도로를 통해 연결되도록 최소한의 도로를 만들려고 한다.
#
#
#
# 위 그림에서 건물과 직선으로 표시된 도로, 해당 도로를 만들 때 드는 비용을 표시해놓은 지도이다.
#
#
#
# 그림에 있는 도로를 다 설치할 때 드는 비용은 62이다. 모든 건물을 연결하는 도로만 만드는 비용은 27로 절약하는 비용은 35이다.
#
# 채완이는 도로가 너무 많아 절약되는 금액을 계산하는 데 어려움을 겪고 있다.
#
# 채완이를 대신해 얼마나 절약이 되는지 계산해주자.

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

N, M = map(int, input().strip().split())
parent = [0] * (N+1)
edges = []
result = 0
for _ in range(M):
    a, b, c = map(int, input().strip().split())
    edges.append([c, a, b])
    result += c
edges.sort()

for i in range(1, N+1):
    parent[i] = i

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는다면? → 간선을 연결
    # 현재 문제에서 구하고자 하는 것은 절약이 되는 금액을 계산하는 것이다.
    # 따라서, MST에 포함되는 간선들의 합을 총합에서 뺴주면 절약이 되는 금액이 나온다.
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result -= cost

# 모든 도시가 연결이 되는 경우는 부모 노드의 번호가 두 가지만 나오는 경우이다.
# 그 이상 나오게 된다면 모든 건물이 연결되지않았다는 것을 알 수 있다.
tmp = 0
for i in range(1, N+1):
    if parent[i] == i:
        tmp += 1

if tmp >= 2:
    print(-1)
else:
    print(result)