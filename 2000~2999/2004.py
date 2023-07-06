# $n \choose m$의 끝자리
# $0$의 개수를 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

def solution(n, k):
    cnt = 0
    while n > 1:
        n //= k
        cnt += n
    return cnt

cnt_5 = solution(n, 5) - solution(m, 5) - solution(n-m, 5)
cnt_2 = solution(n, 2) - solution(m, 2) - solution(n-m, 2)
print(min(cnt_2, cnt_5))