# 정수 집합 S가 주어졌을때, 다음 조건을 만족하는 구간 [A, B]를 좋은 구간이라고 한다.
#
# A와 B는 양의 정수이고, A < B를 만족한다.
# A ≤ x ≤ B를 만족하는 모든 정수 x가 집합 S에 속하지 않는다.
# 집합 S와 n이 주어졌을 때, n을 포함하는 좋은 구간의 개수를 구해보자.

# import sys
# input = sys.stdin.readline
#
# L = int(input())
# elements = list(map(int, input().strip().split()))
# elements.sort()
# n = int(input())
#
# start = 0
# end = 0
# for i in range(len(elements)-1):
#     if elements[i] <= n <= elements[i+1]:
#         start = elements[i]
#         end = elements[i+1]
#         break
#
# cnt = 0
# for a in range(start+1, end):
#     for b in range(a+1, end):
#         if a <= n <= b:
#             cnt += 1
# print(cnt)

import sys
input = sys.stdin.readline

L = int(input())
elements = list(map(int, input().strip().split()))
n = int(input())
elements.sort()

cnt = 0         # 좋은 구간의 개수
start = 0
end = 0
for i in range(len(elements)):
    if elements[i] > n:
        start = elements[i-1]
        end = elements[i]
        break

if n < elements[0]:
    for a in range(1, n+1):
        for b in range(a+1, elements[0]):
            if a <= n <= b:
                cnt += 1
else:
    for a in range(start+1, n+1):
        for b in range(a+1, end):
            if a <= n <= b:
                cnt += 1
print(cnt)