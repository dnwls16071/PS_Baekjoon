# 전설적인 인천 식료품가게의 주인인 김인천 씨는 대대적인 할인행사를 계획하고 있습니다. 계산을 단순하게하기 위해 그는 25% 할인된 가격으로 상점의 모든 품목을 판매하기로 결정했습니다. 즉, 각 품목의 판매 가격은 정상 가격의 정확히 75 %입니다. 우연하게도 인천 식료품가게에서 판매하는 모든 물건의 정상가는 4의 배수인 정수이고, 할인된 가격 역시 편리하게도 모두 정수입니다.
#
# 김인천씨는 이 할인행사를 준비하기위해서 먼저 모든 판매물품의 할인된 판매가격을 프린터로 출력을 실행했고, 또한 할인행사 종료후 다시 쓸 모든 품목에 정상가격표 역시 출력을 실행하였습니다.
#
# 손님이 찾아와 잠깐 자리를 비웠던 김인천씨가 다시 가격표의 출력을 확인하기 위해서 프린터로 돌아와보니, 공교롭게 프린터는 모든 물품의 할인가격과 정상가격을 따로 구분하지 않고 오름차순으로 정렬한 뒤 순서대로 출력하여 하나의 출력물 더미를 만들었습니다. 각 품목의 할인가격표와 정상가격표 모두가 출력물 더미의 어딘가에 있습니다. 그러나 두 유형(할인가격, 정상가격)의 가격표는 비슷하게 보이고, 모든 품목의 가격을 기억하지 못하기 때문에 김인천씨는 어느 가격표가 할인가격표인지 확신할 수 없습니다. 이 상황에서 김인천씨는 무엇이 할인가격표인지 구분해낼 수 있을까요?
#
# 예를 들어, 정상가격이 20, 80, 100 인 경우 할인가격은 15, 60, 75이며 프린터의 인쇄출력더미는 오름차순으로 정렬된 15, 20, 60, 75, 80, 100 가격표들로 구성됩니다.

import sys
input = sys.stdin.readline

T = int(input())
for i in range(0, T):
    # 정가의 75% 할인된 값을 저장하는 배열
    result = []
    N = int(input())
    products = list(map(int, input().strip().split()))

    products = sorted(products, reverse=True)
    for price in products:
        if int(price * 0.75) in products:
            result.append(int(price * 0.75))
            products.remove(int(price * 0.75))
        else:
            pass
    result.sort()
    res = ' '.join(map(str, result))
    print("Case #" + str(i+1) + ": " + res)