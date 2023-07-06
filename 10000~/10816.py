# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

import sys

def binary_search(target, data):
    start = 0
    end = len(data)-1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return data[start:end+1].count(target)
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

N = int(input())
A_li = list(map(int, sys.stdin.readline().strip().split()))
M = int(input())
B_li = list(map(int, sys.stdin.readline().strip().split()))

A_li.sort()
dict = {}
for i in B_li:
    if i not in dict:
        dict[i] = binary_search(i, A_li)

for i in B_li:
    print(dict[i], end = " ")