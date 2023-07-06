# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
#
# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

import math

M = int(input())
N = int(input())

def isPrime(number):
    cnt = 0
    for i in range(2, int(math.sqrt(number))+1):
        if number % i != 0:
            pass
        else:
             cnt += 1
    if number == 1:
        return False
    if cnt == 0:
        return True
    else:
        return False

prime_number = []
for i in range(M, N+1):
    if isPrime(i):
        prime_number.append(i)

if len(prime_number) == 0:
    print(-1)
else:
    print(sum(prime_number))
    print(min(prime_number))

