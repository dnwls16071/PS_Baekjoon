# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().strip().split()))
lst.sort()
v = int(input())

start = bisect_left(lst, v)
end = bisect_right(lst, v)
print(end - start)