# 하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있다. 몇 가지 자연수의 예를 들어 보면 다음과 같다.
#
# 3 : 3 (한 가지)
# 41 : 2+3+5+7+11+13 = 11+13+17 = 41 (세 가지)
# 53 : 5+7+11+13+17 = 53 (두 가지)
# 하지만 연속된 소수의 합으로 나타낼 수 없는 자연수들도 있는데, 20이 그 예이다. 7+13을 계산하면 20이 되기는 하나 7과 13이 연속이 아니기에 적합한 표현이 아니다. 또한 한 소수는 반드시 한 번만 덧셈에 사용될 수 있기 때문에, 3+5+5+7과 같은 표현도 적합하지 않다.
#
# 자연수가 주어졌을 때, 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input())
prime_number = []
arr = [True] * (N+1)
arr[0] = False
arr[1] = False
for i in range(2, N+1):
    if arr[i]:
        prime_number.append(i)
        for j in range(i*i, N+1, i):
            arr[j] = False

cnt = 0
start = 0
end = 0
while end <= len(prime_number):
    if sum(prime_number[start:end+1]) == N:
        cnt += 1
        start += 1
        end += 1
    elif sum(prime_number[start:end+1]) > N:
        start += 1
    else:
        end += 1
print(cnt)



