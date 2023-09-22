# A[1], A[2], ..., A[N]의 N개의 정수가 저장되어 있는 배열이 있다. 이 배열 A의 부분합이란 1 ≤ i ≤ j ≤ N인 정수 i와 j에 대해 A[i]부터 A[j]까지의 합을 말한다.
#
# N과 A[1], A[2], ..., A[N]이 주어졌을 때, 이러한 N×(N+1)/2개의 부분합 중 합이 K인 것이 몇 개나 있는지를 구하는 프로그램을 작성하시오.

# 순차적으로 누적합을 구하면서 k가 되기위해 빼야하는 수가 이전에 구한 누적합이 있는지 체크를 해서 정답을 구했다.

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))
prefix_sum = {0 : 1}

tot = 0
ans = 0
for i in nums:
    tot += i
    if tot - M in prefix_sum.keys():
        ans += prefix_sum[tot - M]
    if tot in prefix_sum:
        prefix_sum[tot] += 1
    else:
        prefix_sum[tot] = 1
print(ans)