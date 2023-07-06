# 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
#
# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
#
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

#1
# op = list(input().split("-"))
#
# result = 0
# if "0" in op[0] or "00" in op[0] or "000" in op[0] or "0000" in op[0] or "00000" in op[0]:
#     if "+" in op[0]:
#         result += eval(op[0])
#     else:
#         result += int(op[0])
# else:
#     if "+" in op[0]:
#         result += eval(op[0])
#     else:
#         result += int(op[0])
#
# for i in range(1, len(op)):
#     if "+" in op[i]:
#         arr = op[i].split("+")
#         temp = 0
#         for j in range(len(arr)):
#             arr[j] = str(arr[j])
#             if arr[j][0] == "0":
#                 temp += int(arr[j])
#             else:
#                 temp += int(arr[j])
#         result -= temp
#     else:
#         if "0" in op[i] or "00" in op[i] or "000" in op[i] or "0000" in op[i] or "00000" in op[i]:
#             result -= int(op[i])
#         else:
#             result -= int(op[i])
# print(result)

#2
op = list(input().split("-"))
result = 0
for i in op[0].split("+"):
    result += int(i)
for i in range(1, len(op)):
    for j in op[i].split("+"):
        result -= int(j)
print(result)