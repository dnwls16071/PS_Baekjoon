# 평행사변형은 평행한 두 변을 가진 사각형이다. 세 개의 서로 다른 점이 주어진다. A(xA,yA), B(xB,yB), C(xC,yC)
#
# 이때, 적절히 점 D를 찾아서 네 점으로 평행사변형을 만들면 된다. 이때, D가 여러 개 나올 수도 있다.
#
# 만들어진 모든 사각형 중 가장 큰 둘레 길이와 가장 작은 둘레 길이의 차이를 출력하는 프로그램을 작성하시오. 만약 만들 수 있는 평행사변형이 없다면 -1을 출력한다.

import math
Xa, Ya, Xb, Yb, Xc, Yc = map(int, input().split())

ac_length = math.sqrt((Xa-Xc)**2 + (Ya-Yc)**2)
ab_length = math.sqrt((Xa-Xb)**2 + (Ya-Yb)**2)
bc_length = math.sqrt((Xb-Xc)**2 + (Yb-Yc)**2)

round1 = (ac_length + ab_length) * 2
round2 = (ac_length + bc_length) * 2
round3 = (ab_length + bc_length) * 2
max_round = max(round1, round2, round3)
min_round = min(round1, round2, round3)

if ((Ya - Yc) * (Xa - Xb)) == ((Ya - Yb) * (Xa - Xc)):
    print(-1.0)
else:
    print(max_round - min_round)