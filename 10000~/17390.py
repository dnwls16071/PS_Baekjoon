# 숭실골 높은 언덕 깊은 골짜기에 출제로 고통 받는 욱제가 살고 있다!
#
# 욱제는 또 출제를 해야 해서 단단히 화가 났다. 그래서 욱제는 길이 N짜리 수열 A를 만들고, A를 비내림차순으로 정렬해서 수열 B를 만들어 버렸다!! 여기서 B를 출력하기만 하면 문제가 너무 쉬우니까 하나만 더 하자. 아래와 같은 질문이 무려 Q개나 주어진다!! (ㅎㅎ;; ㅈㅅ.. ㅋㅋ!!)
#
# L R: BL + BL+1 + ... + BR-1 + BR 을 출력한다.
#
#
# Figure 1. 모든 참가자가 문제를 풀 수 있을 것이라고 기대하는 욱제의 표정
#
# 욱제의 질문에 답하고 함께 엠티를 떠나자!!

import sys
input = sys.stdin.readline

N, Q = map(int, input().strip().split())
prefix_sum = [0]
A = list(map(int, input().strip().split()))
A.sort()

Sum = 0
for i in range(len(A)):
    Sum += A[i]
    prefix_sum.append(Sum)

for i in range(Q):
    L, R = map(int, input().strip().split())
    print(prefix_sum[R] - prefix_sum[L-1])