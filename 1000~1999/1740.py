# 3의 제곱수를 생각하자. 3의 0제곱, 3의 1제곱, 3의 2제곱, ... 은 순서대로 1, 3, 9, 27, ... 이 된다.
#
# 이를 바탕으로, 한 개 이상의 서로 다른 3의 제곱수의 합으로 표현되는 수를 생각할 수 있다. 예를 들어 30은 27과 3의 합이므로, 이러한 수에 포함된다.
#
# 한 개 이상의 서로 다른 3의 제곱수의 합으로 표현되는 N번째로 작은 수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

s = []
N = int(input())
while N > 0:
    s.append(N % 2)
    N //= 2

num = ''.join(map(str, s))
Sum = 0
for i in range(len(str(num))):
    if num[i] == "1":
        Sum += 3**i
print(Sum)