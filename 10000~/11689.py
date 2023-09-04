# 자연수 n이 주어졌을 때, GCD(n, k) = 1을 만족하는 자연수 1 ≤ k ≤ n 의 개수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input())
answer = N

for i in range(2, int(N**0.5)+1):
    if N % i == 0:
        while N % i == 0:
            N //= i
        answer -= answer // i

if N > 1:
    answer -= answer // N
print(answer)