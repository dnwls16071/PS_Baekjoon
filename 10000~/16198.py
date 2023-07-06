# N개의 에너지 구슬이 일렬로 놓여져 있고, 에너지 구슬을 이용해서 에너지를 모으려고 한다.
#
# i번째 에너지 구슬의 무게는 Wi이고, 에너지를 모으는 방법은 다음과 같으며, 반복해서 사용할 수 있다.
#
# 에너지 구슬 하나를 고른다. 고른 에너지 구슬의 번호를 x라고 한다. 단, 첫 번째와 마지막 에너지 구슬은 고를 수 없다.
# x번째 에너지 구슬을 제거한다.
# Wx-1 × Wx+1의 에너지를 모을 수 있다.
# N을 1 감소시키고, 에너지 구슬을 1번부터 N번까지로 다시 번호를 매긴다. 번호는 첫 구슬이 1번, 다음 구슬이 2번, ... 과 같이 매겨야 한다.
# N과 에너지 구슬의 무게가 주어졌을 때, 모을 수 있는 에너지 양의 최댓값을 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def backtracking(s):
    global Max_energy
    if len(li) == 2:
        if s > Max_energy:
            Max_energy = s
        return
    else:
        for i in range(1, len(li)-1):
            r = li[i-1] * li[i+1]
            temp = li[i]
            del li[i]
            backtracking(s + r)
            li.insert(i, temp)

N = int(input().strip())
li = list(map(int, input().strip().split()))
Max_energy = 0
backtracking(0)
print(Max_energy)