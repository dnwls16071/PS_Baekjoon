# 구사과는 지폐를 오직 두 종류만 가지고 있다. 바로 P원 지폐와 Q원 지폐이다. 이 두 종류의 지폐를 구사과는 무한대만큼 가지고 있다.
#
# 오늘 구사과가 구매하려고 하는 물건의 가격은 D원이다. 구사과가 이 물건을 구매하기 위해서 지불해야 하는 금액의 최솟값은 얼마일까?
#
# 물건을 구매하기 위해서는 물건의 가격보다 크거나 같은 금액을 지불해야 한다.

# import sys
# input = sys.stdin.readline
#
# def function(D, P, Q):
#     if D % P == 0 or D % Q == 0:
#         return D
#
#     P, Q = min(P, Q), max(P, Q)
#     Min_Q = D // Q + 1
#     answer = Min_Q * Q
#     # i : Q원 지폐의 개수
#     for i in range(Min_Q - 1, -1, -1):
#         # 가격 D원에서 Q원 지폐의 개수만큼 뺀 값을 P로 나눈 나머지
#         a, b = divmod((D - (i * Q)), P)
#         # 만약 나머지 b가 0이라면? > 나누어떨어졌다는 뜻
#         if b == 0:
#             return D
#         # Q원 지폐 i개 사용 + P원 지폐 (a + 1)개 사용
#         result = i * Q + ((a + 1) * P)
#         if result == D:
#             break
#         else:
#             answer = min(answer, result)
#     return answer
#
# D, P, Q = map(int, input().strip().split())
# print(function(D, P, Q))

D, P, Q = map(int, input().split())
if P < Q:
    P, Q = Q, P
min_cnt = (D // P + 1)  # 최소 개수 : D원을 P원 지폐로 모두 내는 경우
min_cost = min_cnt * P  # 최소 비용 : P원 지폐를 최소 개수만큼 지불하는 경우
if D % P == 0 or D % Q == 0:
    min_cost = D
else:
    for t in range(min_cnt - 1, -1, -1):
        div, mod = divmod(D - (t * P), Q)
        if mod == 0:
            min_cost = D
            break
        temp = (t * P) + ((div + 1) * Q)
        if temp == min_cost:
            break
        min_cost = min(min_cost, temp)
print(min_cost)