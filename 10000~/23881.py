# 오늘도 서준이는 선택 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.
#
# N개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 선택 정렬로 배열 A를 오름차순 정렬할 경우 K 번째 교환되는 수를 구해서 우리 서준이를 도와주자.
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
array = list(map(int, input().strip().split()))
cnt = 0

def selection_sort(array):
    global cnt
    # 가장 큰 수 A[i]를 찾는다.
    for i in range(len(array) - 1, 0, -1):
        max_index = i
        for j in range(i-1, -1, -1):
            if array[max_index] < array[j]:
                max_index = j
        if max_index != i:
            array[i], array[max_index] = array[max_index], array[i]
            cnt += 1
        if cnt == K:
            print(array[max_index], array[i])
            sys.exit(0)
    print(-1)

selection_sort(array)