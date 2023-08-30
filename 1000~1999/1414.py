# 다솜이는 불우이웃 돕기 활동을 하기 위해 무엇을 할지 생각했다. 마침 집에 엄청나게 많은 랜선이 있다는 것을 깨달았다. 마침 랜선이 이렇게 많이 필요 없다고 느낀 다솜이는 랜선을 지역사회에 봉사하기로 했다.
#
# 다솜이의 집에는 N개의 방이 있다. 각각의 방에는 모두 한 개의 컴퓨터가 있다. 각각의 컴퓨터는 랜선으로 연결되어 있다. 어떤 컴퓨터 A와 컴퓨터 B가 있을 때, A와 B가 서로 랜선으로 연결되어 있거나, 또 다른 컴퓨터를 통해서 연결이 되어있으면 서로 통신을 할 수 있다.
#
# 다솜이는 집 안에 있는 N개의 컴퓨터를 모두 서로 연결되게 하고 싶다.
#
# N개의 컴퓨터가 서로 연결되어 있는 랜선의 길이가 주어질 때, 다솜이가 기부할 수 있는 랜선의 길이의 최댓값을 출력하는 프로그램을 작성하시오.

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
lst = [list(input().strip()) for _ in range(N)]
parent = [0] * (N+1)
edges = []
result = 0

# 부모 테이블을 자기 자신으로 초기화
for i in range(1, N+1):
    parent[i] = i

for a in range(N):
    for b in range(N):
        if lst[a][b] == "0":
            edges.append([0, a, b])
        else:
            if 'a' <= lst[a][b] <= 'z':
                cost = ord(lst[a][b]) - 96
                result += cost
            elif 'A' <= lst[a][b] <= 'Z':
                cost = ord(lst[a][b]) - 38
                result += cost
            if a != b:
                edges.append([cost, a, b])
edges.sort()
for edge in edges:
    cost, a, b = edge
    # 랜선이 없음
    if cost == 0:
        continue
    # 두 노드의 부모가 같지 않은 경우에만 연결을 수행
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        # 해당 비용 차감
        result -= cost

for i in range(1, N+1):
    find_parent(parent, i)

# 크루스칼 알고리즘을 돌고 난 후 모든 노드에 대해서 find를 수행한 후에 양 옆의 노드 부모가 같지 않다면>
# 연결이 되지 않은 경우이므로 이런 경우 -1을 출력
for i in range(N-1):
    if parent[i] != parent[i+1]:
        print(-1)
        sys.exit(0)
print(result)