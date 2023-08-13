# 두 정수 A와 B가 주어졌을 때, 두 수의 곱을 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

A, B = map(int, input().strip().split())

print(A * B)