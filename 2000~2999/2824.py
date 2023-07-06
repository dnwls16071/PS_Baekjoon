# 상근이는 학생들에게 두 양의 정수 A와 B의 최대공약수를 계산하는 문제를 내주었다. 그런데, 상근이는 학생들을 골탕먹이기 위해 매우 큰 A와 B를 주었다.
#
# 상근이는 N개의 수와 M개의 수를 주었고, N개의 수를 모두 곱하면 A, M개의 수를 모두 곱하면 B가 된다.
#
# 이 수가 주어졌을 때, 최대공약수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input().strip())
N_li = list(map(int, input().strip().split()))
M = int(input().strip())
M_li = list(map(int, input().strip().split()))

result1 = 1
for i in N_li:
    result1 *= i

result2 = 1
for i in M_li:
    result2 *= i

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

GCD = str(gcd(result1, result2))
if len(GCD) > 9:
    print(GCD[len(GCD)-9:])
else:
    print(GCD)