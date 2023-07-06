# 윤진이는 이번에 카우버거 알바생으로 뽑히게 되었다. 그녀는 카우버거를 평소에 이용하면서 들었던 의문점 한가지가 있었다.
#
# "카우버거에는 왜 세트 메뉴에 대한 할인이 존재하지 않는가?"
#
# 따라서 윤진이의 아이디어로 카우버거에 세트 할인을 도입하고자 한다. 세트 메뉴는 버거 1개, 사이드 메뉴 1개, 음료 1개를 선택 할 경우 각각의 제품에 대해서 10%의 세트 할인을 적용하는 방식으로 진행된다.
#
# 하지만 카우버거 점주는 POS기의 소프트웨어가 오래되어 세트 할인에 대한 내용을 추가할 수가 없었다. 따라서 소프트웨어학부에 재학 중인 윤진이는 전공을 살려 직접 프로그램을 만들어보려고 한다. 윤진이를 도와 POS기에 들어갈 세트 할인에 대한 프로그램을 작성해보자.

import sys
input = sys.stdin.readline

B, C, D = map(int, input().strip().split())
burger_price = list(map(int, input().strip().split()))
side_price = list(map(int, input().strip().split()))
beverage_price = list(map(int, input().strip().split()))

burger_price.sort(reverse=True)
side_price.sort(reverse=True)
beverage_price.sort(reverse=True)

Not_discount_price = sum(burger_price) + sum(side_price) + sum(beverage_price)

burger_length = len(burger_price)
side_length = len(side_price)
beverage_length = len(beverage_price)
Min = min(burger_length, side_length, beverage_length)

Sum = 0
for i in range(Min):
    Sum += (burger_price[i] + side_price[i] + beverage_price[i]) * 0.9

Sum += sum(burger_price[Min:])
Sum += sum(side_price[Min:])
Sum += sum(beverage_price[Min:])

print(Not_discount_price)
print(int(Sum))