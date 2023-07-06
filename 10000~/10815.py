# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

import sys

N = int(input())
own_card = set(map(int, sys.stdin.readline().split()))
M = int(input())
number_lst = list(map(int, sys.stdin.readline().split()))

lst = []
for i in number_lst:
    if i in own_card:
        lst.append(1)
    else:
        lst.append(0)
print(*lst)

# 이분탐색을 이용하는 방법도 고민해볼것