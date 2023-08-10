# Elly는 예상치 못하게 프로그래밍 대회를 준비하는 학생들을 가르칠 위기에 처했다. 대회는 정확히 3명으로 구성된 팀만 참가가 가능하다. 그러나 그녀가 가르칠 학생들에게는 큰 문제가 있었다. 코딩 실력이 좋으면 팀워크가 떨어지고, 팀워크가 좋을수록 코딩 실력이 떨어진다. 그리고 출전하고자 하는 대회는 코딩 실력과 팀워크 모두가 중요하다.
#
# Elly는 그녀가 가르칠 수 있는 모든 학생들의 코딩 실력을 알고 있다. 각각의 코딩 실력 Ai는 -10000부터 10000 사이의 정수로 표시되어 있다. 그녀는 팀워크와 코딩 실력이 모두 적절한 팀을 만들기 위해, 세 팀원의 코딩 실력의 합이 0이 되는 팀을 만들고자 한다. 이러한 조건 하에, 그녀가 대회에 출전할 수 있는 팀을 얼마나 많이 만들 수 있는지를 계산하여라.
#
# N명의 학생들의 코딩 실력 Ai가 -10000부터 10000사이의 정수로 주어질 때, 합이 0이 되는 3인조를 만들 수 있는 경우의 수를 구하여라.

from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

N = int(input())
coding = list(map(int, input().strip().split()))
coding.sort()
cnt = 0

for a in range(N-1):
    for b in range(a+1, N):
        temp = (coding[a] + coding[b]) * -1
        Left = bisect_left(coding, temp, a+1, b)
        Right = bisect_right(coding, temp, a+1, b)
        cnt += Right - Left
print(cnt)