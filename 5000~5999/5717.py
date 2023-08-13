# 상근이의 남자 친구의 수와 여자 친구의 수가 주어졌을 때, 친구는 총 몇 명인지 구하는 프로그램을 작성하시오.

while True:
    A, B = map(int, input().strip().split())
    if A == 0 and B == 0:
        break
    print(A+B)