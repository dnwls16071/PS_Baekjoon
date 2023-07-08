# 폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.
#
# 정사각형은 서로 겹치면 안 된다.
# 도형은 모두 연결되어 있어야 한다.
# 정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
# 정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있다.
#
#
#
# 아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.
#
# 테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.
#
# 테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.

import sys
input = sys.stdin.readline

# ㅏ, ㅓ, ㅗ, ㅜ 모양의 블록 DFS탐색
def DFS(x, y, idx, total):
    global ans
    if idx == 3:
        ans = max(total, ans)
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    DFS(nx, ny, idx+1, total+board[nx][ny])
                    visited[nx][ny] = False

# 나머지 모양의 블록들
def block(x, y, total):
    global ans
    block_count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            block_count += 1
            total += board[nx][ny]

    if block_count == 3:
        ans = max(ans, total)

    if block_count == 4:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            total -= board[nx][ny]
            if total > ans:
                ans = total
            total += board[nx][ny]

N, M = map(int, input().strip().split())
board = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        DFS(i, j, 0, board[i][j])
        block(i, j, board[i][j])
        visited[i][j] = False
print(ans)