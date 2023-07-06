# 1부터 n까지 차례대로 써 내려갈 때 특정 숫자(digit)의 빈도수를 구하여 출력하는 프로그램을 작성하시오.
#
# 예를 들어, n = 11 이고 숫자 1의 빈도수를 구하라고 하면, 1 2 3 4 5 6 7 8 9 10 11 에서 숫자 1은 1에서 한 번, 10에서 한 번, 11에서 두 번 나타나므로 1의 빈도수는 총 4 이다.

n, d = map(int, input().split())
digit_count = {'0' : 0, '1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0}
for i in range(1, n+1):
    j = str(i)
    for t in range(len(j)):
        digit_count[j[t]] += 1

print(digit_count[str(d)])