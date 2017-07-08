def permute_dfs(nums, path, results):
    if not nums:
        results.append(path)
        return
    for i in xrange(len(nums)):
        permute_dfs(nums[:i]+nums[i+1:], path+[nums[i]], results)


def permute_cpp(nums, begin, results):
    if begin >= len(nums)-1:
        print(nums)
        # nums has not changed even print(nums) is changed!
        new_nums = list(nums)
        results.append(new_nums)
        return
    for i in xrange(begin, len(nums)):
        nums[begin], nums[i] = nums[i], nums[begin]
        permute_cpp(nums, begin+1, results)
        nums[begin], nums[i] = nums[i], nums[begin]


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    results = []
    # permute_dfs(nums, [], results)
    permute_cpp(nums, 0, results)
    return results
