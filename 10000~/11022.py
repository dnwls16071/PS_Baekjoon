# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

T = int(input())
for i in range(1, T+1):
    A, B = map(int, input().strip().split())
    print("Case #" + str(i) + ": " + str(A) + " + " + str(B) + " = " + str(A+B))