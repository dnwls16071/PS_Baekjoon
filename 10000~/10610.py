# 어느 날, 미르코는 우연히 길거리에서 양수 N을 보았다. 미르코는 30이란 수를 존경하기 때문에, 그는 길거리에서 찾은 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 만들고 싶어한다.
#
# 미르코를 도와 그가 만들고 싶어하는 수를 계산하는 프로그램을 작성하라.

#1
from itertools import permutations

N = list(input())

result = []
for i in permutations(N, len(N)):
    num = ""
    for j in range(len(i)):
        num += i[j]
    if int(num) % 30 == 0:
        result.append(int(num))
if len(result) == 0:
    print(-1)
else:
    print(max(result))

#2
N = list(input())
N.sort(reverse=True)
sum = ""
for i in N:
    sum += i
if int(sum) % 30 == 0:
    print(int(sum))
else:
    print(-1)