# -2진법은 부호 없는 2진수로 표현이 된다. 2진법에서는 20, 21, 22, 23이 표현 되지만 -2진법에서는 (-2)0 = 1, (-2)1 = -2, (-2)2 = 4, (-2)3 = -8을 표현한다. 10진수로 1부터 표현하자면 1, 110, 111, 100, 101, 11010, 11011, 11000, 11001 등이다.
#
# 10진법의 수를 입력 받아서 -2진수를 출력하는 프로그램을 작성하시오.

import sys

n = int(input())
result = ""
if n == 0:
    print(0)
    sys.exit()

while True:
    if n == 0:
        break
    else:
        if n < 0:
            temp = abs(n)
            if temp % 2 != 0:
                n = (abs(temp) // 2) + 1
                result += str((n * 2) - temp)
            else:
                n = (abs(temp) // 2)
                result += str((n * 2) - temp)
        elif n > 0:
            temp = n
            n = -(temp // 2)
            result += str((temp % 2))
print(result[::-1])