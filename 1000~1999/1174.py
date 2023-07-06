# 음이 아닌 정수를 십진법으로 표기했을 때, 왼쪽에서부터 자리수가 감소할 때, 그 수를 줄어드는 수라고 한다. 예를 들어, 321와 950은 줄어드는 수이고, 322와 958은 아니다.
#
# N번째로 작은 줄어드는 수를 출력하는 프로그램을 작성하시오. 만약 그러한 수가 없을 때는 -1을 출력한다. 가장 작은 줄어드는 수가 1번째 작은 줄어드는 수이다.

from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input().strip())

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
res = []
for i in range(1, 11):
    for j in combinations(arr, i):
        j = list(j)
        j.sort(reverse=True)
        j = int(''.join(map(str, j)))
        res.append(j)

res.sort()
try:
    print(res[N-1])
except IndexError:
    print(-1)