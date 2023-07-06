# 팩토리얼5란, N!의 0이 아닌 뒤 5자리를 말한다.
#
# N이 주어졌을 때, 팩토리얼5를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input())
result = 1

for i in range(2, N+1):
    result *= i
    if len(str(result)) >= 15:
        result = int(str(result)[-15:])
    while str(result)[-1] == "0":
        result = int(str(result)[:-1])

N = str(result)[-5:]
print(N)