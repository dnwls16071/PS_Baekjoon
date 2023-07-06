# 두 정수 A와 B가 있을 때, A에 포함된 숫자의 순서를 섞어서 새로운 수 C를 만들려고 한다. 즉, C는 A의 순열 중 하나가 되어야 한다.
#
# 가능한 C 중에서 B보다 작으면서, 가장 큰 값을 구해보자. C는 0으로 시작하면 안 된다.

#1
# from itertools import permutations
# import sys
# input = sys.stdin.readline
#
# A, B = map(str, input().strip().split())
# B = int(B)
# C = -1
#
# li = list(permutations(A))
# res = []
# for i in li:
#     res.append("".join(map(str, i)))
#
# for i in res:
#     if i[0] == "0":
#         continue
#     i = int(i)
#     if i < B:
#         C = max(C, i)
# print(C)

#2
import sys
input = sys.stdin.readline

A, B = map(str, input().split())
A = list(A)
B = list(B)
length = len(A)
checked = [False] * length
C = -1

# 이 때, current_num은 문자처럼 취급한다는 점을 주의할 것
def recursive(idx, current_num):
    global C
    if idx == length:
        if int(current_num) <= int(''.join(map(str, B))):
            C = max(C, int(current_num))
        return
    for i in range(length):
        if idx == 0 and A[i] == "0":
            continue
        if not checked[i]:
            checked[i] = True
            recursive(idx + 1, current_num + A[i])
            checked[i] = False

recursive(0, '')
print(C)