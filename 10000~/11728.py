# 정렬되어있는 두 배열 A와 B가 주어진다. 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오.

# import sys
#
# N, M = map(int, sys.stdin.readline().strip().split())
# A = list(map(int, sys.stdin.readline().strip().split()))
# B = list(map(int, sys.stdin.readline().strip().split()))
# lst = sorted(A + B)
# print(*lst)

import sys
N, M = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))
B = list(map(int, sys.stdin.readline().strip().split()))

lst = []
p1 = p2 = 0
while p1 < N and p2 < M:
    if A[p1] > B[p2]:
        lst.append(B[p2])
        p2 += 1
    else:
        lst.append(A[p1])
        p1 += 1

while p1 < N:
    lst.append(A[p1])
    p1 += 1

while p2 < M:
    lst.append(B[p2])
    p2 += 1

print(*lst)
