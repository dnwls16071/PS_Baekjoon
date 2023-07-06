# N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다. 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.
#
# 우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안 된다.
#
# 예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고, 주어진 연산자가 덧셈(+) 2개, 뺄셈(-) 1개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는 총 60가지의 식을 만들 수 있다. 예를 들어, 아래와 같은 식을 만들 수 있다.
#
# 1+2+3-4×5÷6
# 1÷2+3+4-5×6
# 1+2÷3×4-5+6
# 1÷2×3-4+5+6
# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 이에 따라서, 위의 식 4개의 결과를 계산해보면 아래와 같다.
#
# 1+2+3-4×5÷6 = 1
# 1÷2+3+4-5×6 = 12
# 1+2÷3×4-5+6 = 5
# 1÷2×3-4+5+6 = 7
# N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input().strip())
A_li = list(map(int, input().strip().split()))
op_cnt = list(map(int, input().strip().split()))

Max = -1000000000
Min = 1000000000

def recursion(idx, res):
    global Max, Min
    if idx == N:
        Max = max(Max, res)
        Min = min(Min, res)
        return
    # 덧셈의 개수
    if op_cnt[0] > 0:
        op_cnt[0] -= 1
        recursion(idx + 1, res + A_li[idx])
        op_cnt[0] += 1
    if op_cnt[1] > 0:
        op_cnt[1] -= 1
        recursion(idx + 1, res - A_li[idx])
        op_cnt[1] += 1
    if op_cnt[2] > 0:
        op_cnt[2] -= 1
        recursion(idx + 1, res * A_li[idx])
        op_cnt[2] += 1
    if op_cnt[3] > 0:
        op_cnt[3] -= 1
        recursion(idx + 1, int(res / A_li[idx]))
        op_cnt[3] += 1

recursion(1, A_li[0])
print(Max)
print(Min)