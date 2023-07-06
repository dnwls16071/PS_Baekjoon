# N개의 정수가 주어진다. 이때, N개의 정수를 오름차순으로 정렬하는 프로그램을 작성하시오. 같은 정수는 한 번만 출력한다.

import sys

N = int(input())
lst = list(map(int, sys.stdin.readline().strip().split()))

lst = list(set(lst))
lst.sort()

for i in lst:
    print(i, end=" ")
