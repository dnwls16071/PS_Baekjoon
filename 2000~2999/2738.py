# N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

A = []
B = []

for i in range(N):
    A.append(list(map(int ,input().strip().split())))

for i in range(N):
    B.append(list(map(int, input().strip().split())))

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end = " ")
    print()