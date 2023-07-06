# BOJ 알고리즘 캠프에는 총 N명이 참가하고 있다. 사람들은 0번부터 N-1번으로 번호가 매겨져 있고, 일부 사람들은 친구이다.
#
# 오늘은 다음과 같은 친구 관계를 가진 사람 A, B, C, D, E가 존재하는지 구해보려고 한다.
#
# A는 B와 친구다.
# B는 C와 친구다.
# C는 D와 친구다.
# D는 E와 친구다.
# 위와 같은 친구 관계가 존재하는지 안하는지 구하는 프로그램을 작성하시오.

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().strip().split())
camp = [[] for _ in range(N)]
visited = [False] * N
flag = False
for _ in range(M):
    a, b = map(int, input().strip().split())
    camp[a].append(b)
    camp[b].append(a)

def DFS(v, depth):
    global flag
    visited[v] = True
    if depth == 5:
        flag = True
        return
    for i in camp[v]:
        if not visited[i]:
            visited[i] = True
            DFS(i, depth + 1)
            visited[i] = False

for i in range(N):
    DFS(i, 1)
    visited[i] = False
    if flag:
        break

if flag:
    print(1)
else:
    print(0)