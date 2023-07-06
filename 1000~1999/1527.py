# 은민이는 4와 7을 좋아하고, 나머지 숫자는 싫어한다. 금민수는 어떤 수가 4와 7로만 이루어진 수를 말한다.
#
# A와 B가 주어졌을 때, A보다 크거나 같고, B보다 작거나 같은 자연수 중에 금민수인 것의 개수를 출력하는 프로그램을 작성하시오.

import itertools
import sys
input = sys.stdin.readline

A, B = map(int, input().strip().split())
x = len(str(A))
y = len(str(B))

cnt = 0
for i in range(x, y+1):
    res = list(itertools.product([4, 7], repeat=i))
    for j in res:
        j = int(''.join(map(str, j)))
        if A <= j <= B:
            cnt += 1
print(cnt)
