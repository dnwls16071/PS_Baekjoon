# n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.

n = int(input())
li = list(map(int, input().split()))
li.sort()
x = int(input())

i = 0
j = len(li)-1
cnt = 0
while True:
    if i >= j:
        break
    else:
        if li[i] + li[j] == x:
            i += 1
            cnt += 1
        elif li[i] + li[j] > x:
            j -= 1
        else:
            i += 1
print(cnt)