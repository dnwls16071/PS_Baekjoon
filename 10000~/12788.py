# 2016년 5월 28일 제 2회 인하대학교 프로그래밍 경시대회(IUPC)가 개최된다. 이 대회는 다른 프로그래밍 경시대회와 다르게  손코딩으로 문제를 풀어야한다. CTP회장인 정은이는 모든 대회 참가자들에게 펜을 지급하기 위하여 펜을 구하기로 하였다. 대회 개최를 위한 예산을 아끼기 위하여 펜을 구매하지 않고 CTP회원들에게 펜을 빌리기로 하였다.
#
# CTP에는 N명의 회원들이 존재하며 각각의 회원들의 필통에 들어있는 펜의 개수는 모두 다르다. 정은이는 여러명의 회원에게 펜을 빌릴경우 펜을 돌려주기에 번거롭다고 생각하여 최소한의 회원들에게 펜을 빌려 참가자들에게 나누어 주려고 한다.
#
# 대회에 참가하는 참가자들은 팀을 구성해서 참가하는데 모든 팀원에게 펜을 지급해야한다. 한 팀이 k명의 팀원으로 구성되어 있을때 몇 명의 회원들에게 펜을 빌려야하는지 출력하시오.

import sys
input = sys.stdin.readline

N = int(input())
M, K = map(int, input().strip().split())
pencil = list(map(int, input().strip().split()))

total = M * K
pencil.sort(reverse=True)
cnt = 0
for i in pencil:
    total -= i
    if total <= 0:
        print(cnt+1)
        break
    cnt += 1

if total > 0:
    print("STRESS")