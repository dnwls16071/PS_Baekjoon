# 백준 온라인 저지의 송년대회 Good Bye BOJ, 2021!의 개최일은 2021년 12월 31일이다. 원이는 대회가 개최된다는 사실이 기뻐 제목을 뚫어져라 보다가 2021이 무언가 특별하다는 사실을 깨달았다.
#
# 그렇다. 2021은 연속한 두 소수 43과 47의 곱이다. 다음에 이런년도가 오려면 무려 470년 뒤인 2491년이 되어야 한다. 원이는 어떤 수가 연속한 두 소수의 곱으로 이루어져 있으면 특별한 수라 부르기로 하였다.
#
# 주어진 수보다 큰 특별한 수 중 가장 작은 수를 구하는 프로그램을 작성하시오.

N = int(input())
prime_number = [True] * 104
prime_number[0] = False
prime_number[1] = False
for i in range(2, 104):
    if prime_number[i]:
        for j in range(2*i, 104, i):
            prime_number[j] = False

li = []
for i in range(len(prime_number)):
    if prime_number[i]:
       li.append(i)

result = []
for i in range(len(li)-1):
    result.append(li[i] * li[i+1])

for i in range(len(result)):
    if result[i] > N:
        print(result[i])
        break
    elif result[i] == N:
        print(result[i+1])
        break