# 성원이는 다이어트를 시도중이다. 성원이는 정말 정말 무겁기 때문에, 저울이 부셔졌다. 성원이의 힘겨운 다이어트 시도를 보고만 있던 엔토피아는 성원이에게 새로운 저울을 선물해 주었다. 성원이는 엔토피아가 선물해준 저울 위에 올라갔다. “안돼!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! G 킬로그램이나 더 쪘어ㅜㅠ”라고 성원이가 말했다. 여기서 말하는 G킬로그램은 성원이의 현재 몸무게의 제곱에서 성원이가 기억하고 있던 몸무게의 제곱을 뺀 것이다.
#
# 성원이의 현재 몸무게로 가능한 것을 모두 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

G = int(input())

# G = (x+y)*(x-y)
x = [i for i in range(1, 100001)]
y = [j for j in range(1, 100001)]

X = 100000  # 현재 몸무게의 제곱 값
Y = 100000  # 기억하고 있던 몸무게의 제곱 값
res = []
left = 0
right = 0
while left < X and right < Y:
    if (x[left] + y[right]) * (x[left] - y[right]) == G:
        res.append(x[left])

    if (x[left] + y[right]) * (x[left] - y[right]) < G:
        left += 1
        continue
    right += 1

if len(res) == 0:
    print(-1)
else:
    res.sort()
    for i in res:
        print(i)