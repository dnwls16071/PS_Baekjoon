# 오늘도 서준이는 버블 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.
#
# N개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 버블 정렬로 배열 A를 오름차순 정렬할 경우 K 번째 교환되는 수를 구해서 우리 서준이를 도와주자.
#
# 크기가 N인 배열에 대한 버블 정렬 의사 코드는 다음과 같다.
#
# bubble_sort(A[1..N]) { # A[1..N]을 오름차순 정렬한다.
#     for last <- N downto 2
#         for i <- 1 to last - 1
#             if (A[i] > A[i + 1]) then A[i] <-> A[i + 1]  # 원소 교환
# }

import sys
input = sys.stdin.readline

A, K = map(int, input().strip().split())
array = list(map(int, input().strip().split()))
cnt = 0

def bubble_sort(array):
    global cnt, K
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                cnt += 1
                array[j], array[j+1] = array[j+1], array[j]
                if cnt == K:
                    print(array[j], array[j+1])
                    sys.exit(0)
    if cnt < K:
        print(-1)
        sys.exit(0)

bubble_sort(array)