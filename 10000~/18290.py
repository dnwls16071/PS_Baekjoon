# 크기가 N×M인 격자판의 각 칸에 정수가 하나씩 들어있다. 이 격자판에서 칸 K개를 선택할 것이고, 선택한 칸에 들어있는 수를 모두 더한 값의 최댓값을 구하려고 한다. 단, 선택한 두 칸이 인접하면 안된다. r행 c열에 있는 칸을 (r, c)라고 했을 때, (r-1, c), (r+1, c), (r, c-1), (r, c+1)에 있는 칸이 인접한 칸이다.

import sys
input = sys.stdin.readline

N, M, K = map(int, input().strip().split())
board = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

max_value = -10001 * (N * M)
def DFS(x, y, cnt, sum):
    global max_value
    if cnt == K:
        max_value = max(max_value, sum)
        return
    for a in range(N):
        for b in range(M):
            if visited[a][b] == False:
                visited[a][b] = True
                DFS(x, y, cnt+1, sum)
                visited[a][b] = 0

