# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
#
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.
#
# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().strip().split()))
temp = list(set(X))
temp.sort()
my_dict = {}

for i in range(len(temp)):
    if temp[i] in my_dict:
        pass
    else:
        my_dict[temp[i]] = i

for i in X:
    print(my_dict[i], end = " ")
