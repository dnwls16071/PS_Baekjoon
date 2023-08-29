# 효빈이의 비밀 박스에는 조약돌이 N개 들어있다. 조약돌의 색상은 1부터 M까지 중의 하나이다.
#
# 비밀 박스에서 조약돌을 랜덤하게 K개 뽑았을 때, 뽑은 조약돌이 모두 같은 색일 확률을 구하는 프로그램을 작성하시오.

import math
import sys
input = sys.stdin.readline

M = int(input())
lst = list(map(int, input().strip().split()))
K = int(input())

total = math.comb(sum(lst), K)
temp = 0
for i in lst:
    temp += math.comb(i, K)
print(temp / total)