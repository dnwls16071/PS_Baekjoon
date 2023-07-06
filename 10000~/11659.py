# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

import sys

N, M = map(int, sys.stdin.readline().strip().split())
li = list(map(int, sys.stdin.readline().strip().split()))

prefix_sum = [0]
sum_val = 0
for i in li:
    sum_val += i
    prefix_sum.append(sum_val)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    print(prefix_sum[j] - prefix_sum[i-1])