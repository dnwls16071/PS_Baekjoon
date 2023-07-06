# 세 정수 a, b, L이 주어졌을 때, LCM(a, b, c) = L을 만족하는 가장 작은 c를 찾는 프로그램을 작성하시오. LCM(a, b, c)는 a, b, c의 최소공배수이다.

import sys
input = sys.stdin.readline

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

a, b, L = map(int, input().strip().split())
LCM = a * b // gcd(a, b)

L_li = []
for i in range(1, int(L**0.5)+1):
    if L % i == 0:
        L_li.append(i)
        L_li.append(L // i)

L_li.sort()
flag = False
for i in L_li:
    if LCM * i // gcd(LCM, i) == L:
        print(i)
        flag = True
        break

if flag == False:
    print(-1)