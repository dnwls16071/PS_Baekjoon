# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for i in range(N)]
lst.sort()

for i in lst:
    print(i)