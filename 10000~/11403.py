# 가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().strip().split())) for _ in range(N)]

for k in range(N):
    for a in range(N):
        for b in range(N):
            # 직접 가는 경로 or 거쳐 가는 경로
            if graph[a][b] == 1 or (graph[a][k] == 1 and graph[k][b] == 1):
                graph[a][b] = 1

for i in range(N):
    for j in range(N):
        print(graph[i][j], end = " ")
    print()