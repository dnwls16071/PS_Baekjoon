# n × n의 크기의 대나무 숲이 있다. 욕심쟁이 판다는 어떤 지역에서 대나무를 먹기 시작한다. 그리고 그 곳의 대나무를 다 먹어 치우면 상, 하, 좌, 우 중 한 곳으로 이동을 한다. 그리고 또 그곳에서 대나무를 먹는다. 그런데 단 조건이 있다. 이 판다는 매우 욕심이 많아서 대나무를 먹고 자리를 옮기면 그 옮긴 지역에 그 전 지역보다 대나무가 많이 있어야 한다.
#
# 이 판다의 사육사는 이런 판다를 대나무 숲에 풀어 놓아야 하는데, 어떤 지점에 처음에 풀어 놓아야 하고, 어떤 곳으로 이동을 시켜야 판다가 최대한 많은 칸을 방문할 수 있는지 고민에 빠져 있다. 우리의 임무는 이 사육사를 도와주는 것이다. n × n 크기의 대나무 숲이 주어져 있을 때, 이 판다가 최대한 많은 칸을 이동하려면 어떤 경로를 통하여 움직여야 하는지 구하여라.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(y, x):
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        else:
            if forest[y][x] < forest[ny][nx]:
                dp[y][x] = max(dp[y][x], DFS(ny, nx) + 1)
    return dp[y][x]

n = int(input())
forest = []
for _ in range(n):
    forest.append(list(map(int, input().strip().split())))

dp = [[-1] * n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
Max = 0
for i in range(n):
    for j in range(n):
        Max = max(Max, DFS(i, j))
print(Max)
