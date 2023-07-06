# 수빈이가 세상에서 가장 좋아하는 것은 소수이고, 취미는 소수를 가지고 노는 것이다. 요즘 수빈이가 가장 관심있어 하는 소수는 7331이다.
#
# 7331은 소수인데, 신기하게도 733도 소수이고, 73도 소수이고, 7도 소수이다. 즉, 왼쪽부터 1자리, 2자리, 3자리, 4자리 수 모두 소수이다! 수빈이는 이런 숫자를 신기한 소수라고 이름 붙였다.
#
# 수빈이는 N자리의 숫자 중에서 어떤 수들이 신기한 소수인지 궁금해졌다. N이 주어졌을 때, 수빈이를 위해 N자리 신기한 소수를 모두 찾아보자.

import sys
input = sys.stdin.readline

N = int(input().strip())

def prime_number(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def recursive(x):
    if len(str(x)) == N:
        print(x)
    for i in range(10):
        val = 10 * x + i
        if prime_number(val):
            recursive(val)

recursive(2)
recursive(3)
recursive(5)
recursive(7)