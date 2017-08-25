class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l_sum, r_sum = 0, 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                l_sum = max(l_sum+num, r_sum)
            else:
                r_sum = max(l_sum, r_sum+num)

        prev_yes, prev_no = 0,0
        # most fastest solution
        for num in nums:
            temp = prev_no
            prev_no = max(prev_no, prev_yes)
            prev_yes = num + temp
        return max(prev_yes, prev_no)

    '''
    solution: recuresive: slice to the sub solution
    rob(num[0:end]) = rob(num[0:end-1]) or rob(num[0:end-2]) + end
    however recur can not save mid-results which appear more than once
    so it wastes lots of time: Time Limited Exceeded
    '''
    def rob_recur(self, nums):
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            l_rob = self.rob_recur(nums[:-1])
            r_rob = self.rob_recur(nums[:-2]) + nums[-1]
            return max(l_rob, r_rob)