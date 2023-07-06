# `오늘도 서준이는 버블 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.
#
# N개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 버블 정렬로 배열 A를 오름차순 정렬할 경우 정렬 과정에서 배열 A가 배열 B와 같은 경우가 발생하는지 확인해 보자. 초기 상태 배열 A도 정렬 과정에서 발생 가능한 경우로 생각하자.
#
# 크기가 N인 배열에 대한 버블 정렬 의사 코드는 다음과 같다.
#
# bubble_sort(A[1..N]) { # A[1..N]을 오름차순 정렬한다.
#     for last <- N downto 2
#         for i <- 1 to last - 1
#             if (A[i] > A[i + 1]) then A[i] <-> A[i + 1]  # 원소 교환
# }`
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

if A == B:
    print(1)
    sys.exit(0)

def bubble_sort(A, B):
    n = len(A)

    # Perform n-1 passes
    for i in range(n - 1):
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                if A[j+1] == B[j+1]:
                    if A == B:
                        print(1)
                        sys.exit(0)
    print(0)

bubble_sort(A, B)