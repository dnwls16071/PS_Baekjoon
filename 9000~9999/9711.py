# 피보나치 수열은 아래와 같이 표현된다.
#
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# 각 숫자는 앞의 두 숫자의 합으로 나타내는 것을 알 수 있다.
#
# P와 Q 그리고 n이 주어질 때, P번째 피보나치 숫자를 Q로 나눈 나머지를 구하여라.

#1 재귀함수를 이용한 피보나치 함수 구현(시간초과)
# import sys
# input = sys.stdin.readline
#
# def fibonacci(X):
#     if X == 0:
#         return 0
#     elif X == 1 or X == 2:
#         return 1
#     else:
#         return fibonacci(X-1) + fibonacci(X-2)
#
# seq = 1
# T = int(input())
# for i in range(T):
#     P, Q = map(int, input().strip().split())
#     result = fibonacci(P)
#     print("Case #" + str(seq) + ":", str(result % Q))
#     seq += 1

#2
import sys
input = sys.stdin.readline

dp = [0] * 10001
dp[1] = 1
dp[2] = 1
for i in range(3, 10001):
    dp[i] = dp[i-1] + dp[i-2]

seq = 1
T = int(input())
for i in range(T):
    P, Q = map(int, input().strip().split())
    result = dp[P]
    print("Case #" + str(seq) + ":", str(result % Q))
    seq += 1