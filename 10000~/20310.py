# 어느 날, 타노스는 0과 1로 이루어진 문자열
# $S$를 보았다. 신기하게도,
# $S$가 포함하는 0의 개수와
# $S$가 포함하는 1의 개수는 모두 짝수라고 한다.
#
# 갑자기 심술이 난 타노스는
# $S$를 구성하는 문자 중 절반의 0과 절반의 1을 제거하여 새로운 문자열
# $S'$를 만들고자 한다.
# $S'$로 가능한 문자열 중 사전순으로 가장 빠른 것을 구하시오.

import sys
input = sys.stdin.readline

S = list(input().strip())

cnt_0 = S.count("0") // 2
cnt_1 = S.count("1") // 2

for i in range(cnt_0):
    S.pop(-S[::-1].index("0")-1)

for i in range(cnt_1):
    S.pop(S.index("1"))

print(''.join(map(str, S)))