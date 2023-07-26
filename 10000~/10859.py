# 어제 자다가 알람 시계를 떨어뜨렸는지, 08:15분이 51:80분이 되어 있었다. 그때 나는 디지털로 표시된 어떤 숫자는 180도 뒤집혔을 때도 숫자가 될 수 있다는 걸 깨달았다.
#
#
#
# 소수 18115211이 디지털로 표시된 그림
#
#
#
# 18115211이 180도 뒤집혀서 11251181이 되었다. (소수가 아님)
#
# , , ,  은 뒤집혀서도 , , ,  그대로이다.
#  은 그냥 왼쪽으로 옮겨진다.
#  은 가 되고,  는 이 된다.
# , ,  은 더 이상 숫자가 아니다. (, , )
# 내가 좋아하는 숫자는 소수이다. 당신이 할 일은 주어진 숫자가 소수인지, 뒤집혀서도 소수인지 확인하는 것이다.

import sys
input = sys.stdin.readline
def isPrime(x):
    if x == 1 or x == 0:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

N = int(input())
if N == 2 or N == 5:    # 2, 5는 뒤집혀서도 2, 5 그대로 소수이므로 yes
    print("yes")
    exit(0)
if '3' in str(N) or '4' in str(N) or '7' in str(N):     # 3, 4, 7은 뒤집히면 더 이상 숫자가 아니므로 no
    print("no")
    exit(0)
if isPrime(N):  # 입력값 N이 소수이면?
    t = list(str(N))[::-1]
    for i in range(len(t)):
        if t[i] == '6': # 6을 뒤집으면 9가 된다.
            t[i] = '9'
        elif t[i] == '9': # 9를 뒤집으면 6이 된다.
            t[i] = '6'
    t = int(''.join(t))
    if isPrime(t):  # 뒤집은 수 역시 소수이면?
        print("yes")
    else:           # 뒤집은 수가 소수가 아니라면?
        print("no")
else:   # 입력값 N이 소수가 아니라면?
    print("no")
