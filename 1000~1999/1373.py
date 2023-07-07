# 2진수가 주어졌을 때, 8진수로 변환하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

binary = input()  # 이진수 입력
decimal = int(binary, 2)  # 2진수를 10진수로 변환

result = oct(decimal)   # 10진수를 8진수로 변환
print(result[2:])  # 8진수 출력