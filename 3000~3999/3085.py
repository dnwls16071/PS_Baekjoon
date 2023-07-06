# 상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.
#
# 가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.
#
# 사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

N = int(input())
board = []
max_count = 0
for _ in range(N):
    board.append(list(input()))

def width_search():
    global max_count
    for i in range(N):
        width_cnt = 1
        for j in range(N-1):
            if board[i][j] == board[i][j+1]:
                width_cnt += 1
                max_count = max(max_count, width_cnt)
            else:
                width_cnt = 1

def height_search():
    global max_count
    for i in range(N):
        height_cnt = 1
        for j in range(N-1):
            if board[j][i] == board[j+1][i]:
                height_cnt += 1
                max_count = max(max_count, height_cnt)
            else:
                height_cnt = 1

for i in range(N):
    width_cnt = 1
    for j in range(N-1):
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        width_search()
        height_search()
        board[i][j+1], board[i][j] = board[i][j], board[i][j+1]
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
        width_search()
        height_search()
        board[j+1][i], board[j][i] = board[j][i], board[j+1][i]
print(max_count)