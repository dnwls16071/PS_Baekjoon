# 형준이는 수열을 하나 가지고 있다. 형준이는 수열을 정열적으로 정렬해보려 한다. 과연, 정렬할 수 있을까?

N = int(input())
lst = list(map(int, input().split()))

lst.sort()
for i in lst:
    print(i, end = " ")