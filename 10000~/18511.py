# N보다 작거나 같은 자연수 중에서, 집합 K의 원소로만 구성된 가장 큰 수를 출력하는 프로그램을 작성하시오. K의 모든 원소는 1부터 9까지의 자연수로만 구성된다.
#
# 예를 들어 N=657이고, K={1, 5, 7}일 때 답은 577이다.

from itertools import product
import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
lst = list(map(int, input().strip().split()))
length = len(str(N))

res = []
while True:
    temp = list(product(lst, repeat = length))
    for i in temp:
        i = int(''.join(map(str, i)))
        if i <= N:
            res.append(i)
    if len(res) >= 1:
        print(max(res))
        break
    else:
        length -= 1