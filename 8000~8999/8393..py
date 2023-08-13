# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

n = int(input())

print(n * (n+1) // 2)