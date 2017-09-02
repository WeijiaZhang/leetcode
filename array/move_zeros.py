class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        algorithm 1: consider four condition: (0,x), (0,0), (x,0), (x,x)
        """
        # if len(nums) <= 1:
        #     return
        # p1, p2 = 0, 1
        # while p2 < len(nums):
        #     if nums[p1] == 0 and nums[p2] != 0:
        #         nums[p1], nums[p2] = nums[p2], nums[p1]
        #         p1 += 1
        #         p2 += 1
        #     elif nums[p1] == 0 and nums[p2] == 0:
        #         p2 += 1
        #     # that is (x,0), (x,x)
        #     else:
        #         p1 += 1
        #         p2 += 1

        # conclusion swap solution
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
        # move all the nonzero advance
        nonzero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nonzero] = nums[i]
                nonzero += 1

        for i in range(nonzero, len(nums)):
            nums[i] = 0




