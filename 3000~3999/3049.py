# 세 대각선이 한 점에서 만나지 않는 볼록 N각형이 주어졌을 때, 대각선의 교차점의 개수를 세는 프로그램을 작성하시오.
#
# 아래 그림은 위의 조건을 만족하는 한 육각형의 교차점 그림이다.
#
# 모든 내부각이 180도보다 작은 다각형을 볼록 다각형이라고 한다.

import math

N = int(input())
if N == 3:
    print(0)
else:
    print(math.factorial(N) // (math.factorial(4) * math.factorial(N-4)))