# 1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.
#
# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
# 예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다. 또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.
#
# 이 추측은 아직도 해결되지 않은 문제이다.
#
# 백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.

#1
# import sys
# input = sys.stdin.readline
#
# arr = [True] * 1000001
# arr[0] = False
# arr[1] = False
# for i in range(2, 1001):
#     if arr[i]:
#         for j in range(i*i, 1000001, i):
#             arr[j] = False
#
# while True:
#     n = int(input().strip())
#     if n == 0:
#         break
#
#     for i in range(len(arr)):
#         if arr[i] and arr[n-i]:
#             print(str(n), "=", str(i), "+", str(n-i))
#             break

#2
# import sys
# input = sys.stdin.readline
#
# arr = [True] * 1000001
# arr[0] = False
# arr[1] = False
# for i in range(2, 1001):
#     if arr[i]:
#         for j in range(i*i, 1000001, i):
#             arr[j] = False
#
# while True:
#     n = int(input().strip())
#     if n == 0:
#         break
#
#     a = 0
#     b = n
#     while True:
#         if a > b:
#             print("Goldbach's conjecture is wrong.")
#             break
#         if arr[a] and arr[b]:
#             print(str(n), "=", str(a), "+", str(b))
#             break
#         a += 1
#         b -= 1

#3
import sys
input = sys.stdin.readline

arr = [True] * 1000001
arr[0] = False
arr[1] = False
for i in range(2, 1001):
    if arr[i]:
        for j in range(i*i, 1000001, i):
            arr[j] = False

def check(n):
    for i in range(2, n):
        if arr[i] and arr[n-i]:
            print(str(n), "=", str(i), "+", str(n-i))
            return 0
    return 1

while True:
    try:
        n = int(input().strip())
        if n == 0:
            break
        if check(n):
            print("Goldbach's conjecture is wrong.")
    except EOFError:
        break