# N*M크기의 행렬 A와 M*K크기의 행렬 B가 주어졌을 때, 두 행렬을 곱하는 프로그램을 작성하시오.

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

B = []
M, K = map(int, input().split())
for _ in range(M):
    B.append(list(map(int, input().split())))

C = [[0] * K for _ in range(N)]
for n in range(N):
    for k in range(K):
        for m in range(M):
            C[n][k] += A[n][m] * B[m][k]

for a in range(N):
    for b in range(K):
        print(C[a][b], end = " ")
    print("")