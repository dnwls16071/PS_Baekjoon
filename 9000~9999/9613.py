# 양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.

import math

t = int(input())
li = []
for _ in range(t):
    li = list(map(int, input().split()))
    result = li[1:]
    total = 0
    for a in range(len(result)-1):
        for b in range(a+1, len(result)):
            total += math.gcd(result[a], result[b])
    print(total)