# 정수 n(0 ≤ n ≤ 4*109)가 주어졌을 때, n보다 크거나 같은 소수 중 가장 작은 소수 찾는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

def isprime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    n = int(input())

    while True:
        if n == 1:
            n += 1
        if isprime(n):
            print(n)
            break
        n += 1