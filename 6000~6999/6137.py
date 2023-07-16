# N개의 문자로 이루어진 문자열 S가 입력된다.
#
# 이 문자열의 각 문자들로 새로운 문자열 T를 만들려고한다.
#
# 문자열 S로 문자열 T를 만드는 규칙은 다음과 같다.
#
# 문자열 S의 가장 앞의 문자 하나를 문자열 T의 마지막에 추가한다.
# 문자열 S의 가장 뒤의 문자 하나를 문자열 T의 마지막에 추가한다.
# 위 규칙으로 만들어진 문자열 T들 중 사전순으로 가장 빠른 문자열을 출력하는 프로그램을 작성하시오.

# CBBABC > CBABBC
import sys
input = sys.stdin.readline

res = ""
N = int(input())
for _ in range(N):
    Str = input().strip()
    res += Str

ans = ""
left = 0
right = len(res) - 1
while left < right:
    if res[left] < res[right]:
        ans += res[left]
        left += 1
    elif res[left] > res[right]:
        ans += res[right]
        right -= 1
    # 이 문제의 핵심 : 사전순으로 앞선 출력(새로운 포인터를 만들어줌)
    else:
        left_next, right_next = left, right
        flag = True
        while left_next < right_next:
            if res[left_next] < res[right_next]:
                ans += res[left]
                left += 1
                flag = False
                break
            elif res[left_next] > res[right_next]:
                ans += res[right]
                right -= 1
                flag = False
                break
            else:
                left_next += 1
                right_next -= 1
        if flag:
            ans += res[right]
            right -= 1
ans += res[left]

result = list(ans)
for i in range(1, len(result)+1):
    print(result[i-1], end = "")
    if i % 80 == 0:
        print()