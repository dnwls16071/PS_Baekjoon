# 첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

import sys
input = sys.stdin.readline

A, B, C = map(int, input().strip().split())

def power(a, b, m):
    if b == 0:
        return 1
    elif b == 1:
        return a % m

    tmp = power(a, b//2, m)
    if b % 2 == 0:
        return (tmp * tmp) % m
    else:
        return (tmp * tmp * a) % m

print(power(A, B, C))