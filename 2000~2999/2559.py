# 매일 아침 9시에 학교에서 측정한 온도가 어떤 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 알아보고자 한다.
#
# 예를 들어, 아래와 같이 10일 간의 온도가 주어졌을 때,
#
# 3 -2 -4 -9 0 3 7 13 8 -3
#
# 모든 연속적인 이틀간의 온도의 합은 아래와 같다.
#
#
#
# 이때, 온도의 합이 가장 큰 값은 21이다.
#
# 또 다른 예로 위와 같은 온도가 주어졌을 때, 모든 연속적인 5일 간의 온도의 합은 아래와 같으며,
#
#
#
# 이때, 온도의 합이 가장 큰 값은 31이다.
#
# 매일 측정한 온도가 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 계산하는 프로그램을 작성하시오.

N, K = map(int, input().split())
li = list(map(int, input().split()))

prefix_temperature_sum = [0]
val = 0
for i in range(len(li)):
    val += li[i]
    prefix_temperature_sum.append(val)

max = -1000000001
L = 0
R = 0
for i in range(1, N-K+2):
    L = i
    R = L+K-1
    if max < prefix_temperature_sum[R] - prefix_temperature_sum[L-1]:
        max = prefix_temperature_sum[R] - prefix_temperature_sum[L-1]
print(max)