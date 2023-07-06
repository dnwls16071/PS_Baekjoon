# 정수 N을 정수 D로 나눴을 때의 몫을 Q, 나머지를 R이라고 하면 항등식 R = N - Q×D가 성립한다.
#
# n개의 정수로 된 수열이 있을 때, 모든 정수를 한 정수 D로 나눴을 때 나머지가 같아지는 경우가 있다. 그리고 수열에 따라서는 이러한 정수 D가 여러 개 존재할 수 있다.
#
# n개의 정수로 된 수열이 주어졌을 때, 가장 큰 D를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().strip().split()))
Min = min(lst)

def GCD(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

result = []
for i in range(N):
    if lst[i] != Min:
        result.append(lst[i] - Min)

temp = result[0]
for i in range(1, len(result)):
    temp = GCD(temp, result[i])
print(temp)