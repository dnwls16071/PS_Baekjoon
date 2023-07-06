# 2차원 배열이 주어졌을 때 (i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합을 구하는 프로그램을 작성하시오. 배열의 (i, j) 위치는 i행 j열을 나타낸다.

import sys

N, M = map(int, sys.stdin.readline().split())
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

answer = 0
K = int(input())
for _ in range(K):
    i, j, x, y = map(int, sys.stdin.readline().strip().split())
    for a in range(i-1, x):
        for b in range(j-1, y):
            answer += arr[a][b]
    print(answer)
    answer = 0