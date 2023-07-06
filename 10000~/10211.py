# 크기 N인 정수형 배열 X가 있을 때, X의 부분 배열(X의 연속한 일부분) 중 각 원소의 합이 가장 큰 부분 배열을 찾는 Maximum subarray problem(최대 부분배열 문제)은 컴퓨터 과학에서 매우 잘 알려져 있다.
#
# 여러분은 N과 배열 X가 주어졌을 때, X의 maximum subarray의 합을 구하자. 즉, max1 ≤ i ≤  j ≤ N (X[i]+...+X[j])를 구하자.

T = int(input())
for _ in range(T):
    N = int(input())
    li = list(map(int, input().split()))
    for i in range(1, len(li)):
        li[i] = max(li[i], li[i] + li[i-1])
    print(max(li))