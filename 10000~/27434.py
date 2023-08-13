# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

def recursive(N):
    if N == 0 or N == 1:
        return 1
    return N * recursive(N-1)

print(recursive(N))