# 소수 마을들의 주민들은 매우 특이한 규칙을 준수한다. 규칙은 바로 “가고 싶은 위치까지의 거리가 소수일 경우에만 간다”라는 것이다. 소수 마을의 주민 승욱이는 소수 마을에서 멀리 떨어진 A마을에 볼일이 있어 그곳까지 가야한다. 소수 마을에서 A마을까지의 단숨에 가고 싶지만 안타깝게도 두 마을의 거리는 소수가 아닐 경우에는 그럴 수가 없다. 그럴 경우에는 다른 마을들을 경유하여 가야한다. (경유하는 마을도 현재 위치에서의 거리가 소수일 경우에만 갈 수 있다.) 소수 마을과 경유할 수 있는 마을들, 그리고 A마을의 위치가 좌표평면 상으로 주어질 때, 승욱이가 소수 마을의 규칙을 준수하여 A마을로 갈 수 있는 최단의 길을 찾는 것을 도와주자. 소수 판정을 위해 마을 간의 거리는 정수 부분만으로 취급한다. 예를 들어, 거리가 3.1415라면 이를 버림하여 3만 취급한다.

import heapq
import sys
import math
input = sys.stdin.readline
INF = int(1e9)

# 에라토스테네스의 체로 소수를 거르기
arr = [True] * 10001
arr[0] = False
arr[1] = False
for i in range(2, int(10001**0.5)+1):
    if arr[i]:
        for j in range(2*i, 10001, i):
            arr[j] = False

# 시작 좌표, 도착 좌표
graph = []
X1, Y1, X2, Y2 = map(int, input().strip().split())
N = int(input())
graph.append([X1, Y1])
graph.append([X2, Y2])
# 경유 좌표
for _ in range(N):
    a, b = map(int, input().strip().split())
    graph.append([a, b])

# 에라토스테네스의 체에 의한 소수 판별 함수
def is_prime(x):
    if arr[x]:
        return True
    else:
        return False

# 다익스트라 함수(좌표의 개념 → 값을 어떻게 처리해야할지 많은 고민...)
def dijkstra(start):
    distance = [INF] * (N+2)
    distance[0] = 0
    q = []
    heapq.heappush(q, [0, 0])
    while q:
        dist, now = heapq.heappop(q)
        now_x, now_y = graph[now]
        if distance[now] < dist:
            continue
        for i in range(N+2):
            next_x, next_y = graph[i]
            temp = int(math.sqrt((now_x - next_x) ** 2 + (now_y - next_y) ** 2))
            if is_prime(temp) and distance[i] > dist + temp:
                distance[i] = dist + temp
                heapq.heappush(q, [dist + temp, i])
    return distance

res = dijkstra(0)
if res[1] == INF:
    print(-1)
else:
    print(res[1])