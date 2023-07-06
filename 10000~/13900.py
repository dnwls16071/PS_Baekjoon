# N개의 정수 중 서로 다른 위치의 두 수를 뽑는 모든 경우의 두 수의 곱의 합을 구하라.
#
# 예를 들어 N = 3이고 주어진 정수가 2, 3, 4일 때, 두 수를 뽑는 모든 경우는 (2, 3), (2, 4), (3, 4)이며 이때 각각의 곱은 6, 8, 12이다. 따라서 총합은 26이다.

#1
from itertools import combinations

N = int(input())
li = list(map(int, input().split()))

total = 0
for i in combinations(li, 2):
    result = 1
    for j in range(len(i)):
        result *= i[j]
    total += result
print(total)

#2
N = int(input())
li = list(map(int, input().split()))

result = sum(li)
total = 0
for i in li:
    result -= i
    total += result * i
print(total)