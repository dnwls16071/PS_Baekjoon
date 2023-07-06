# N과 L이 주어질 때, 합이 N이면서, 길이가 적어도 L인 가장 짧은 연속된 음이 아닌 정수 리스트를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N, L = map(int, input().strip().split())

x = 0
val = -1
for i in range(L, 101):
    ix = N - (i * (i+1) // 2)
    if ix % i == 0:
        val = ix // i
        if val >= -1:
            for j in range(val + 1, val + i + 1):
                print(j, end=" ")
            break
else:
    print(-1)