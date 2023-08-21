# 다섯 개의 자연수가 있다. 이 수의 적어도 대부분의 배수는 위의 수 중 적어도 세 개로 나누어 지는 가장 작은 자연수이다.
#
# 서로 다른 다섯 개의 자연수가 주어질 때, 적어도 대부분의 배수를 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

number = list(map(int, input().strip().split()))
min_num = min(number)

while True:
    flag = 0
    # 적어도 3개로 나누어지는 가장 작은 자연수를 구하기 위한 변수 flag
    for num in number:
        if min_num % num == 0:
            flag += 1
    if flag > 2:
        break
    min_num += 1
print(min_num)