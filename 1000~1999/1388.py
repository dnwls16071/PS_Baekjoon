# 형택이는 건축가이다. 지금 막 형택이는 형택이의 남자 친구 기훈이의 집을 막 완성시켰다. 형택이는 기훈이 방의 바닥 장식을 디자인했고, 이제 몇 개의 나무 판자가 필요한지 궁금해졌다. 나무 판자는 크기 1의 너비를 가졌고, 양수의 길이를 가지고 있다. 기훈이 방은 직사각형 모양이고, 방 안에는 벽과 평행한 모양의 정사각형으로 나누어져 있다.
#
# 이제 ‘-’와 ‘|’로 이루어진 바닥 장식 모양이 주어진다. 만약 두 개의 ‘-’가 인접해 있고, 같은 행에 있다면, 두 개는 같은 나무 판자이고, 두 개의 ‘|’가 인접해 있고, 같은 열에 있다면, 두 개는 같은 나무 판자이다.
#
# 기훈이의 방 바닥을 장식하는데 필요한 나무 판자의 개수를 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
board = []
for i in range(N):
    board.append(list(input()))

cnt = 0
for i in range(N):
    pri_block = "|"
    for j in range(M):
        if board[i][j] == "-":
            if board[i][j] != pri_block:
                cnt += 1
        pri_block = board[i][j]

for i in range(M):
    pri_block = "-"
    for j in range(N):
        if board[j][i] == "|":
            if board[j][i] != pri_block:
                cnt += 1
        pri_block = board[j][i]
print(cnt)