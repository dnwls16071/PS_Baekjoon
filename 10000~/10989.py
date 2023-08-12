# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

n = int(input())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(input())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)