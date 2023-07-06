# 총 N개의 문자열로 이루어진 집합 S가 주어진다.
#
# 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

N, M = map(int, input().split())
include_string = {}
for i in range(N):
    include_string[i] = input()

count = 0
for i in range(M):
    search_string = input()
    if search_string in include_string.values():
        count += 1
print(count)