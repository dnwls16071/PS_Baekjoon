# 정수로 이루어진 크기가 같은 배열 A, B, C, D가 있다.
#
# A[a], B[b], C[c], D[d]의 합이 0인 (a, b, c, d) 쌍의 개수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

n = int(input())
A = []
B = []
C = []
D = []
for i in range(n):
    a, b, c, d = map(int, input().strip().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab_dict = {}
for a in A:
    for b in B:
        if a + b not in ab_dict:
            ab_dict[a + b] = 1
        else:
            ab_dict[a + b] += 1

result = 0
for c in C:
    for d in D:
        if -(c + d) in ab_dict:
            result += ab_dict[-(c + d)]
print(result)