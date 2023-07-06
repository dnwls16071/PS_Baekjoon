# 행복이는 길이가 $N$인 수열 $A$에서 소수들을 골라 최소공배수를 구해보려고 한다.
# 행복이를 도와 이를 계산해주자.

#1
# import sys
# input = sys.stdin.readline
#
# N = int(input())
# arr = set(map(int, input().strip().split()))
# Max = max(arr)
#
# prime_number_lst = []
# prime_number = [True] * (Max+1)
# prime_number[0] = False
# prime_number[1] = False
# for i in range(2, Max+1):
#     if prime_number[i]:
#         prime_number_lst.append(i)
#         for j in range(i*i, Max+1, i):
#             prime_number[j] = False
#
# result = 1
# for i in arr:
#     if prime_number[i]:
#         result *= i
#
# if result == 1:
#     print(-1)
# else:
#     print(result)

#2
import sys
input = sys.stdin.readline

N = int(input())
arr = set(map(int, input().strip().split()))

is_prime = [True] * 1000001
is_prime[0] = False
is_prime[1] = False
for i in range(2, len(is_prime)):
    if is_prime[i]:
        for j in range(i*i, len(is_prime), i):
            is_prime[j] = False

result = 1
for i in arr:
    if is_prime[i]:
        result *= i

if result == 1:
    print(-1)
else:
    print(result)