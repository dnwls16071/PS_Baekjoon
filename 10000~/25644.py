# 미래를 예측하는 능력이 있는 정균이는 앞으로
# $N$일간 ANA 회사의 주가가 어떻게 변하는지 정확히 예측할 수 있다. 정균이는 예측한 결과를 바탕으로 ANA 회사의 주식 한 주를 적당한 시점에 사고 적당한 시점에 팔아서 최대한의 이득을 얻으려고 한다.
#
# ANA 회사의 앞으로
# $N$일간의 주가를
# $a_1, a_2, ..., a_N$이라고 하자. 정균이가
# $i$번째 날에 주식을 사고,
# $j$번째 날에 판다면
# $a_j - a_i$만큼의 이득을 얻을 수 있다. 정균이는 자금이 넉넉하기 때문에 주가가 아무리 높아도 주식을 살 수 있고, 상황이 여의치 않을 경우 사자마자 바로 팔 수도 있다.
#
# 앞으로
# $N$일간 ANA 회사의 주가가 주어졌을 때, 정균이가 주식 한 주를 적당한 시점에 사고 적당한 시점에 팔아서 얻을 수 있는 최대 이득은 얼마일까?

# import sys
# input = sys.stdin.readline
#
# N = int(input())
# ANA = list(map(int, input().strip().split()))
#
# Max_benefit = 0     # i날의 최대 이익
# result = 0          # 최대 이득
# for i in range(N-1, -1, -1):
#     Max_benefit = max(Max_benefit, ANA[i])
#     result = max(result, Max_benefit - ANA[i])
# print(result)

import sys
input = sys.stdin.readline

N = int(input())
stock = list(map(int, input().strip().split()))

# 최저가로 매수한 날이 최고가로 매도한 날보다 앞에 있다면?
if stock.index(min(stock)) < stock.index(max(stock)):
    print(max(stock) - min(stock))
# 최저가로 매수한 날이 최고가로 매도한 날보다 뒤에 있다면?
elif stock.index(min(stock)) > stock.index(max(stock)):
    # print(stock)
    stock.pop(stock.index(max(stock)))
    # print(stock)
# 최저가로 매수한 날과 최고가로 매도한 날이 같아서 결국 Zero가 된다면?
else:
    print(0)
