# 세준이는 정수 S와 K가 주어졌을 때, 합이 S인 K개의 양의 정수를 찾으려고 한다. 만약 여러개일 경우 그 곱을 가능한 최대로 하려고 한다.
#
# 가능한 최대의 곱을 출력한다.
#
# 만약 S=10, K=3이면, 3,3,4는 곱이 36으로 최대이다.

import sys
input = sys.stdin.readline

S, K = map(int, input().strip().split())
arr = [S // K for i in range(K)]

while True:
    if sum(arr) == S:
        break
    else:
        arr[-1] += 1
        arr.sort(reverse = True)

result = 1
for i in arr:
    result *= i
print(result)