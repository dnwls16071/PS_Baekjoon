# BOJ에서 정답이 여러가지인 경우에는 스페셜 저지를 사용한다. 스페셜 저지는 유저가 출력한 답을 검증하는 코드를 통해서 정답 유무를 결정하는 방식이다. 오늘은 스페셜 저지 코드를 하나 만들어보려고 한다.
#
# 정점의 개수가 N이고, 정점에 1부터 N까지 번호가 매겨져있는 양방향 그래프가 있을 때, DFS 알고리즘은 다음과 같은 형태로 이루어져 있다.
#
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# void dfs(int x) {
#     if (check[x] == true) {
#         return;
#     }
#     check[x] = true;
#     // x를 방문
#     for (int y : x와 인접한 정점) {
#         if (check[y] == false) {
#             dfs(y);
#         }
#     }
# }
# 이 문제에서 시작 정점은 1이기 때문에 가장 처음에 호출하는 함수는 dfs(1)이다. DFS 방문 순서는 dfs함수에서 // x를 방문 이라고 적힌 곳에 도착한 정점 번호를 순서대로 나열한 것이다.
#
# 트리가 주어졌을 때, 올바른 DFS 방문 순서인지 구해보자.

from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
# 연결리스트로 표현한 graph
for _ in range(1, N):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(sequence, start):
    element = sequence.popleft()
    if not sequence:
        print(1)
        sys.exit(0)
    visited[element] = True
    for i in range(len(graph[element])):
        if sequence[0] in graph[element] and not visited[sequence[0]]:
            DFS(sequence, sequence[0])
    return False

sequence = deque(map(int, input().strip().split()))
if sequence[0] != 1:
    print(0)
    sys.exit(0)
if not DFS(sequence, 1):
    print(0)