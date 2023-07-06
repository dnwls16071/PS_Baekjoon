# N!의 값을 계산한 후에, 0이 아닌 가장 낮은 자리 수를 구하시오.
#
# 예를 들어, 4! = 24 이기 때문에, 0이 아닌 가장 낮은 자리 수는 4이다. 또, 5! = 120이기 때문에, 0이 아닌 가장 낮은 자리 수는 2 이다.

import math
import sys
input = sys.stdin.readline

N = int(input())

res = str(math.factorial(N))
while True:
    res = res[::-1]
    for i in res:
        if i == "0":
            continue
        else:
            print(i)
            sys.exit(0)