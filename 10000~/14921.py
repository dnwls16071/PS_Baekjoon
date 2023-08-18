# 홍익대 화학연구소는 다양한 용액을 보유하고 있다. 각 용액은 -100,000,000부터 100,000,000사이의 특성 값을 갖는데,
#
# 같은 양의 두 용액을 혼합하면, 그 특성값은 두 용액의 특성값의 합이 된다.
#
# 당신은 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 하는데, 각 용액은 10ml시험관에 10ml씩 들어있고, 빈 20ml 시험관이 단 하나 있다. 게다가 용액을 계량할 수 없어서, 두 용액을 섞을 때는 10ml씩 섞어서 20ml로 만드는데, 단 한번밖에 할 수 없다. 그래서 미리 용액의 특성값들을 보고, 어떤 두 용액을 섞을 것인지 정해야 한다.
#
# 예를 들어, 연구소에 있는 용액들의 특성값이 [-101, -3, -1, 5, 93]이라고 하자. 이 경우에 특성 값이 각각 -101, 93인 용액을 혼합하면 -8인 용액을 만들 수 있다. 또한 특성값이 5인 용액과 93인 용액을 혼합하면 특성 값이 98인 용액을 만들 수 있다. 모든 가능한 조합을 생각해 보면, 특성값이 2인 용액이 0에 가장 가까운 용액이다.
#
# 용액들의 특성값 A1, … ,AN이 오름차순으로 주어졌을 때, 이 중 두 개의 용액을 혼합하여 만들 수 있는 0에 가장 가까운 특성값 B를 출력하시오.

import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().strip().split()))
min_value = float('INF')

start = 0
end = N-1
while start < end:
    if abs(liquid[start] + liquid[end]) < abs(min_value):
        min_value = liquid[start] + liquid[end]

    if liquid[start] + liquid[end] > 0:
        end -= 1
    elif liquid[start] + liquid[end] < 0:
        start += 1
    else:
        break
print(min_value)
