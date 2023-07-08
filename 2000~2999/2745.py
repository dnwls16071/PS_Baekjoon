# B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.
#
# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
#
# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

import sys
input = sys.stdin.readline

N, B = map(str, input().strip().split())
N = ''.join(map(str, reversed(N)))
B = int(B)

answer = 0
def convert(N):
    global answer
    for i in range(len(N)):
        if N[i] in '0123456789':
            answer += int(N[i]) * (B ** i)
        else:
            answer += (ord(N[i]) - 55) * (B ** i)
    return answer

print(convert(N))