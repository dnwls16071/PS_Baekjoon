# 정수 X가 주어졌을 때, X와 구성이 같으면서 X보다 큰 수 중 가장 작은 수를 출력한다.
#
# 수의 구성이 같다는 말은, 수를 이루고 있는 각 자리수가 같다는 뜻이다. 예를 들어, 123과 321은 수의 구성이 같다. 하지만, 123과 432는 구성이 같지 않다.

from itertools import permutations
import sys
input = sys.stdin.readline

flag = False
X = list(input().strip())
temp = int(''.join(map(str, X)))
for i in sorted(permutations(X, len(X))):
    t = int(''.join(map(str, i)))
    if temp < t:
        flag = True
        break

if flag:
    print(t)
else:
    print(0)