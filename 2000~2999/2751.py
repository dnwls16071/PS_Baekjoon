# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input())
number = []
for _ in range(N):
    number.append(int(input()))

number.sort()
for i in number:
    print(i)