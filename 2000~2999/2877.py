# 창영이는 4와 7로 이루어진 수를 좋아한다. 창영이가 좋아하는 수 중에 K번째 작은 수를 구해 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

K = int(input())
S = format(K+1, "b")[1:]
S = S.replace("0", "4")
S = S.replace("1", "7")
print(S)