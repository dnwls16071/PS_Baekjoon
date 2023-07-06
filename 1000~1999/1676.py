# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

import math
N = int(input())

N_factorial = math.factorial(N)
cnt = 0
while True:
    if N_factorial % 10 == 0:
        N_factorial //= 10
        cnt += 1
    else:
        break
print(cnt)