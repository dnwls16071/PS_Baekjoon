# N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

#1
N, M = map(int, input().split())
A_li = list(map(int, input().split()))

start = 0
end = 0
cnt = 0
while True:
    if end == len(A_li):
        break
    else:
        if sum(A_li[start:end+1]) == M:
            cnt += 1
            start += 1
            end += 1
        elif sum(A_li[start:end+1]) > M:
            start += 1
        else:
            end += 1
print(cnt)

#2
N, M = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
right = 1
cnt = 0
while right <= N and left <= right:
    sum_nums = nums[left:right]
    total = sum(sum_nums)
    if total == M:
        cnt += 1
        right += 1
    elif total < M:
        right += 1
    else:
        left += 1
print(cnt)