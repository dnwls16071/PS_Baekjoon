# 문자열 A와 B가 주어진다. 한 번 문자열을 바꾸는 것은 A의 한 글자를 골라서 문자열의 가장 처음으로 옮기는 것을 의미한다.
#
# A를 B로 바꾸기 위해서 문자열을 바꿔야 하는 횟수의 최솟값을 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

A_String = list(input().strip())
B_String = list(input().strip())

A_sort = sorted(A_String)
B_sort = sorted(B_String)

if A_sort != B_sort:
    print(-1)
    sys.exit()

if len(A_String) == 1:
    if str(''.join(map(str, A_sort))) == str(''.join(map(str, B_sort))):
        print(0)
    else:
        print(-1)
else:
    idx = len(A_String) - 1
    cnt = 0
    for i in range(len(A_String) - 1, -1, -1):
        if A_String[i] != B_String[idx]:
            cnt += 1
        else:
            idx -= 1
    print(cnt)