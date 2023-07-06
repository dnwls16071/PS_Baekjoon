# N개의 수 A1, A2, ..., AN이 입력으로 주어진다. 총 M개의 구간 i, j가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

import sys

N = int(input())
A_li = list(map(int, sys.stdin.readline().strip().split()))

prefix_sum = [0]
sum = 0
for i in range(N):
    sum += A_li[i]
    prefix_sum.append(sum)

M = int(input())
for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    print(prefix_sum[j] - prefix_sum[i-1])