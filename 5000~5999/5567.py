# 상근이는 자신의 결혼식에 학교 동기 중 자신의 친구와 친구의 친구를 초대하기로 했다. 상근이의 동기는 모두 N명이고, 이 학생들의 학번은 모두 1부터 N까지이다. 상근이의 학번은 1이다.
#
# 상근이는 동기들의 친구 관계를 모두 조사한 리스트를 가지고 있다. 이 리스트를 바탕으로 결혼식에 초대할 사람의 수를 구하는 프로그램을 작성하시오.

from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
relationship = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().strip().split())
    relationship[a].append(b)
    relationship[b].append(a)


def BFS(graph, start):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        start = queue.popleft()
        for i in graph[start]:
            if not visited[i]:
                visited[i] = visited[start] + 1
                queue.append(i)
    return visited


visited = [0] * (n + 1)
BFS(relationship, 1)
friend = 0
visited = [False] * (n + 1)
li = BFS(relationship, 1)
for i in li:
    if i < 4 and i > 0:
        friend += 1
print(friend - 1)