# 정보 초등학교에서는 단체로 2박 3일 수학여행을 가기로 했다. 여러 학년이 같은 장소로 수학여행을 가려고 하는데 1학년부터 6학년까지 학생들이 묵을 방을 배정해야 한다. 남학생은 남학생끼리, 여학생은 여학생끼리 방을 배정해야 한다. 또한 한 방에는 같은 학년의 학생들을 배정해야 한다. 물론 한 방에 한 명만 배정하는 것도 가능하다.
#
# 한 방에 배정할 수 있는 최대 인원 수 K가 주어졌을 때, 조건에 맞게 모든 학생을 배정하기 위해 필요한 방의 최소 개수를 구하는 프로그램을 작성하시오.
#
# 예를 들어, 수학여행을 가는 학생이 다음과 같고 K = 2일 때 12개의 방이 필요하다. 왜냐하면 3학년 남학생을 배정하기 위해 방 두 개가 필요하고 4학년 여학생에는 방을 배정하지 않아도 되기 때문이다.
#
# 학년	여학생	남학생
# 1학년	영희	동호, 동진
# 2학년	혜진, 상희	경수
# 3학년	경희	동수, 상철, 칠복
# 4학년	 	달호
# 5학년	정숙	호동, 건우
# 6학년	수지	동건

import sys
input = sys.stdin.readline

male_dict = {}
female_dict = {}
N, K = map(int, input().strip().split())
for _ in range(N):
    a, b = map(int, input().strip().split())
    # b: 학년
    if a == 1:  # 남학생
        if b not in male_dict:
            male_dict[b] = 1
        else:
            male_dict[b] += 1
    else:       # 여학생
        if b not in female_dict:
            female_dict[b] = 1
        else:
            female_dict[b] += 1

room = 0
for key, value in female_dict.items():
    if value % K == 0:
        room += value // K
    else:
        room += (value // K) + 1

for key, value in male_dict.items():
    if value % K == 0:
        room += value // K
    else:
        room += (value // K) + 1
print(room)