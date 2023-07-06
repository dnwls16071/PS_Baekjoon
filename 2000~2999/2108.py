# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
#
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

import sys

N = int(input())
li = []
dict = {}
for _ in range(N):
    val = int(sys.stdin.readline().strip())
    li.append(val)

    if val not in dict:
        dict[val] = 1
    else:
        dict[val] += 1

li.sort()
dict = sorted(dict.items(), key = lambda x : (-x[1], x[0]))
start = 0
end = len(li) - 1
mid = (start + end) // 2

print(int(round(sum(li) / N, 0)))
if len(li) == 1:
    print(li[0])
else:
    print(li[mid])
if len(li) > 1 and dict[0][1] == dict[1][1]:
    print(dict[1][0])
elif len(li) > 1 and dict[0][1] != dict[1][1]:
    print(dict[0][0])
else:
    print(dict[0][0])
print(max(li) - min(li))