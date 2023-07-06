# 정수 M개가 주어졌을 때, 모든 두 수의 쌍 중에서 가장 큰 최대공약수 찾는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

def GCD(a, b):
    if a > b:
        b, a = a, b
    while b > 0:
        a, b = b, a % b
    return a

N = int(input())
for _ in range(N):
    li = list(map(int, input().strip().split()))
    MAX = -1
    for a in range(len(li)):
        for b in range(a+1, len(li)):
            if MAX < GCD(li[a], li[b]):
                MAX = GCD(li[a], li[b])
    print(MAX)