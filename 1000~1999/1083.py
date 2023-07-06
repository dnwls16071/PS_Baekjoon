# 크기가 N인 배열 A가 있다. 배열에 있는 모든 수는 서로 다르다. 이 배열을 소트할 때, 연속된 두 개의 원소만 교환할 수 있다. 그리고, 교환은 많아봐야 S번 할 수 있다. 이때, 소트한 결과가 사전순으로 가장 뒷서는 것을 출력한다.

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().strip().split()))
S = int(input())

for i in range(N):
    Max = max(A[i:min(N, i+1+S)])
    idx = A.index(Max)
    for j in range(idx, i, -1):
        A[j], A[j - 1] = A[j - 1], A[j]
    S -= (idx - i)

    if S <= 0:
        break

print(' '.join(map(str, A)))

# 1 2 3 4 5 6 7 8 9 10
# 10 1 2 3 4 5 6 7 8 9
# 10 9 1 2 3 4 5 6 7 8