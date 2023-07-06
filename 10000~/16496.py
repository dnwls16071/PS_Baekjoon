# 음이 아닌 정수가 N개 들어있는 리스트가 주어졌을 때, 리스트에 포함된 수를 나열하여 만들 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

#1
# from itertools import permutations
# import sys
# input = sys.stdin.readline
#
# N = int(input())
# li = list(map(int, input().strip().split()))
#
# Max = -1
# for i in permutations(li, len(li)):
#     i = int(''.join(map(str, i)))
#     if i > Max:
#         Max = i
# print(Max)

#2
# import sys
# input = sys.stdin.readline
#
# N = int(input())
# li = list(map(int, input().strip().split()))
#
# Maximum_length = 0
# for i in li:
#     i = str(i)
#     if Maximum_length < len(i):
#         Maximum_length = len(i)
#
# result = []
# for i in range(len(li)):
#     length = len(str(li[i]))
#     if length == Maximum_length:
#         result.append([int(li[i]), li[i]])
#     else:
#         temp = str(li[i]) * (Maximum_length - length + 1)
#         result.append([int(temp), li[i]])
# result.sort(key = lambda x : x[0], reverse=True)
#
# ans = ""
# for i in range(len(result)):
#     ans += str(result[i][-1])
# print(ans)

#3
import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().strip().split()))

result = []
for i in li:
    s = str(i)
    length = len(s)
    while len(s) < 10:
        s += s[len(s) - length]
    result.append([int(s), int(i)])
result.sort(key = lambda x : x[0], reverse=True)

ans = []
for i in result:
    ans.append(i[1])
print(int(''.join(map(str, ans))))