# 모든 원소가 양의 정수인 집합이 있을 때, 원소를 거꾸로 뒤집고 그 원소를 오름차순으로 정렬하는 프로그램을 작성하세요.
#
# 단, 원소를 뒤집었을 때 0이 앞에 선행되는 경우는 0을 생략해야합니다.

import sys
input = sys.stdin.read

N, *S = input().split()
for i in range(int(N)):
    S[i] = S[i][::-1]
S = list(map(int, S))
print(*sorted(S), sep="\n")