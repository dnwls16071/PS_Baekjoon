# 0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.
#
# 행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
first_matrix = [list(input()) for _ in range(N)]
second_matrix = [list(input()) for _ in range(N)]

def reverse(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            if first_matrix[i][j] == "0":
                first_matrix[i][j] = "1"
            else:
                first_matrix[i][j] = "0"

def check():
    for i in range(N):
        for j in range(M):
            if first_matrix[i][j] != second_matrix[i][j]:
                return False
    return True

cnt = 0
for i in range(N-2):
    for j in range(M-2):
        if first_matrix[i][j] != second_matrix[i][j]:
            reverse(i, j)
            cnt += 1

if check():
    print(cnt)
else:
    print(-1)