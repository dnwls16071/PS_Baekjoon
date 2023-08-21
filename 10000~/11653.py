# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input())

def function(N):
    lst = []
    i = 2
    while N != 1:
        if N % i == 0:
            lst.append(i)
            N //= i
        else:
            i += 1
    return lst

result = function(N)
for i in result:
    print(i)