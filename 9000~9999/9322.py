# 소희는 공개키와 개인키 한 쌍으로 보안을 유지하는 것이 매우 불편하다고 생각했다. 그래서 소희는 공개키만을 이용하는 암호화 체계를 개발했다. 이를 "철벽 보안 알고리즘"이라고 부르기로 했다. 알고리즘은 다음과 같다.
#
# 한 단어는 1~10개의 대문자(A-Z)들로 이루어진 문자열이다. 한 문장은 공백으로 구분된 단어들로 이루어졌다.
#
# 제 1 공개키는 최대 한 번만 사용된 단어들로 되어있다.
#
# 제 2 공개키는 제 1 공개키의 단어들을 재배치하여 만들어진다.
#
# 평문(암호화 되지 않은 문장)은 제 1 공개키와 같이 여러 단어들로 되어있지만, 제 1 공개키와 다르게 각 단어들은 중복이 가능하다.
#
# 암호문(암호화 된 문장)은 평문을 제 2 공개키를 만든 규칙의 반대로 재배치하여 만들어진다.
#
# 주어진 2개의 공개키와 암호문으로 평문을 복구하라.

from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    a = list(input().split())
    b = list(input().split())
    c = list(input().split())
    encryption_dict = defaultdict(int)
    for i in range(n):
        encryption_dict[b[i]] = c[i]
    for i in a:
        print(encryption_dict[i], end = " ")
