# 수열 S가 주어졌을 때, 수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수를 구하는 프로그램을 작성하시오.
#
# 예를 들어, S = [5, 1, 2]인 경우에 1, 2, 3(=1+2), 5, 6(=1+5), 7(=2+5), 8(=1+2+5)을 만들 수 있다. 하지만, 4는 만들 수 없기 때문에 정답은 4이다.

from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input().strip())
li = list(map(int, input().strip().split()))

result = []
for i in range(1, N+1):
    temp = list(combinations(li, i))
    for t in temp:
        result.append(sum(t))

result = list(set(result))
result.sort()
j = 1
for i in result:
    if j != i:
        break
    j += 1
print(j)