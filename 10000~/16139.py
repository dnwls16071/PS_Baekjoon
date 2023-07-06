# 승재는 인간-컴퓨터 상호작용에서 생체공학 설계를 공부하다가 키보드 자판이 실용적인지 궁금해졌다. 이를 알아보기 위해 승재는 다음과 같은 생각을 했다.
#
# '문자열에서 특정 알파벳이 몇 번 나타나는지 알아봐서 자주 나타나는 알파벳이 중지나 검지 위치에 오는 알파벳인지 확인하면 실용적인지 확인할 수 있을 것이다.'
#
# 승재를 도와 특정 문자열
# $S$, 특정 알파벳
# $\alpha$와 문자열의 구간
# $[l,r]$이 주어지면
# $S$의
# $l$번째 문자부터
# $r$번째 문자 사이에
# $\alpha$가 몇 번 나타나는지 구하는 프로그램을 작성하여라. 승재는 문자열의 문자는
# $0$번째부터 세며,
# $l$번째와
# $r$번째 문자를 포함해서 생각한다. 주의할 점은 승재는 호기심이 많기에 (통계적으로 크게 무의미하지만) 같은 문자열을 두고 질문을
# $q$번 할 것이다.

#1. 1차원 배열을 이용한 누적 합 알고리즘 이용
# import sys
# input = sys.stdin.readline
#
# input_string = input().strip()
# q = int(input())
# for i in range(q):
#     prefix_sum = [0]
#     Sum = 0
#     char, start, end = map(str, input().strip().split())
#     start, end = int(start), int(end)
#     for i in input_string:
#         if i == char:
#             Sum += 1
#             prefix_sum.append(Sum)
#         else:
#             prefix_sum.append(Sum)
#     print(prefix_sum[end+1] - prefix_sum[start])

import sys
input = sys.stdin.readline
from string import ascii_lowercase

S = input().rstrip()
q = int(input())
char_lst = {}
lst = ascii_lowercase
for i in lst:
    char_lst[i] = [0]
    count = 0
    for j in range(len(S)):
        if S[j] == i:
            count += 1
        char_lst[i].append(count)

for _ in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)
    print(char_lst[a][r+1] - char_lst[a][l])