# 오늘도 서준이는 선택 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.
#
# N개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 선택 정렬로 배열 A를 오름차순 정렬할 경우 K 번 교환이 발생한 직후의 배열 A를 출력해 보자.
#
# N이 매우 커서 시간 초과를 고민하고 있는 우리 서준이를 도와주자.
#
# 크기가 N인 배열에 대한 선택 정렬 의사 코드는 다음과 같다.
#
# selection_sort(A[1..N]) { # A[1..N]을 오름차순 정렬한다.
#     for last <- N downto 2 {
#         A[1..last]중 가장 큰 수 A[i]를 찾는다
#         if (last != i) then A[last] <-> A[i]  # last와 i가 서로 다르면 A[last]와 A[i]를 교환
#     }
# }

import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
A = list(map(int, input().strip().split())) # 정렬이 수행되지 않은 리스트
B = sorted(A)       # 정렬이 수행된 리스트
dic = {}            # 사전

for idx, val in enumerate(A):
    dic[val] = idx

cnt = 0
for i in range(N-1, -1, -1):
    # A : [3, 1, 2, 4, 5]
    # B : [1, 2, 3, 4, 5]
    # 2, 3
    if A[i] != B[i]:
        temp = [A[i], B[i]]
        # 2, 3 → 3, 2
        A[i], A[dic[B[i]]] = A[dic[B[i]]], A[i]
        dic[temp[0]], dic[temp[1]] = dic[temp[1]], dic[temp[0]]
        cnt += 1
    if K == cnt:
        print(*A)
        sys.exit(0)
else:
    print(-1)