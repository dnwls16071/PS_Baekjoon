# 실수 a와 정수 b가 주어졌을 때, a의 b제곱을 정확하게 계산하는 프로그램을 작성하시오.

from decimal import Decimal, getcontext
# decimal 모듈은 정확한 10진수 연산을 지원하는 라이브러리
# Decimal : 오차 없이 정확한 10진수를 표현하는 클래스
# getcontext() : decimal 모듈의 컨텍스트 : 정확도, 반올림 방식 등과 같은 정밀도 설정 요소
import sys
input = sys.stdin.readline

a, b = map(float, input().strip().split())
b = int(b)

def func(a, b, precision = 1100):
    getcontext().prec = precision
    decimal_a = Decimal(str(a))
    decimal_b = Decimal(str(b))

    result = decimal_a ** decimal_b
    return result

result = func(a, b)
formatted_result = format(result, 'f')
print(formatted_result)