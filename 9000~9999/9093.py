# 문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 단, 단어의 순서는 바꿀 수 없다. 단어는 영어 알파벳으로만 이루어져 있다.

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    sentence = list(map(str, input().strip().split()))
    for i in range(len(sentence)):
        sentence[i] = sentence[i][::-1]
    print(' '.join(map(str, sentence)))
