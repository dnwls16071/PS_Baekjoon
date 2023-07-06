# 유진이는 현수의 암호를 알아내려고 한다. 유진이는 사전 조사를 통해 임현수의 컴퓨터에 어떤 문자들이 쓰이는지 알아내었고, 하나씩 대입해보려고 한다. 대입하는 순서는 유진이가 메모한 문자 집합의 순서대로이고, 한 글자부터 암호가 풀릴 때까지 모두 대입해본다.
#
# 예를 들어, 메모한 문자 집합이 bca라고 한다면, 유진이는 b, c, a, bb, bc, ba, cb, cc, ca, ab, ac, aa, bbb, bbc, ........ 순서로 암호가 풀릴 때까지 계속 대입해본다.

import sys
input = sys.stdin.readline

chars = input().strip()
password = input().strip()

