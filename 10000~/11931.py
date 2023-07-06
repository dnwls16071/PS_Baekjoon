# N개의 수가 주어졌을 때, 이를 내림차순으로 정렬하는 프로그램을 작성하시오.

import sys

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst.append(int(input()))

lst.sort(reverse=True)
for i in lst:
    print(i)