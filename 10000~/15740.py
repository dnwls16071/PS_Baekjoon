# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

A, B = map(int, input().strip().split())
print(A + B)