# 월드컵 축구의 응원을 위한 모임에서 회장을 선출하려고 한다. 이 모임은 만들어진지 얼마 되지 않았기 때문에 회원 사이에 서로 모르는 사람도 있지만, 몇 사람을 통하면 모두가 서로 알 수 있다. 각 회원은 다른 회원들과 가까운 정도에 따라 점수를 받게 된다.
#
# 예를 들어 어느 회원이 다른 모든 회원과 친구이면, 이 회원의 점수는 1점이다. 어느 회원의 점수가 2점이면, 다른 모든 회원이 친구이거나 친구의 친구임을 말한다. 또한 어느 회원의 점수가 3점이면, 다른 모든 회원이 친구이거나, 친구의 친구이거나, 친구의 친구의 친구임을 말한다.
#
# 4점, 5점 등은 같은 방법으로 정해진다. 각 회원의 점수를 정할 때 주의할 점은 어떤 두 회원이 친구사이이면서 동시에 친구의 친구사이이면, 이 두사람은 친구사이라고 본다.
#
# 회장은 회원들 중에서 점수가 가장 작은 사람이 된다. 회장의 점수와 회장이 될 수 있는 모든 사람을 찾는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
graph = [[INF] * (N+1) for _ in range(N+1)]
while True:
    a, b = map(int, input().strip().split())
    if a == -1 and b == -1:
        break
    graph[a][b] = 1
    graph[b][a] = 1

for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b:
            graph[a][b] = 0

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]

lst = []
for i in range(1, N+1):
    lst.append(max(graph[i][1:]))

# 점수가 가장 낮은 사람이 회장 후보로 선출
min_score = min(lst)
answer = []
print(min_score, lst.count(min_score))
for idx, val in enumerate(lst):
    if val == min_score:
        answer.append(idx+1)
print(*answer)