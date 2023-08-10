# 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N, S = map(int, input().strip().split())
lst = list(map(int, input().strip().split())) + [0 for _ in range(100001)]

left = 0
right = 0
partsum = lst[0]
min_length = float('INF')

while right <= N:
    if partsum >= S:
        if min_length > right - left + 1:
            min_length = right - left + 1
        partsum -= lst[left]
        left += 1
    else:
        right += 1
        partsum += lst[right]

if min_length == float('INF'):
    print(0)
else:
    print(min_length)