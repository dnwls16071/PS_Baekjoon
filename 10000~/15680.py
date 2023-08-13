# 연세대학교의 영문명은 YONSEI, 슬로건은 Leading the Way to the Future이다.
#
# 이를 출력하는 프로그램을 작성해보도록 하자.

import sys
input = sys.stdin.readline

N = int(input())
if N == 0:
    print("YONSEI")
else:
    print("Leading the Way to the Future")