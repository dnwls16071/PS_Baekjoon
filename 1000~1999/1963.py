# 소수를 유난히도 좋아하는 창영이는 게임 아이디 비밀번호를 4자리 ‘소수’로 정해놓았다. 어느 날 창영이는 친한 친구와 대화를 나누었는데:
#
# “이제 슬슬 비번 바꿀 때도 됐잖아”
# “응 지금은 1033으로 해놨는데... 다음 소수를 무엇으로 할지 고민중이야"
# “그럼 8179로 해”
# “흠... 생각 좀 해볼게. 이 게임은 좀 이상해서 비밀번호를 한 번에 한 자리 밖에 못 바꾼단 말이야. 예를 들어 내가 첫 자리만 바꾸면 8033이 되니까 소수가 아니잖아. 여러 단계를 거쳐야 만들 수 있을 것 같은데... 예를 들면... 1033 1733 3733 3739 3779 8779 8179처럼 말이야.”
# “흠...역시 소수에 미쳤군. 그럼 아예 프로그램을 짜지 그래. 네 자리 소수 두 개를 입력받아서 바꾸는데 몇 단계나 필요한지 계산하게 말야.”
# “귀찮아”
# 그렇다. 그래서 여러분이 이 문제를 풀게 되었다. 입력은 항상 네 자리 소수만(1000 이상) 주어진다고 가정하자. 주어진 두 소수 A에서 B로 바꾸는 과정에서도 항상 네 자리 소수임을 유지해야 하고, ‘네 자리 수’라 하였기 때문에 0039 와 같은 1000 미만의 비밀번호는 허용되지 않는다.

from itertools import permutations
import math
import sys
input = sys.stdin.readline

num = 9999999
prime_number = [True] * (num + 1)
prime_number[0] = False
prime_number[1] = False
for i in range(2, int(math.sqrt(num)) + 1):
    if prime_number[i]:
        for j in range(i*i, num+1, i):
            prime_number[j] = False

T = int(input())
for _ in range(T):
    cnt = 0
    number = input().strip()
    lenNumber = len(number)
    li = []
    for i in range(lenNumber):
        li.append(int(number[i]))
    for i in range(1, lenNumber+1):
        for j in list(set(permutations(li, i))):
            temp = ''.join(map(str, j))
            if temp[0] == "0":
                continue
            else:
                if prime_number[int(temp)]:
                    cnt += 1
    print(cnt)