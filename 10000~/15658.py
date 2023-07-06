# N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 또, 수와 수 사이에 끼워넣을 수 있는 연산자가 주어진다. 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다. 연산자의 개수는 N-1보다 많을 수도 있다. 모든 수의 사이에는 연산자를 한 개 끼워넣어야 하며, 주어진 연산자를 모두 사용하지 않고 모든 수의 사이에 연산자를 끼워넣을 수도 있다.
#
# 우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안 된다.
#
# 예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고, 주어진 연산자가 덧셈(+) 3개, 뺄셈(-) 2개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는 총 250가지의 식을 만들 수 있다. 예를 들어, 아래와 같은 식을 만들 수 있다.
#
# 1+2+3-4×5÷6
# 1÷2+3+4-5×6
# 1+2÷3×4-5+6
# 1÷2×3-4+5+6
# 1+2+3+4-5-6
# 1+2+3-4-5×6
# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 이에 따라서, 위의 식 4개의 결과를 계산해보면 아래와 같다.
#
# 1+2+3-4×5÷6 = 1
# 1÷2+3+4-5×6 = 12
# 1+2÷3×4-5+6 = 5
# 1÷2×3-4+5+6 = 7
# 1+2+3+4-5-6 = -1
# 1+2+3-4-5×6 = -18
# N개의 수와 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.

#1
# from itertools import permutations
#
# import sys
# input = sys.stdin.readline
#
# N = int(input().strip())
# A = list(map(int, input().strip().split()))
# # [덧셈, 뺄셈, 곱셈, 나눗셈]
# op_cnt = list(map(int, input().strip().split()))
# op = [0] * op_cnt[0] + [1] * op_cnt[1] + [2] * op_cnt[2] + [3] * op_cnt[3]
#
# temp = list(set(permutations(op, N-1)))
#
# Max = -1000000000
# Min = 1000000000
# for i in temp:
#     result = A[0]
#     idx = 0
#     for j in i:
#         idx += 1
#         if j == 0:  # 덧셈
#             result += A[idx]
#         elif j == 1:# 뺄셈
#             result -= A[idx]
#         elif j == 2:# 곱셈
#             result *= A[idx]
#         elif j == 3:# 나눗셈
#             if result < 0:
#                 result = abs(result) // A[idx]
#             else:
#                 result = result // A[idx]
#     if result > Max:
#         Max = result
#     if result < Min:
#         Min = result
# print(Max)
# print(Min)

#2
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().strip().split()))
op_cnt = list(map(int, input().strip().split()))

Max = -1000000000
Min = 1000000000


def DFS(idx, result):
    global Max, Min
    if idx == N:
        Max = max(Max, result)
        Min = min(Min, result)
        return

    if op_cnt[0] > 0:
        op_cnt[0] -= 1
        DFS(idx + 1, result + A[idx])
        op_cnt[0] += 1
    if op_cnt[1] > 0:
        op_cnt[1] -= 1
        DFS(idx + 1, result - A[idx])
        op_cnt[1] += 1
    if op_cnt[2] > 0:
        op_cnt[2] -= 1
        DFS(idx + 1, result * A[idx])
        op_cnt[2] += 1
    if op_cnt[3] > 0:
        op_cnt[3] -= 1
        DFS(idx + 1, int(result / A[idx]))
        op_cnt[3] += 1


DFS(1, A[0])
print(Max)
print(Min)