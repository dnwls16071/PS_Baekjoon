def next_permutations(nums):
    i = len(nums) - 1
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1

    if i == 0:
        nums.sort()
        return

    j = len(nums) - 1
    while nums[j] <= nums[i-1]:
        j -= 1

    nums[i-1], nums[j] = nums[j], nums[i-1]
    nums[i:] = reversed(nums[i:])
    return nums

# 다음 순열 알고리즘
# 현재 순열 다음으로 올 수 있는 큰 순열을 구하는 문제
# 오름차순 정렬을 이용하는 부분으로 뒤에서부터 역순으로 탐색하여 오름차순이 깨지는 시점을 확인
# 다시 뒤에서부터 역순으로 탐색하여 교환하는 과정을 거침
# 오름차순이 꺠지는 시점부터 이후의 부분을 오름차순 정렬
