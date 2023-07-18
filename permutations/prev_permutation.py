def prev_permutations(nums):
    i = len(nums) - 1
    while i > 0 and nums[i - 1] <= nums[i]:
        i -= 1

    if i == 0:
        nums.sort(reverse=True)
        return

    j = len(nums) - 1
    while nums[j] >= nums[i-1]:
        j -= 1

    nums[i-1], nums[j] = nums[j], nums[i-1]
    nums[i:] = reversed(nums[i:])
    return nums