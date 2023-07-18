def next_permutations(nums):
    i = len(nums) - 1
    while i > 0 and nums[i-1] >= nums[i]:
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

# 테스트케이스
1 3 5 4 2

# 다음 순열을 구하라는 의미는 사전 순으로 봤을 때 더 큰 수가 앞에 위치하게끔 나오는 형태의 순열을 구하라는 문제가 된다.
# 1. 뒤에서부터 탐색을 진행하면 i = 2가 됨을 알 수 있다.(이 i값을 기준으로 뒤에 나오는 모든 값들을 오름차순 정렬하는데 사용한다.)
# 2. 문제에서 다음 순열을 위해서 바뀌어야 하는 부분은 3, 4이다. 따라서 14행과 같이 Swap을 진행한다.
# 3. i값을 기준으로 오름차순 정렬을 하고 nums를 반환한다.
