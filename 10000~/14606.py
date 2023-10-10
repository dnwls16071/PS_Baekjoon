# 갑은 아주대학교 학생입니다. 갑은 팔달관 1층에서 학과 개강총회를 준비하고 있습니다. 갑은 피자를 N 판 시켰습니다. 식탁 위에 피자 N 판이 탑처럼 쌓여있습니다. 갑은 높이가 N 인 이 한 피자탑을, 높이가 1인 피자탑들로 분리시켜야 합니다. 갑은 이 일을 하기 싫었습니다. 하지만 다음과 같은 격언이 있습니다.
#
# “피할 수 없다면 즐겨라!” - 로버트 엘리어트
#
# 격언대로, 갑은 혼자 놀기를 하며 즐겁게 일을 해결하기로 합니다. 그래서 다음과 같은 놀이를 하기로 했습니다.
#
# 먼저 놀이를 시작하기 전에, 식탁 위엔 N 개의 피자판이 하나의 탑으로 쌓여있습니다. 놀이가 시작되면, 갑은 식탁 위에 있는 피자탑들 중 하나를 고릅니다. 그리고 고른 피자탑을 두 개의 피자탑으로 분리합니다. 이때 갑은, 분리된 두 피자탑의 높이의 곱만큼 즐거움을 느낍니다. 즉, 갑이 고른 피자탑의 높이가 A이고, 갑이 이 피자탑을 높이 B인 피자탑과 높이 C인 피자탑으로 분리했다면, 갑은 이때 B * C만큼의 즐거움을 느낍니다. 단, 높이가 1인 피자탑은 더는 분리시키지 않습니다. 갑은 계속 피자탑들을 분리해나갑니다. 이 놀이를 하다가 식탁 위에 더 이상 분리할 수 있는 피자탑이 없어진다면, 갑의 개강총회 준비 일은 끝나게 됩니다.
#
# 갑은 문득, 혼자 놀기를 통해 얼마나 재밌게 놀 수 있을지 궁금해졌습니다. 갑이 주문한 피자판의 수 N 이 주어질 때, 갑이 혼자 놀기를 통해 얻을 수 있는 즐거움의 총합의 최댓값을 구해주세요.
#
#
#
# < 높이가 8인 피자탑을 높이가 4인 피자탑 둘로 분리시키는 과정 >

import sys
input = sys.stdin.readline

N = int(input())
pizza = [0] * 11
pizza[1] = 0

for i in range(1, N):
    pizza[i+1] = pizza[i] + i
print(pizza[N])