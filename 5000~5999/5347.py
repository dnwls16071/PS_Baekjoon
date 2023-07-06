# 두 수 a와 b가 주어졌을 때, a와 b의 최소 공배수를 구하는 프로그램을 작성하시오.

import sys
import math

n = int(input())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(math.lcm(a, b))