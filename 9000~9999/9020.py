# 1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.
#
# 골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.
#
# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

import sys
input = sys.stdin.readline

def sieve_of_Eratosthenes(n):
    arr = [True for _ in range(n+1)]
    arr[0] = False
    arr[1] = False
    for i in range(2, int(n**0.5)+1):
        if arr[i]:
            for j in range(2*i, n+1, i):
                arr[j] = False
    return [i for i in range(2, n+1) if arr[i]]

#1
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     li = sieve_of_Eratosthenes(n)
#     half = n // 2
#     for i in range(half, 1, -1):
#         if i in li and n-i in li:
#             print(i, n-i)
#             break

T = int(input())
for _ in range(T):
    n = int(input())
    li = sieve_of_Eratosthenes(n)
    a = n // 2
    while a > 0:
        if a in li and n - a in li:
            print(a, n-a)
            break
        a -= 1