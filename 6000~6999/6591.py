# n개의 원소 중에서 k개를 순서 없이 선택하는 방법의 수는 몇 가지 일까?

import sys
input = sys.stdin.readline

def nCk(N, K):
    if K == 0:
        return 1
    if K > N - K:
        K = N - K

    N_val = 1
    K_val = 1
    for i in range(K):
        N_val *= (N-i)
        K_val *= (K-i)

    return N_val // K_val

while True:
    A, B = map(int, input().strip().split())
    if A == 0 and B == 0:
        break
    print(nCk(A, B))