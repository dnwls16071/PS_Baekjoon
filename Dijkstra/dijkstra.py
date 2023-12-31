import sys
input = sys.stdin.readline
INF = int(1e9)	# 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().strip().split())
# 시작 노드 번호를 입력하기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 무한으로 초기화
distance = [INF] * (n+1)


# 모든 간선 정보를 입력받기
for _ in range(m):
	a, b, c = map(int, input().strip().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라고 설정
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
	min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드
    for i in range(1, n+1):
    	# 최단 거리가 최솟값을 가지면서 방문한 적이 없는 노드라면?
    	if distance[i] < min_value and not visited[i]:
	        min_value = distance[i]
    	    index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
    	distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
    	now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
    	    cost = distance[i] + j[1]
            if cost < distance[j[0]]:
            	distance[j[0]] = cost

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
	if distance[i] == INF:
    	print("INFINITY")
    else:
	    print(distance[i])


import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)	# 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
V, E = map(int, input().strip().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(V+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (V+1)

# 모든 간선 정보를 입력받기
for _ in range(E):
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    a, b, c = map(int, input().strip().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드에서 시작 노드로 가는 비용은 0이다.
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # 큐가 비어있지않으면?
    while q:
    	# 최단 거리가 가장 짧은 노드에 대한 (거리, 노드 번호) 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있다면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            # graph의 정보 주의하자!
            # graph[a] = (b, c)	→ a에서 b로 가는 비용이 c다.
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
