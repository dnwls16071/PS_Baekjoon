# 두 양의 정수가 주어졌을 때, 첫 번째 수가 두 번째 수보다 큰지 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

while True:
    A, B = map(int, input().strip().split())
    if A == 0 and B == 0:
        break
    if A > B:
        print("Yes")
    else:
        print("No")